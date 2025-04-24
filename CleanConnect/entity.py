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

class UserAccount:
    def __init__(self, user_id=None, name=None, username=None, email=None, password=None, role_id=None, suspended=None):
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
            user.role = role_map.get(user.role_id, "Unknown")  # add role_name as extra field
            account_list.append(user)

        return account_list
    
    def updateAccount(self, user_id, new_name, new_username, new_email, new_password, new_role_id):
        # Perform the database update logic for the provided user ID
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
        cursor.execute(query, (new_name, new_username, new_email, new_password, new_role_id, user_id))
        db.commit()
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
            cursor.execute(query, (name, username, password ,email, role_id))
            db.commit()
            print("Account created successfully")
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            db.rollback()
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
        
    def setSuspended(self, user_id: int, suspended: bool):
        cursor = db.cursor()
        cursor.execute(
            "UPDATE useraccounts SET suspended=%s WHERE user_id=%s",
            (1 if suspended else 0, user_id)
        )
        db.commit()
        cursor.close()

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
        cursor.execute(query, (new_role, role_id))
        db.commit()
        cursor.close()

class CleanerService:
    def __init__(self, clean_svc_id=None, cleaner_id=None, category_id=None,service_id=None, price=None, description=None):
        self.clean_svc_id = clean_svc_id
        self.cleaner_id = cleaner_id 
        self.category_id = category_id                 
        self.service_id = service_id                    
        self.price = price
        self.description = description
        
    def addService(self, cleaner_id, category_id, service_id, price, description):
        print(f"Adding service with cleaner_id={cleaner_id}, category_id={category_id}, service_id={service_id}, price={price}, description={description}")
        cursor = db.cursor()
        query = """
            INSERT INTO cleaner_service (cleaner_id, category_id,service_id, price, description)
            VALUES (%s, %s, %s, %s, %s)
        """
        cursor.execute(query, (cleaner_id, category_id, service_id, price, description))
        db.commit()
        cursor.close()

        return True

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
        services = cursor.fetchall()
        cursor.close()

        result = []
        for row in services:
            service_obj = CleanerService(
                cleaner_id=row[0],
                service_id=row[1],
                price=row[2],
                description=row[3]
            )
            service_obj.service_name = row[4]
            service_obj.category_name = row[5]
            result.append(service_obj)

        return result
    
    def updateService(self, cleaner_id, service_id, new_price, new_description):
        try:
            print(f"Trying to update with cleaner_id={cleaner_id}, service_id={service_id}, new_price={new_price}, new_description={new_description}")
            cursor = db.cursor()
            query = """
                UPDATE cleaner_service
                SET price = %s, description = %s
                WHERE cleaner_id = %s AND service_id = %s
            """
            cursor.execute(query, (new_price, new_description, cleaner_id, service_id))
            db.commit()
            if cursor.rowcount > 0:
                print("Service updated successfully!")
            else:
             print("No service found with the provided cleaner_id and service_id.")
        except Exception as e:
            print(f"Error updating service: {e}")
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
        
    def searchCleanerServices(self, search_query):
        cursor = db.cursor()
        query = """
                SELECT cs.clean_svc_id, cs.cleaner_id, cs.category_id, cs.service_id, cs.price, cs.description, s.`cat/sv_name` AS service_name, c.`cat/sv_name` AS category_name
                FROM `cleaner_service` cs
                JOIN `categories_services` s ON cs.service_id = s.`catsv_id`
                JOIN `categories_services` c ON cs.category_id = c.`catsv_id`
                WHERE s.`cat/sv_name` LIKE %s
        """
        cursor.execute(query, (f"%{search_query}%",))
        services = cursor.fetchall()
        cursor.close()

        service_list = []
        for service in services:
            service_list.append(CleanerService(service[0], service[1], service[2], service[3], service[4], service[5]))
        return service_list



class CategoryService:
    def __init__(self, catsv_id=None, cat_sv_name=None, parentCat_id =None):
        self.catsv_id = catsv_id
        self.cat_sv_name = cat_sv_name
        self.parentCat_id = parentCat_id

    def getAllCategories(self):
        cursor = db.cursor()
        cursor.execute("SELECT catsv_id, `cat/sv_name`, parentCat_id FROM categories_services WHERE parentCat_id IS NULL")
        rows = cursor.fetchall()
        cursor.close()
        return [CategoryService(*row) for row in rows]

    def getServicesByCategory(self, parentCat_id):
        cursor = db.cursor()
        cursor.execute("SELECT catsv_id, `cat/sv_name`, parentCat_id FROM categories_services WHERE parentCat_id = %s", (parentCat_id,))
        rows = cursor.fetchall()
        cursor.close()
        return [CategoryService(*row) for row in rows]



        





# RANDOM STUFF FOR CI TESTING PLEASE IGNORE
