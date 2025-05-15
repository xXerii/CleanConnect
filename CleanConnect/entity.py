import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "clean_connect",
    port = 3306

)

if db.is_connected():
    print("Connected succesfully")

else:
    print("Connection failed")

class UserProfile:
    def __init__(self, role_id=None, role=None, suspended=None):
        self.role_id = role_id
        self.role = role
        self.suspended = suspended

    def viewProfiles(self):
        cursor = db.cursor()
        query = "SELECT * FROM userprofile"
        cursor.execute(query)
        profiles = cursor.fetchall()
        cursor.close()

        profile_list = []
        for profile in profiles:
            profile = UserProfile(profile[0], profile[1], profile[2])
            profile_list.append(profile)

        return profile_list
        
    def searchProfiles(self, search_query):
        cursor = db.cursor()
        query = "SELECT * FROM userprofile WHERE role LIKE %s" 
        cursor.execute(query, (f"%{search_query}%",)) # Comma after the formatted string to make it a single-element tuple, wont work without
        profiles = cursor.fetchall()
        cursor.close()

        profile_list = []
        for profile in profiles:
            profile_list.append(UserProfile(profile[0], profile[1], profile[2]))
        return profile_list
    
    def updateProfile(self, role_id, new_role):
        # Perform the database update logic for the provided user ID
        cursor = db.cursor()
        query = "UPDATE userprofile SET role =%s WHERE role_id = %s "
        try:
            cursor.execute(query, (new_role, role_id))
            db.commit()
            print("Profile updated successfully # DEBUG TRUE")
            return True
        except mysql.connector.Error as err:
            print(f"Error: {err} # DEBUG FALSE")
            db.rollback()
            return False
          
        finally:
            cursor.close()

    def createProfile(self, role):
        cursor = db.cursor()
        query = """
            INSERT INTO userprofile (
                role
            ) VALUES (%s)
        """
        try:
            cursor.execute(query, (role,))
            db.commit()
            print("Profile created successfully # DEBUG TRUE")
            return True
        except mysql.connector.Error as err:
            print(f"Error: {err} # DEBUG FALSE")
            db.rollback()
            return False
        
        finally:
            cursor.close()
    
    def setProfileSuspension(self, role_id: int, suspended: bool):
        try:
            cursor = db.cursor(buffered=True)

            sql1 = """
                UPDATE userprofile
                   SET suspended= %s
                 WHERE role_id = %s
            """
            cursor.execute(sql1, (suspended, role_id))

            sql2 = """
                UPDATE useraccounts
                SET suspended = %s
                WHERE role_id = %s
                """
            cursor.execute(sql2, (suspended, role_id))

            db.commit()
            return True

        except Exception as e:
            print("Error toggling profile:", e)
            db.rollback()
            return False

        finally:
            cursor.close()

class UserAccount:
    profile: UserProfile
    
    def __init__(self, user_id=None, name=None, username=None, email=None, password=None, role_id=None, suspended=None, profile: UserProfile =None):
        self.profile = profile
        self.user_id = user_id
        self.name = name
        self.username = username
        self.email = email
        self.password = password
        self.role_id = role_id
        self.suspended = suspended

    def viewAccounts(self):
        cursor = db.cursor()
        query = "SELECT * FROM useraccounts"
        cursor.execute(query)
        accounts = cursor.fetchall()

        # Fetch role mapping
        cursor.execute("SELECT role_id, role FROM userprofile")
        role_map = dict(cursor.fetchall())

        cursor.close()

        account_list = []
        for account in accounts:
            user = UserAccount(account[0], account[1], account[2], account[3], account[4], account[5], account[6])
            user.role = role_map.get(user.role_id, "Unknown")
            account_list.append(user)

        return account_list
    
    def updateAccount(self, user_id, new_name, new_username, new_email, new_password, new_role_id):
        cursor = db.cursor()
        query = """
            UPDATE useraccounts
            SET name = %s,
                username = %s,
                email = %s,
                password = %s,
                role_id = %s
            WHERE user_id = %s
        """
        try:
            cursor.execute(
                query,
                (new_name, new_username, new_email, new_password, new_role_id, user_id)
            )
            db.commit()
            print("Account updated successfully # DEBUG TRUE")
            return True
        except mysql.connector.Error as err:
            print(f"Error: {err} # DEBUG FALSE")
            db.rollback()
            return False
        finally:
            cursor.close()

    def searchAccounts(self, search_query):
        cursor = db.cursor()
        query = "SELECT * FROM useraccounts WHERE username LIKE %s" 
        cursor.execute(query, (f"%{search_query}%",)) # Comma after the formatted string to make it a single-element tuple, wont work without
        accounts = cursor.fetchall()
        cursor.close()

        account_list = []
        for account in accounts:
            account_list.append(UserAccount(account[0], account[1], account[2], account[3], account[4], account[5], account[6]))
        return account_list
    
    def createAccount(self, name, username, password, email, role_id):
        cursor = db.cursor()
        query = """
            INSERT INTO useraccounts (name, username, password, email, role_id)
            VALUES (%s, %s, %s, %s, %s)
        """
        try:
            cursor.execute(query, (name, username, password, email, role_id))
            db.commit()
            print("Account created successfully # DEBUG TRUE")
            return True
        except mysql.connector.Error as err:
            print(f"Error: {err} # DEBUG FALSE")
            db.rollback()
            return False
        finally:
            cursor.close()

    def loginAccount(self, username, password):
        cursor = db.cursor()
        query = """
            SELECT ua.user_id, ua.name, ua.username, ua.email, ua.password, ua.role_id, ua.suspended
            FROM useraccounts ua
            WHERE ua.username = %s AND ua.password = %s
        """
        cursor.execute(query, (username, password))
        row = cursor.fetchone()
        cursor.close()

        if not row:
            return None

        # Unpack including suspended flag
        uid, name, username, email, pw, role, suspended = row
        return UserAccount(uid, name, username, email, pw, role, suspended)
        
    def setAccountSuspension(self, user_id: int, suspended: bool):
        try:
            cursor = db.cursor()
            cursor.execute(
                "UPDATE useraccounts SET suspended=%s WHERE user_id=%s",
                (1 if suspended else 0, user_id)
            )
            db.commit()
            return True
        except Exception as e:
            print(f"Error setting suspension status: {e} # DEBUG FALSE")
            db.rollback()
            return False
        finally:
            cursor.close()

class CleanerService:
    def __init__(self, clean_svc_id=None, cleaner_id=None, category_id=None,service_id=None, price=None, description=None, service_name=None, category_name=None):
        self.clean_svc_id = clean_svc_id
        self.cleaner_id = cleaner_id 
        self.category_id = category_id                 
        self.service_id = service_id                    
        self.price = price
        self.description = description
        self.service_name = service_name
        self.category_name = category_name

    def addService(self, cleaner_id, category_id, service_id, price, description):
        print(f"Adding service with cleaner_id={cleaner_id}, category_id={category_id}, service_id={service_id}, price={price}, description={description}")
        try:
            cursor = db.cursor()

            # 1) Check for an existing row with the same cleaner_id & service_id
            dup_check_sql = """
                SELECT 1
                FROM cleaner_service
                WHERE cleaner_id = %s
                AND service_id = %s
                LIMIT 1
            """
            cursor.execute(dup_check_sql, (cleaner_id, service_id))
            if cursor.fetchone():
            # already exists → bail out
                return False
            
            query = """
                INSERT INTO cleaner_service (cleaner_id, category_id, service_id, price, description)
                VALUES (%s, %s, %s, %s, %s)
            """
            cursor.execute(query, (cleaner_id, category_id, service_id, price, description))
            db.commit()
            return True
        
        except Exception as e:
            print(f"Error adding service: {e}")
            db.rollback()
            return False
        finally:
            cursor.close()
    
    def getCleanerServicesByUser(self, user_id):
        cursor = db.cursor()
        query = """
            SELECT cs.cleaner_id, cs.service_id, cs.price, cs.description, s.`cat/sv_name` AS service_name, c.`cat/sv_name` AS category_name
            FROM cleaner_service cs
            JOIN categories_services s ON cs.service_id = s.catsv_id
            JOIN categories_services c ON cs.category_id = c.catsv_id
            WHERE cs.cleaner_id = %s
        """
        cursor.execute(query, (user_id,))
        rows = cursor.fetchall()
        cursor.close()

        services = []
        for row in rows:
            service_obj = CleanerService(
                cleaner_id=row[0],
                service_id=row[1],
                price=row[2],
                description=row[3]
            )
            service_obj.service_name = row[4]
            service_obj.category_name = row[5]
            services.append(service_obj)

        return services
    
    def updateService(self, cleaner_id, service_id, new_price, new_description):
        try:
            print(f"Trying to update with cleaner_id={cleaner_id}, service_id={service_id}, new_price={new_price}, new_description={new_description}")
            cursor = db.cursor()
            query = """
                UPDATE cleaner_service
                    SET price       = %s,
                        description = %s
                  WHERE cleaner_id  = %s
                    AND service_id  = %s
            """
            cursor.execute(query, (new_price, new_description, cleaner_id, service_id))
            db.commit()

        # cursor.rowcount is the number of rows affected by the last execute()
            if cursor.rowcount > 0:
                print("Service updated successfully!")
                return True
            else:
                print("No service found with the provided cleaner_id and service_id.")
                return False

        except Exception as e:
            print(f"Error updating service: {e}")
            db.rollback()
            return False

        finally:
                cursor.close()
    
    def deleteService(self, cleaner_id, service_id):
        try:
            cursor = db.cursor()
            # Use sub queries to delete 
            query = """ 
                DELETE FROM cleaner_service
                WHERE clean_svc_id = (
                SELECT clean_svc_id
                FROM cleaner_service
                WHERE cleaner_id = %s AND service_id = %s
                LIMIT 1
                )
             """
            cursor.execute(query, (cleaner_id, service_id))
            db.commit()
            if cursor.rowcount > 0:
                print(f"Service with cleaner_id={cleaner_id} and service_id={service_id} deleted successfully!")
                return True
            else:
                print(f"No service found with cleaner_id={cleaner_id} and service_id={service_id}")
                return False
        except Exception as e:
            print(f"Error deleting service: {e}")
            return False
        finally:
            cursor.close()
    
    def searchCleanerServices(self, search_query,cleaner_id):
        cursor = db.cursor()
        query = """
                SELECT cs.clean_svc_id, cs.cleaner_id, cs.category_id, cs.service_id, cs.price, cs.description, s.`cat/sv_name` AS service_name, c.`cat/sv_name` AS category_name
                FROM `cleaner_service` cs
                JOIN `categories_services` s ON cs.service_id = s.`catsv_id`
                JOIN `categories_services` c ON cs.category_id = c.`catsv_id`
                WHERE s.`cat/sv_name` LIKE %s AND cs.cleaner_id = %s
        """
        cursor.execute(query, (f"%{search_query}%",cleaner_id))
        services = cursor.fetchall()
        cursor.close()

        service_list = []
        for service in services:
            service_list.append(CleanerService(service[0], service[1], service[2], service[3], service[4], service[5], service[6], service[7]))
        return service_list
    
    def getJobHistoryByCleaner(self, cleaner_id):
        cursor = db.cursor()
        query = """
            SELECT 
            jh.cleaner_id, jh.booked_by, c.`cat/sv_name` AS service_provided, jh.total_charged,
            jh.booked_at
            FROM job_history jh
            JOIN categories_services c 
            ON jh.service_id = c.catsv_id
            WHERE jh.cleaner_id = %s
            ORDER BY 
            STR_TO_DATE(jh.booked_at, '%d/%m/%y') ASC
        """
        cursor.execute(query, (cleaner_id,))
        result = cursor.fetchall()
        cursor.close()

        # Convert tuples to dictionaries
        job_history = []
        for row in result:
            job_history.append({
                "cleaner_id": row[0],
                "booked_by": row[1],
                "service_provided": row[2],
                "total_charged": row[3],
                "booked_at": row[4]
            })

        return job_history
    
    def getCleanerProfile(self, cleaner_id):
        cursor = db.cursor()
        query = """ 
        SELECT 
            ua.user_id AS cleaner_id,
            ua.name AS cleaner_name,
            ua.email AS cleaner_email,
            cs.category_id,
            cat1.`cat/sv_name` AS category_name,
            cs.service_id,
            cat2.`cat/sv_name` AS service_name,
            cs.price,
            cs.description
        FROM 
            useraccounts ua
        INNER JOIN 
            cleaner_service cs ON ua.user_id = cs.cleaner_id
        LEFT JOIN 
            categories_services cat1 ON cs.category_id = cat1.catsv_id
        LEFT JOIN 
            categories_services cat2 ON cs.service_id = cat2.catsv_id
        WHERE 
            ua.user_id = %s
            AND ua.role_id = 2;
        """

        cursor.execute(query, (cleaner_id,))
        result = cursor.fetchall()
        cursor.close()

        return result

    def searchAllServices(self, search_query):
        cursor = db.cursor()
        query = """
        SELECT 
            cs.clean_svc_id, 
            cs.cleaner_id, 
            cs.category_id, 
            cs.service_id, 
            cs.price, 
            cs.description, 
            sv.`cat/sv_name` AS service_name, 
            cat.`cat/sv_name` AS category_name
        FROM 
            cleaner_service cs
        INNER JOIN 
            categories_services sv ON cs.service_id = sv.catsv_id
        INNER JOIN 
            categories_services cat ON cs.category_id = cat.catsv_id
        WHERE 
            cat.`cat/sv_name` LIKE %s OR sv.`cat/sv_name` LIKE %s  -- Search both category and service names
        """
        cursor.execute(query, (f"%{search_query}%", f"%{search_query}%")) 
        rows = cursor.fetchall()
        cursor.close()

        service_list = []
        for row in rows:
            service_obj = CleanerService(
                clean_svc_id=row[0],
                cleaner_id=row[1],
                category_id=row[2],
                service_id=row[3],
                price=row[4],
                description=row[5],
                service_name=row[6],
                category_name=row[7]
            )
            service_list.append(service_obj)

        return service_list
    
    def searchShortlistedServicesByCategory(self, user_id, search_query):
        cursor = db.cursor()
        query = """
        SELECT 
            sl.cleaner_id,
            sl.category_id,
            sl.service_id,
            cs.price,
            sv.`cat/sv_name` AS service_name,
            cat.`cat/sv_name` AS category_name
        FROM 
            shortlist sl
        JOIN 
            categories_services sv ON sl.service_id = sv.catsv_id
        JOIN 
            categories_services cat ON sl.category_id = cat.catsv_id
        JOIN 
            cleaner_service cs ON sl.service_id = cs.service_id
        WHERE 
            sl.homeowner_id = %s AND (sv.`cat/sv_name` LIKE %s OR cat.`cat/sv_name` LIKE %s)
        """
        cursor.execute(query, (user_id, f"%{search_query}%", f"%{search_query}%")) 
        rows = cursor.fetchall()
        print(rows)
        cursor.close()

        service_list = []
        for row in rows:
            service_obj = CleanerService(
                cleaner_id=row[0],
                category_id=row[1],
                service_id=row[2],
                price=row[3],
                service_name=row[4],
                category_name=row[5]
            )
            service_list.append(service_obj)

        return service_list


    def getAllAvailableService(self):
        cursor = db.cursor()
        query = """
        SELECT 
            cs.clean_svc_id,
            cs.cleaner_id,
            cs.category_id,
            cs.service_id,
            cs.price,
            cs.description,
            sv.`cat/sv_name` AS service_name,
            cat.`cat/sv_name` AS category_name
        FROM 
            cleaner_service cs
        INNER JOIN 
            categories_services sv ON cs.service_id = sv.catsv_id
        INNER JOIN 
            categories_services cat ON cs.category_id = cat.catsv_id
        ORDER BY 
            cat.`cat/sv_name` ASC, sv.`cat/sv_name` ASC;
        """
        cursor.execute(query)
        rows = cursor.fetchall()
        cursor.close()

        services = []
        for row in rows:
            service_obj = CleanerService(
                    clean_svc_id=row[0],
                    cleaner_id=row[1],
                    category_id=row[2],
                    service_id=row[3],
                    price=row[4],
                    description=row[5],
                    service_name=row[6],
                    category_name=row[7]
            )

            services.append(service_obj)

        return services
    
    def getShortlistedServices(self, homeowner_id):
        cursor = db.cursor()
        cursor.execute("""
                SELECT 
                    cs.cleaner_id,  -- Cleaner ID
                    cat.catsv_id AS category_id,  -- Category ID
                    cs.service_id,  -- Service ID
                    s.`cat/sv_name` AS service_name,  -- Service Name
                    cat.`cat/sv_name` AS category_name,  -- Category Name
                    cs.price  -- Price
                FROM shortlist sl
                JOIN cleaner_service cs ON sl.service_id = cs.service_id AND sl.cleaner_id = cs.cleaner_id
                JOIN categories_services s ON cs.service_id = s.catsv_id  -- Service Name
                JOIN categories_services cat ON s.parentCat_id = cat.catsv_id  -- Category Name
                WHERE sl.homeowner_id = %s;
            """, (homeowner_id,))
    
        results = []
        for row in cursor.fetchall():
            obj = CleanerService(
                cleaner_id=row[0],
                category_id=row[1],
                service_id=row[2],
                service_name=row[3],
                category_name=row[4],
                price=row[5]
            )
            results.append(obj)
    
        cursor.close()
        return results
    
     # -------- short-lists ----------
    def addShortlist(self, cleaner_id, homeowner_id, category_id, service_id):
        try:
            cur = db.cursor()

            # Check for existing entry
            cur.execute(
                """
                SELECT 1
                  FROM shortlist
                 WHERE cleaner_id = %s
                   AND homeowner_id = %s
                   AND category_id = %s
                   AND service_id = %s
                """,
                (cleaner_id, homeowner_id, category_id, service_id)
            )
            if cur.fetchone() is not None:
                return False

            cur.execute(
                """
                INSERT INTO shortlist (cleaner_id, homeowner_id, category_id, service_id)
                VALUES (%s, %s, %s, %s)
                """,
                (cleaner_id, homeowner_id, category_id, service_id)
            )
            db.commit()
            return True

        except Exception as e:
            print(f"Error in addShortlist: {e}")
            db.rollback()
            return False

        finally:
            cur.close()
    
    def removeShortlist(self, cleaner_id, homeowner_id,category_id, service_id):
        cursor = db.cursor()
        try:
            query = """
                DELETE FROM shortlist 
                WHERE cleaner_id = %s AND homeowner_id = %s 
                AND category_id = %s AND service_id = %s
            """
            cursor.execute(query, (cleaner_id, homeowner_id, category_id, service_id))
            db.commit()

            if cursor.rowcount > 0:
                print("Shortlist entry removed successfully.")
                return True  # Successfully removed
            else:
                print("No matching shortlist entry found.")
                return False  # No matching entry to remove
            
        except Exception as e:
            db.rollback()
            print("Failed to remove shortlist entry:", e)
        finally:
            cursor.close()


class CategoryService:
    def __init__(self, catsv_id=None, cat_sv_name=None, parentCat_id =None, cat_desc=None):
        self.catsv_id = catsv_id
        self.cat_sv_name = cat_sv_name
        self.parentCat_id = parentCat_id
        self.cat_desc = cat_desc


    def getAllCategories(self):
        cursor = db.cursor()
        cursor.execute("SELECT catsv_id, `cat/sv_name`, parentCat_id, cat_desc FROM categories_services WHERE parentCat_id IS NULL")
        rows = cursor.fetchall()
        cursor.close()
        return [CategoryService(*row) for row in rows]

    def getServicesByCategory(self, parentCat_id):
        cursor = db.cursor()
        cursor.execute("SELECT catsv_id, `cat/sv_name`, parentCat_id FROM categories_services WHERE parentCat_id = %s", (parentCat_id,))
        rows = cursor.fetchall()
        cursor.close()
        return [CategoryService(*row) for row in rows]
    
    def fetchCleanersByCategory(self, category_id):
        cursor = db.cursor()

        query = """
            SELECT u.name, u.email
            FROM useraccounts u
            JOIN cleaner_service cs ON u.user_id = cs.cleaner_id
            JOIN categories_services cat ON cs.service_id = cat.catsv_id
            WHERE cat.parentCat_id = %s AND u.role_id = %s
        """
        cleaner_role_id = 2  # replace with actual role_id value for cleaners
        cursor.execute(query, (category_id, cleaner_role_id))
        rows = cursor.fetchall()
        cursor.close()

        return [UserAccount(name=row[0], email=row[1]) for row in rows]

    def addCategory(self, cat_sv_name, cat_desc):
        cursor = db.cursor()
        try:
            query = """
           INSERT INTO categories_services (`cat/sv_name`, parentCat_id, cat_desc)
            VALUES (%s, NULL, %s) 
            """
            cursor.execute(query, (cat_sv_name, cat_desc))
            db.commit()
            return True
    
        except Exception as e:
            db.rollback()
            print("Error adding category:", e)
            return False
        
    def addNewService(self, cat_sv_name, parentCat_id):
        cursor = db.cursor()
        try:
        # First, check if the parent category exists
            cursor.execute("SELECT catsv_id FROM categories_services WHERE catsv_id = %s", (parentCat_id,))
            result = cursor.fetchone()

            # If the parent category does not exist, create a new one
            if result is None:
                print(f"Parent category with ID {parentCat_id} does not exist. Creating a new category...")
                cursor.execute("""
                INSERT INTO categories_services (`cat/sv_name`, parentCat_id)
                VALUES (%s, %s)
            """, (f"New Category {parentCat_id}", None))  # Insert a new parent category
                db.commit()
                parentCat_id = cursor.lastrowid  # Get the ID of the newly created category
                print(f"New parent category created with ID {parentCat_id}")

            query = """
            INSERT INTO categories_services (`cat/sv_name`, parentCat_id)
            VALUES (%s, %s)
            """
            cursor.execute(query, (cat_sv_name, parentCat_id))
            db.commit()
            return True
        
        except Exception as e:
            db.rollback()
            print(f"Error adding new service: {e}")
            return False

        finally:
            cursor.close()
        
    def deleteCategory(self, catsv_id): # ON DELETE CASCADE
        cursor = db.cursor()
        try:
            cursor.execute("DELETE FROM categories_services WHERE catsv_id = %s AND parentCat_id IS NULL", (catsv_id,))
            db.commit()
            return True
        except Exception as e:
            db.rollback()
            print(f"Error deleting category: {e}")
            return False
        finally:
            cursor.close()

    def updateCategoryDesc(self, catsv_id, new_desc):
        cursor = db.cursor()
        try:
            cursor.execute(
                "UPDATE categories_services SET cat_desc = %s WHERE catsv_id = %s",
                (new_desc, catsv_id)
            )
            db.commit()
            return True
        except Exception as e:
            db.rollback()
            print(f"Error updating description: {e}")
            return False
        finally:
            cursor.close()
    
    def searchCategories(self, search_query):
        cursor = db.cursor()
        sql = """
            SELECT catsv_id,
                    `cat/sv_name`,
                   cat_desc
              FROM categories_services
             WHERE `cat/sv_name` LIKE %s
        """
        # note the comma: makes it a single‐element tuple
        cursor.execute(sql, (f"%{search_query}%",))
        rows = cursor.fetchall()
        cursor.close()

        category_list = []
        for row in rows:
            # adjust the constructor args to match your Category model
            category_list.append(
                CategoryService(
                    catsv_id=row[0],
                    cat_sv_name=row[1],
                    cat_desc=row[2]
                )
            )
        return category_list


class CleanerAnalytics:
    """Logs views & short-lists and returns live counts."""
    def __init__(self):
        self.conn = db

    # -------- profile views --------
    def log_view(self, cleaner_id, viewer_id):
        cur = self.conn.cursor()
        cur.execute(
            "INSERT INTO profile_view (cleaner_id, viewer_id) VALUES (%s,%s)",
            (cleaner_id, viewer_id)
        )
        self.conn.commit();  cur.close()

    def view_count(self, cleaner_id):
        cur = self.conn.cursor()
        cur.execute("SELECT COUNT(*) FROM profile_view WHERE cleaner_id=%s",
                    (cleaner_id,))
        cnt = cur.fetchone()[0];  cur.close()
        return cnt

    def shortlist_count(self, cleaner_id):
        cur = self.conn.cursor()
        cur.execute("SELECT COUNT(*) FROM shortlist WHERE cleaner_id=%s",
                    (cleaner_id,))
        cnt = cur.fetchone()[0];  cur.close()
        return cnt

    def shortlist_count_for_user(self, cleaner_id, homeowner_id):
        cur = self.conn.cursor()
        cur.execute("SELECT 1 FROM shortlist "
                    "WHERE cleaner_id=%s AND homeowner_id=%s",
                    (cleaner_id, homeowner_id))
        exists = cur.fetchone()
        cur.close()
        return bool(exists)

class BookedServices:
    def __init__(self):
        self.db = db  # Assuming `db` is your database connection object
    
    def getBookedServices(self, user_id):
        """
        Fetch booked services for a specific user from the booked_services table.
        """
        cursor = self.db.cursor()
        query = """
            SELECT 
                bs.cleaner_id,
                bs.cleaner_name,
                bs.category_id,
                cs.`cat/sv_name` AS service_name,
                bs.total_charged,
                bs.booked_at
            FROM 
                booked_services bs
            JOIN 
                categories_services cs ON bs.catsv_id = cs.catsv_id
            WHERE 
                bs.user_id = %s
            ORDER BY 
                bs.booked_at DESC
        """
        cursor.execute(query, (user_id,))
        result = cursor.fetchall()
        cursor.close()

         # Format the result into a list of dictionaries
        booked_services = []
        for row in result:
            booked_services.append({
                "cleaner_id": row[0],
                "cleaner_name": row[1],
                "category_id": row[2],
                "service_name": row[3],  # Fetch service name instead of service_id
                "total_charged": row[4],
                "booked_at": row[5]
            })

            return booked_services
        

# ------------------------------------------------------------------
# Booking reports
# ------------------------------------------------------------------
class BookingReports:
    def __init__(self):
        self.conn = db                          # uses your existing connection

    # ❶ bookings grouped by category
    def by_category(self, date_from, date_to):
        cur = self.conn.cursor()
        cur.execute("""
            SELECT cs.`cat/sv_name` AS category,
                   COUNT(*)          AS booked
            FROM   booked_services  b
                   JOIN categories_services cs
                     ON b.category_id = cs.catsv_id
            WHERE  DATE(b.booked_at) BETWEEN %s AND %s
            GROUP  BY cs.`cat/sv_name`
        """, (date_from, date_to))
        rows = cur.fetchall()
        cur.close()
        
        return {cat.strip(): cnt for cat, cnt in rows}

    # number of distinct cleaners booked
    def cleaners_booked(self, date_from, date_to):
        cur = self.conn.cursor()
        cur.execute("""
            SELECT COUNT(DISTINCT cleaner_id)
            FROM   booked_services
            WHERE  DATE(booked_at) BETWEEN %s AND %s
        """, (date_from, date_to))
        count = cur.fetchone()[0]
        cur.close()
        return count

    def getBookingsByCleaner(self, start, end):
        cur = db.cursor()
        cur.execute("""
            SELECT cleaner_name, COUNT(*)
            FROM booked_services
            WHERE booked_at BETWEEN %s AND %s
            GROUP BY cleaner_name
        """, (start, end))
        rows = cur.fetchall(); cur.close()
        return {name.strip(): cnt for name, cnt in rows}

        

# RANDOM STUFF FOR CI TESTING PLEASE IGNORE
