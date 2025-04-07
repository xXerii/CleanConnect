
    def loginAccount(self, username, password):
        cursor = db.cursor()
        query = "SELECT * FROM useraccounts WHERE username = %s AND password = %s"
        cursor.execute(query, (username, password))
