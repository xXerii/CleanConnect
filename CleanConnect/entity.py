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
    def __init__(self, id=None, username=None, password=None, role_id=None):
        self.id = id
        self.username = username
        self.password = password
        self.role_id = role_id

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
        





# RANDOM STUFF FOR CI TESTING PLEASE IGNORE