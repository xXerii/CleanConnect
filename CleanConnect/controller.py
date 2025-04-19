import entity
from entity import UserAccount

class UserLoginController:
    def __init__(self):
        self.userAccount = entity.UserAccount()

    def loginAccount(self, username, password):
        return self.userAccount.loginAccount(username, password)
    
class ViewAccountsController:
    def __init__(self):
        self.user_account = UserAccount()

    def fetchAllAccounts(self):
        # Fetch all accounts from the database
        return self.user_account.fetchAllAccounts()

    def createAccount(self, username, password, role_id, suspended):
        # Create a new user account
        return self.user_account.createAccount(username, password, role_id, suspended)
    
class ViewProfileController:
    def __init__(self):
        self.userProfile = entity.UserProfile()

    def fetchAllProfiles(self):
        return self.userProfile.fetchAllProfiles()