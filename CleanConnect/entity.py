import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "clean_connect"
)

if db.is_connected():
    print("Connected succesfully")

else:
    print("Connection failed")

class UserAccount:
    def __init__(self, id=None, username=None, password=None):
        self.id = id
        self.username = username
        self.password = password

    def loginAccount(self, username, password):
        cursor = db.cursor()
        query = "SELECT * FROM useraccounts WHERE username = %s AND password = %s"
        cursor.execute(query, (username, password))

        account = cursor.fetchone()
        
        if account:
            return UserAccount(*account)
        else:
            return None