import controller
import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox, filedialog

# Please use this dummy function as placeholder for the buttons if needed
def dummy():
    messagebox.showinfo("Clicked", "Feature coming soon.")

class LoginPage:
    def __init__(self, root):
        self.root = root
        self.displayLoginPage()

    def displayLoginPage(self):
        # Clear existing widgets if needed (optional)
        for widget in self.root.winfo_children():
            widget.destroy()

        # Set up the login UI
        Label(self.root, text="Login", font=("Arial", 24)).pack(pady=30)


        Label(self.root, text="Username").pack(pady=(10, 5))
        self.username_entry = Entry(self.root, width=30)
        self.username_entry.pack()

        Label(self.root, text="Password").pack(pady=(10, 5))
        self.password_entry = Entry(self.root, show="*", width=30)
        self.password_entry.pack()

        Button(self.root, text="Login", command=self.login).pack(pady=20)

    def login(self):

        # Create login controller instance
        self.controller = controller.UserLoginController()

        username = self.username_entry.get()
        password = self.password_entry.get()

        user = self.controller.loginAccount(username ,password)


        if user:
            print(f"Role ID: {user.role_id}")

            if user.role_id == 1:
                print ("Role: Admin")
                # Creates an instance of the admin page
                AdminPage(self.root,user)
            elif user.role_id == 2:
                print ("Role: Cleaner")
                # Creates an instance of the cleaner page
                CleanerPage(self.root,user)
            elif user.role_id == 3:
                print ("Role: Home Owner")
                # Creates an instance of the home owner page
                HomeOwnerPage(self.root,user)
            elif user.role_id == 4:
                print ("Role: Platform Manager")
                # Creates an instance of the platform manager page
                PlatformMngrPage(self.root,user)
            
            else:
                print("Role not found")
            
                
            print (f"User ID: {user.id}")
            messagebox.showinfo("Login Successful", f"Welcome {user.username}!")
        else:
            messagebox.showerror("Login Failed", "Invalid credentials.")

    def logout(self):
        messagebox.showinfo("Logged Out", "You have been logged out.")
        self.displayLoginPage()


# ADMIN PAGE
class AdminPage:
    def __init__(self, root, user):
        self.root = root
        self.user = user
        self.displayAdminPage()

    def displayAdminPage(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        Label(self.root, text=f"Admin Dashboard", font=("Arial", 24)).pack(pady=30)
        Label(self.root, text=f"Welcome, {self.user.username}").pack(pady=10)
        Label(self.root, text=f"Role ID: {self.user.role_id}").pack(pady=5)

        # Add Admin features here
        Button(self.root, text="View Reports", command=dummy).pack(pady=5)
        Button(self.root, text="Manage Users", command=self.openManageAccounts).pack(pady=5)

        Button(self.root, text="Logout", command=self.logout).pack(pady=20)

    # Opens the Accounts page
    def openManageAccounts(self):
        self.displayAccountsPage()
    
    def displayAccountsPage(self):
        self.controller = controller.ViewAccountsController()
        # Set up the accounts display UI
        for widget in self.root.winfo_children():
            widget.destroy()

        # Frame for the title
        title_frame = tk.Frame(self.root)
        title_frame.grid(row=0, column=0, columnspan=5, pady=30)  # Title section in grid (row 0)

        # Title Label inside the title frame
        tk.Label(title_frame, text="User Accounts", font=("Arial", 24)).grid(row=0, column=0, padx=200)

        # Search Frame
        search_frame = tk.Frame(self.root)
        search_frame.grid(row=1,column=0,columnspan=5, pady=10)

        search_var=tk.StringVar()

        tk.Label(search_frame, text="Search Username:").grid(row=0, column=0, padx=5)
        search_entry = tk.Entry(search_frame, textvariable=search_var, width=30)
        search_entry.grid(row=0, column=1, padx=5)

        def perform_search():
            keyword = search_var.get().lower()
            filtered = [acc for acc in self.controller.fetchAllAccounts() if keyword in acc.username.lower()]
            render_table(filtered)

        tk.Button(search_frame, text="Search", command=perform_search).grid(row=0, column=2, padx=5)
        tk.Button(search_frame, text="Reset", command=lambda: render_table(self.controller.fetchAllAccounts())).grid(row=0, column=3, padx=5)

        # Frame for table
        table_frame = tk.Frame(self.root)
        table_frame.grid(row=2, column=0, columnspan=5, pady=10)

        self.all_accounts = self.controller.fetchAllAccounts()

        def render_table(accounts):
            # Clear previous widgets in table frame
            for widget in table_frame.winfo_children():
                widget.destroy()

            headers = ["ID", "Username", "Role", "Actions"]
            for col, header in enumerate(headers):
                tk.Label(table_frame, text=header, font=("Arial", 12, "bold")).grid(row=0, column=col, padx=15, pady=5)

            for row, account in enumerate(accounts, start=1):
                tk.Label(table_frame, text=account.id).grid(row=row, column=0, padx=15, pady=5)
                tk.Label(table_frame, text=account.username).grid(row=row, column=1, padx=15, pady=5)
                tk.Label(table_frame, text=getattr(account, 'role', account.role_id)).grid(row=row, column=2, padx=15, pady=5)
                tk.Button(table_frame, text="Edit", command=lambda acc=account: self.edit_account(acc)).grid(row=row, column=3, padx=10)
                tk.Button(table_frame, text="Delete", command=lambda acc=account: self.delete_account(acc)).grid(row=row, column=4, padx=10)

        # Back and logout buttons inside the table frame (or you can place them in a separate frame as well)
            tk.Button(table_frame, text="Back to Dashboard", command=self.displayAdminPage).grid(row=row+1, column=0, padx=10, pady=10)
            tk.Button(table_frame, text="View Profiles", command=self.openManageProfiles).grid(row=row+1, column=1, padx=10, pady=10)
            tk.Button(table_frame, text="Add Account", command=dummy).grid(row=row+1, column=2, padx=10, pady=10) # THIS IS THE ADD ACCOUNT BUTTON (Funtion goes after command)

        render_table(self.all_accounts)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
    
    # Opens the Profile page
    def openManageProfiles(self):
        self.displayProfilesPage()

    def displayProfilesPage(self):
        self.controller = controller.ViewProfileController()
        # Set up the accounts display UI
        for widget in self.root.winfo_children():
            widget.destroy()

        # Frame for the title
        title_frame = tk.Frame(self.root)
        title_frame.grid(row=0, column=0, columnspan=5, pady=30)  # Title section in grid (row 0)

        # Title Label inside the title frame
        tk.Label(title_frame, text="User Profiles", font=("Arial", 24)).grid(row=0, column=0, padx=200)
        
        # Search Frame
        search_frame = tk.Frame(self.root)
        search_frame.grid(row=1,column=0,columnspan=5, pady=10)

        search_var=tk.StringVar()

        tk.Label(search_frame, text="Search Profile:").grid(row=0, column=0, padx=5)
        search_entry = tk.Entry(search_frame, textvariable=search_var, width=30)
        search_entry.grid(row=0, column=1, padx=5)

        def perform_search():
            keyword = search_var.get().lower()
            filtered = [prof for prof in self.controller.fetchAllProfiles() if keyword in prof.role.lower()]
            render_table(filtered)

        tk.Button(search_frame, text="Search", command=perform_search).grid(row=0, column=2, padx=5)
        tk.Button(search_frame, text="Reset", command=lambda: render_table(self.controller.fetchAllProfiles())).grid(row=0, column=3, padx=5)

        # Frame for table
        table_frame = tk.Frame(self.root)
        table_frame.grid(row=2, column=0, columnspan=5, pady=10)

        self.all_profiles = self.controller.fetchAllProfiles()

        def render_table(profiles):
            # Clear previous widgets in table frame
            for widget in table_frame.winfo_children():
                widget.destroy()

            headers = ["Role ID", "Role Name","Actions"]
            for col, header in enumerate(headers):
                tk.Label(table_frame, text=header, font=("Arial", 12, "bold")).grid(row=0, column=col, padx=15, pady=5)

            for row, account in enumerate(profiles, start=1):
                tk.Label(table_frame, text=account.role_id).grid(row=row, column=0, padx=15, pady=5)
                tk.Label(table_frame, text=account.role).grid(row=row, column=1, padx=15, pady=5)
                tk.Button(table_frame, text="Edit", command=dummy).grid(row=row, column=2, padx=10)
                tk.Button(table_frame, text="Delete", command=dummy).grid(row=row, column=3, padx=10)
    

            # Back and logout buttons inside the table frame (or you can place them in a separate frame as well)
            tk.Button(table_frame, text="Back to Dashboard ", command=self.displayAdminPage).grid(row=row+1, column=0, padx=10, pady=10)
            tk.Button(table_frame, text="View Accounts", command=self.openManageAccounts).grid(row=row+1, column=1, padx=10, pady=10)
            tk.Button(table_frame, text="Add Profile", command=dummy).grid(row=row+1, column=2, padx=10, pady=10) # THIS IS THE ADD Profile BUTTON (Funtion goes after command)

        render_table(self.all_profiles)

    # Creates an instance of LoginPage to utilise the
    # logout funtioned defined there
    def logout(self):
        logout = LoginPage(self.root)
        logout.logout()


# CLEANER PAGE
class CleanerPage:
    def __init__(self, root, user):
        self.root = root
        self.user = user
        self.displayCleanerPage()

    def displayCleanerPage(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        Label(self.root, text=f"Cleaner Dashboard", font=("Arial", 24)).pack(pady=30)
        Label(self.root, text=f"Welcome, {self.user.username}").pack(pady=10)
        Label(self.root, text=f"Role ID: {self.user.role_id}").pack(pady=5)

        # Add Admin features here
        Button(self.root, text="View Services", command=dummy).pack(pady=5)
        Button(self.root, text="View Interest Metrics", command=dummy).pack(pady=5)

        Button(self.root, text="Logout", command=self.logout).pack(pady=20)


    # Creates an instance of LoginPage to utilise the
    # logout funtioned defined there
    def logout(self):
        logout = LoginPage(self.root)
        logout.logout()


# HOME OWNER PAGE
class HomeOwnerPage:
    def __init__(self, root, user):
        self.root = root
        self.user = user
        self.displayHomeOwnerPage()

    def displayHomeOwnerPage(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        Label(self.root, text=f"Home Owner Dashboard", font=("Arial", 24)).pack(pady=30)
        Label(self.root, text=f"Welcome, {self.user.username}").pack(pady=10)
        Label(self.root, text=f"Role ID: {self.user.role_id}").pack(pady=5)

        # Add Admin features here
        Button(self.root, text="View Cleaners Available", command=dummy).pack(pady=5)

        Button(self.root, text="Logout", command=self.logout).pack(pady=20)

    def dummy(self):
        messagebox.showinfo("Clicked", "Feature coming soon.")

    # Creates an instance of LoginPage to utilise the
    # logout funtioned defined there
    def logout(self):
        logout = LoginPage(self.root)
        logout.logout()
        

# PLATFORM PAGE
class PlatformMngrPage:
    def __init__(self, root, user):
        self.root = root
        self.user = user
        self.PlatformMngrPage()

    def PlatformMngrPage(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        Label(self.root, text=f"Platform Manager Dashboard", font=("Arial", 24)).pack(pady=30)
        Label(self.root, text=f"Welcome, {self.user.username}").pack(pady=10)
        Label(self.root, text=f"Role ID: {self.user.role_id}").pack(pady=5)

        # Add Admin features here
        Button(self.root, text="View Cleaning Categories", command=dummy).pack(pady=5)
        Button(self.root, text="Generate Reports etc", command=dummy).pack(pady=5)

        Button(self.root, text="Logout", command=self.logout).pack(pady=20)

    def dummy(self):
        messagebox.showinfo("Clicked", "Feature coming soon.")

    # Creates an instance of LoginPage to utilise the
    # logout funtioned defined there
    def logout(self):
        logout = LoginPage(self.root)
        logout.logout()           


def page():
    window = Tk()
    window.geometry("1280x720")
    window.title('CleanConnect')
    window.minsize(960,540)
    LoginPage(window)
    window.mainloop()

if __name__ == '__main__':
    page()
