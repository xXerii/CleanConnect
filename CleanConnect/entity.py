import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "clean_connect",
    port = 3307

)

if db.is_connected():
    print("Connected succesfully")

else:
    print("Connection failed")

class UserAccount:
    def __init__(self, id=None, username=None, password=None, role_id=None, suspended=None):
        self.id = id
        self.username = username
        self.password = password
        self.role_id = role_id
        self.suspended = suspended

    def fetchAllAccounts(self):
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
            user = UserAccount(account[0], account[1], account[2], account[3], account[4])
            user.role = role_map.get(user.role_id, "Unknown")  # add role_name as extra field
            account_list.append(user)

        return account_list

    def createAccount(self, username, password, role_id, suspended=0):
        cursor = db.cursor()
        query = """
            INSERT INTO useraccounts (username, password, role_id, suspended)
            VALUES (%s, %s, %s, %s)
        """
        try:
            cursor.execute(query, (username, password, role_id, suspended))
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
            SELECT ua.id, ua.username, ua.password, ua.role_id
            FROM useraccounts ua
            WHERE ua.username = %s AND ua.password = %s
        """
        cursor.execute(query, (username, password))
        account = cursor.fetchone()
        cursor.close()

        if account:
            return UserAccount(*account)  # Unpack: id, username, password, role_id
        else:
            return None

class UserProfile:
    def __init__(self, role_id=None, role=None, suspended=None):
        self.role_id = role_id
        self.role = role
        self.suspended = suspended

    def fetchAllProfiles(self):
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

        





# RANDOM STUFF FOR CI TESTING PLEASE IGNORE
