import entity
from entity import UserAccount

class UserLoginController:
    def __init__(self):
        self.userAccount = entity.UserAccount()

    def loginAccount(self, username, password):
        return self.userAccount.loginAccount(username, password)
    
class ViewAccountsController:
    def __init__(self):
        self.userAccount = UserAccount()

    def viewAccounts(self):
        return self.userAccount.viewAccounts()

class SearchAccountsController:
    def __init__(self):
        self.userAccount = entity.UserAccount()

    def searchAccounts(self, username):
        return self.userAccount.searchAccounts(username)
    
    
class UpdateAccountsController:
    def __init__(self):
        self.userAccount = entity.UserAccount()

    def updateAccount(self, user_id, new_name, new_username, new_email, new_password, new_role_id):
        return self.userAccount.updateAccount(user_id, new_name, new_username, new_email, new_password, new_role_id)
    
class CreateAccountsController:
    def __init__(self):
        self.userAccount = entity.UserAccount()
    
    def createAccount(self, name, username, password ,email, role_id):
        # Create a new user account
        return self.userAccount.createAccount(name, username, password ,email, role_id)
    
class ViewProfileController:
    def __init__(self):
        self.userProfile = entity.UserProfile()

    def viewProfiles(self):
        return self.userProfile.viewProfiles()

class SearchProfilesController:
    def __init__(self):
        self.userProfile = entity.UserProfile()

    def searchProfiles(self, role):
        return self.userProfile.searchProfiles(role)

class UpdateProfileController:
    def __init__(self):
        self.userProfile = entity.UserProfile()

    def updateProfile(self,role_id, new_role):
        return self.userProfile.updateProfile(role_id, new_role) 
