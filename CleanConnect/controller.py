import entity

class UserLoginController:
    def __init__(self):
        self.userAccount = entity.UserAccount()

    def loginAccount(self, username, password):
        return self.userAccount.loginAccount(username, password)
    
class ViewAccountsController:
    def __init__(self):
        self.userAccount = entity.UserAccount()

    def fetchAllAccounts(self):
        return self.userAccount.fetchAllAccounts()
    
class ViewProfileController:
    def __init__(self):
        self.userProfile = entity.UserProfile()

    def fetchAllProfiles(self):
        return self.userProfile.fetchAllProfiles() 