import entity
from datetime import date, timedelta

class UserLoginController:
    def __init__(self):
        self.userAccount = entity.UserAccount()

    def loginAccount(self, username, password):
        return self.userAccount.loginAccount(username, password)
    

    # THIS FUNCTION IS STRICTLY FOR LOGIN TDD
    """ 
    def checkCredentials(self, username, password):
        user = self.loginAccount(username, password)

        if not user:
            return {"status": "fail", "message": "Invalid credentials"}

        if user.suspended:
            return {"status": "suspended", "message": "Account suspended"}

        return {
            "status": "success",
            "user_id": user.user_id,
            "username": user.username,
            "role_id": user.role_id
        } """
    
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

class ViewAllAvailableServicesController:
    def __init__(self):
        self.cleanerService = entity.CleanerService()
    
    def getAllAvailableService(self):
        # Fetch all services available
        return self.cleanerService.getAllAvailableService()

class SearchAllAvailableServicesController:
    def __init__(self):
        self.cleanerService = entity.CleanerService()
    
    def searchAllServices(self, search_query):
        # Fetch services based on selected category
        return self.cleanerService.searchAllServices(search_query)
    
class SearchShortlistedServicesController:
    def __init__(self):
        self.cleanerService = entity.CleanerService()

    def fetchShortlistedServiceCategoryResult(self, user_id, search_query):
        # Call the model method to get the shortlisted services by category
        return self.cleanerService.searchShortlistedServicesByCategory(user_id, search_query)

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
    
class FetchCleanerByCatController:
    def __init__(self):
        self.categoryService = entity.CategoryService()

    def fetchCleanerByCat(self,category_id):
        return self.categoryService.fetchCleanersByCategory(category_id)

class ViewShortlistedServicesController:
    def __init__(self):
        self.model = entity.CleanerService()

    def getShortlistedServices(self, homeowner_id):
        return self.model.getShortlistedServices(homeowner_id)

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

class CleanerProfViewsController:
    def __init__(self):
        self.model = entity.CleanerAnalytics()

    def logView(self, cleaner_id, viewer_id):
        self.model.log_view(cleaner_id, viewer_id)

    def getViewCount(self, cleaner_id):
        return self.model.view_count(cleaner_id)

class CleanerShortlistsViewsController:
    def __init__(self):
        self.model = entity.CleanerAnalytics()

    def getShortlistCount(self, cleaner_id):
        return self.model.shortlist_count(cleaner_id)

class AddShortlistController:
    def __init__(self):
        self.cleanerService = entity.CleanerService()

    def addShortlist(self, cleaner_id, homeowner_id, category_id, service_id, clean_svc_id):
        return self.cleanerService.addShortlist(cleaner_id, homeowner_id, category_id, service_id, clean_svc_id)    

class RemoveShortlistController:
    def __init__(self):
        self.cleanerService = entity.CleanerService()

    def removeShortlist(self, cleaner_id, homeowner_id, category_id, service_id):
        return self.cleanerService.removeShortlist(cleaner_id, homeowner_id, category_id, service_id)
    
class AddCategoryController:
    def __init__(self):
        self.categoryService = entity.CategoryService()

    def addCategory(self, cat_sv_name, cat_desc):
        return self.categoryService.addCategory(cat_sv_name, cat_desc)

class AddPlatformServiceController:
    def __init__(self):
        self.categoryService = entity.CategoryService()

    def addService(self, cat_sv_name, parentCat_id):
        return self.categoryService.addNewService(cat_sv_name, parentCat_id)

class DeleteCategoryController:
    def __init__(self):
        self.categoryService = entity.CategoryService()

    def deleteCategory(self, catsv_id):
        return self.categoryService.deleteCategory(catsv_id)

class UpdateCategoryController:
    def __init__(self):
        self.categoryService = entity.CategoryService()

    def updateCategoryDesc(self, catsv_id, new_desc):
        return self.categoryService.updateCategoryDesc(catsv_id, new_desc)

class SearchCategoryController:
    def __init__(self):
        self.categoryService = entity.CategoryService()

    def searchCategories(self, search_query):
        return self.categoryService.searchCategories(search_query)
    
# User Admins Controllers
class CreateProfileController:
    def __init__(self):
        self.userProfile = entity.UserProfile()
    
    def createProfile(self, role):
        # Create a new user account
        return self.userProfile.createProfile(role)
    
class SuspendAccountsController:
    def __init__(self):
        self.userAccount = entity.UserAccount()
    
    def setAccountSuspension(self, id: int, suspended: bool):
        return self.userAccount.setAccountSuspension(id, suspended)

class SuspendProfileController:
    def __init__(self):
        self.userProfile = entity.UserProfile()
    
    def setProfileSuspension(self, id: int, suspended: bool):
        return self.userProfile.setProfileSuspension(id, suspended)

class BookedServicesController:
    def __init__(self):
        self.bookedServices = entity.CleanerService()

    def fetchBookedServices(self, user_id):
        """
        Fetch booked services for a specific user.
        """
        return self.bookedServices.getPastBookingsByHomeOwner(user_id)    

# Cleaners Controllers

# Home owner Controllers

# Platform Manager Controllers
class BookingReportController:
    def __init__(self):
        self.model = entity.BookingReports()

    def getBookingsByCategory(self, date_from, date_to):
        return self.model.by_category(date_from, date_to)

    def getCleanersBooked(self, date_from, date_to):
        return self.model.cleaners_booked(date_from, date_to)
    
    def getBookingsByCleaner(self, date_from, date_to):
        return self.model.getBookingsByCleaner(date_from, date_to)

class DailyReportController:
    def __init__(self):
        self.rep   = BookingReportController()
        self.today = date.today()

    def category_report(self, start=None, end=None):
        if start and end:
            return self.rep.getBookingsByCategory(start, end)
        return self.rep.getBookingsByCategory(self.today, self.today)

    def cleaner_report(self, start=None, end=None):
        if start and end:
            return self.rep.getBookingsByCleaner(start, end)
        return self.rep.getBookingsByCleaner(self.today, self.today)

    def distinct_cleaners(self, start=None, end=None):
        if start and end:
            return self.rep.getCleanersBooked(start, end)
        return self.rep.getCleanersBooked(self.today, self.today)

class WeeklyReportController:
    def __init__(self):
        self.rep  = BookingReportController()
        self.to   = date.today()
        self.frm  = self.to - timedelta(days=6)

    def category_report(self, start=None, end=None):
        return self.rep.getBookingsByCategory(
            start or self.frm,
            end   or self.to
        )

    def cleaner_report(self, start=None, end=None):
        return self.rep.getBookingsByCleaner(
            start or self.frm,
            end   or self.to
        )

    def distinct_cleaners(self, start=None, end=None):
        return self.rep.getCleanersBooked(
            start or self.frm,
            end   or self.to
        )

class MonthlyReportController:
    def __init__(self):
        self.rep  = BookingReportController()
        self.to   = date.today()
        self.frm  = self.to - timedelta(days=29)

    def category_report(self, start=None, end=None):
        return self.rep.getBookingsByCategory(
            start or self.frm,
            end   or self.to
        )

    def cleaner_report(self, start=None, end=None):
        return self.rep.getBookingsByCleaner(
            start or self.frm,
            end   or self.to
        )

    def distinct_cleaners(self, start=None, end=None):
        return self.rep.getCleanersBooked(
            start or self.frm,
            end   or self.to
        )