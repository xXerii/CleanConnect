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
    
class UpdateAccountsController:
    def __init__(self):
        self.userAccount = entity.UserAccount()

    def updateAccount(self, id, new_username, new_password, new_role_id):
        return self.userAccount.updateAccount(id,new_username, new_password, new_role_id)
    
class ViewProfileController:
    def __init__(self):
        self.userProfile = entity.UserProfile()

    def fetchAllProfiles(self):
        return self.userProfile.fetchAllProfiles() 