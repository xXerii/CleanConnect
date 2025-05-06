import entity

class UserLoginController:
    def __init__(self):
        self.userAccount = entity.UserAccount()

    def loginAccount(self, username, password):
        return self.userAccount.loginAccount(username, password)
    
class ViewAccountsController:
    def __init__(self):
        self.userAccount = entity.UserAccount()

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

class SuspendAccountsController:
    def __init__(self):
        self.userAccount = entity.UserAccount()
    
    def setAccountSuspension(self, id: int, suspended: bool):
        return self.userAccount.setSuspended(id, suspended)
    
    
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
    
    
class AddServiceController:
    def __init__(self):
        self.cleanerService = entity.CleanerService()

    def addService(self, cleaner_id, category_id, service_id, price, description):
        return self.cleanerService.addService(cleaner_id, category_id, service_id, price, description)

class FetchCategoriesController:
    def __init__(self):
        self.category_service = entity.CategoryService()

    def fetchCategories(self):
        return self.category_service.getAllCategories()
    
class FetchServicesByCategoryController:
    def __init__(self):
        self.categoryService =entity.CategoryService()

    def fetchServicesByCategory(self, parentCat_id):
        return self.categoryService.getServicesByCategory(parentCat_id)

class FetchAllAvailableServicesController:
    def __init__(self):
        self.cleanerService = entity.CleanerService()
    
    def fetchAllAvailableService(self):
        # Fetch all services available
        return self.cleanerService.getAllAvailableService()

class SearchAllAvailableServicesByCategoryController:
    def __init__(self):
        self.cleanerService = entity.CleanerService()
    
    def fetchSearchServiceCategoryResult(self, search_query):
        # Fetch services based on selected category
        return self.cleanerService.searchServiceByCategory(search_query)

class FetchCleanerProfileController:
    def __init__(self):
        self.cleanerService = entity.CleanerService()
    
    def fetchCleanerProfileResult(self,cleaner_id):
        return self.cleanerService.getCleanerProfile(cleaner_id)

class FetchCleanerAllServicesController:
    def __init__(self):
        self.cleanerService = entity.CleanerService()

    def fetchCleanerAllService(self, user_id):
        # Fetch all services with the associated cleaner and category info
        return self.cleanerService.getCleanerServicesByUser(user_id)

class UpdateServiceController:
    def __init__(self):
        self.cleanerService = entity.CleanerService()

    def updateService(self, cleaner_id, service_id, new_price, new_description):
        return self.cleanerService.updateService(cleaner_id, service_id, new_price, new_description)

class DeleteServiceController:
    def __init__(self):
        self.cleanerService = entity.CleanerService()

    def deleteService(self, cleaner_id, service_id):
        return self.cleanerService.deleteService(cleaner_id, service_id)
    
class SearchServiceController:
    def __init__(self):
        self.cleanerService = entity.CleanerService()

    def searchService(self, search_query,cleaner_id):
        return self.cleanerService.searchCleanerServices(search_query, cleaner_id)

class JobHistoryController:
    def __init__(self):
        self.cleaner_service = entity.CleanerService()

    def fetchJobHistory(self, cleaner_id):
        """
        Fetch job history for a specific cleaner.
        """
        return self.cleaner_service.getJobHistoryByCleaner(cleaner_id)

class CleanerAnalyticsController:
    def __init__(self):
        self.model = entity.CleanerAnalytics()

    # façade methods used by the UI
    def logView(self, cleaner_id, viewer_id):
        self.model.log_view(cleaner_id, viewer_id)

    def toggleShortlist(self, cleaner_id, homeowner_id):
        self.model.toggle_shortlist(cleaner_id, homeowner_id)

    def getCounts(self, cleaner_id):
        return {
            "views":      self.model.view_count(cleaner_id),
            "shortlists": self.model.shortlist_count(cleaner_id),
        }

class BookedServicesController:
    def __init__(self):
        self.bookedServices = entity.BookedServices()

    def fetchBookedServices(self, user_id):
        """
        Fetch booked services for a specific user.
        """
        return self.bookedServices.getBookedServices(user_id)