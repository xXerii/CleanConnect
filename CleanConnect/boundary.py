import controller
import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox
import datetime
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import calendar

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

        if not user:
            messagebox.showerror("Login Failed", "Invalid credentials.")
            pass  # Placeholder to avoid syntax errors

        if user.suspended:
            messagebox.showerror("Account Suspended",
                                "Your account has been suspended.\n"
                                "Please contact an administrator.")
            return
        
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
            
                
            print (f"User ID: {user.user_id}")
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

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    # User Accounts functions
    # Opens the Accounts page
    def openManageAccounts(self):
        self.displayAccountsPage()
    
    def displayAccountsPage(self):
        # Create ViewAccounts controller instance
        self.controller = controller.ViewAccountsController()
        self.searchController = controller.SearchAccountsController()

        # Set up the accounts display UI
        for widget in self.root.winfo_children():
            widget.destroy()
        
        # Set background color
        self.root.configure(bg="#f0f2f5")

        # Title Frame
        title_frame = tk.Frame(self.root, bg="#f0f2f5")
        title_frame.grid(row=0, column=0, columnspan=5, pady=30)  # Title section in grid (row 0)

        # Title Label inside the title frame
        tk.Label(title_frame, text="User Accounts", font=("Arial", 24, "bold"), bg="#f0f2f5", fg="#333").grid(row=0, column=0, padx=200)

        # Search Frame
        search_frame = tk.Frame(self.root)
        search_frame.grid(row=1,column=0,columnspan=5, pady=10)

        search_var=tk.StringVar()

        tk.Label(search_frame, text="Search Username:").grid(row=0, column=0, padx=5)
        self.search_entry = tk.Entry(search_frame, textvariable=search_var, width=30)
        self.search_entry.grid(row=0, column=1, padx=5)

        def perform_search():
            query = self.search_entry.get().strip()
            if query:
                filtered_accounts = self.searchController.searchAccounts(query)
                if not filtered_accounts:
                    messagebox.showerror("No Results", f"No accounts found for '{query}'.")
            else:
                render_table(filtered_accounts)

        tk.Button(search_frame, text="Search", command=perform_search).grid(row=0, column=2, padx=5)
        tk.Button(search_frame, text="Reset", command=lambda: render_table(self.controller.viewAccounts())).grid(row=0, column=3, padx=5)

        # Table Frame
        table_frame = tk.Frame(self.root, bg="#add8e6")
        table_frame.grid(row=2, column=0, columnspan=4, padx=30, pady=10, sticky="nsew")

        # Fetch all accounts ONCE and store them
        self.all_accounts = self.controller.viewAccounts()

        def render_table(accounts):
            # Clear previous widgets in table frame
            for widget in table_frame.winfo_children():
                widget.destroy()

            headers = ["User ID", "Username", "Role","Status", "Actions"]
            header_font = ("Arial", 12, "bold")
            for col, header in enumerate(headers):
                tk.Label(table_frame, text=header, font=header_font, bg="#e6e6e6", fg="#222", padx=15, pady=5).grid(row=0, column=col, sticky="nsew")

            row_count = 1  # Track the number of rows

            for account in accounts:
                tk.Label(table_frame, text=account.user_id, font=("Arial", 12), bg="#add8e6", padx=15, pady=5).grid(row=row_count, column=0, sticky="nsew")
                tk.Label(table_frame, text=account.username, font=("Arial", 12), bg="#add8e6", padx=15, pady=5).grid(row=row_count, column=1, sticky="nsew")
                tk.Label(table_frame, text=getattr(account, 'role', account.role_id), font=("Arial", 12), bg="#add8e6", padx=15, pady=5).grid(row=row_count, column=2, sticky="nsew")

                status = "Suspended" if account.suspended else "Active"
                tk.Label(table_frame, text=status, font=("Arial", 12), bg="#add8e6", padx=15, pady=5).grid(row=row_count, column=3, sticky="nsew")

                # Action buttons in one frame
                action_frame = tk.Frame(table_frame, bg="#add8e6")
                action_frame.grid(row=row_count, column=4, padx=10, pady=5)

                edit_btn = tk.Button(action_frame, text="Edit", command=lambda acc=account: self.displayAccountUpdateForm(acc), font=("Arial", 12, "bold"), width=8, borderwidth=0, cursor="hand2")
                edit_btn.pack(side="left", padx=10)

                suspend_button_text = "Suspend" if not account.suspended else "Reactivate"
                suspend_btn = tk.Button(action_frame, text=suspend_button_text,  command=lambda acc=account: self.suspendUserAccount(acc.user_id, acc.suspended), fg="black", font=("Arial", 12, "bold"), width=8,  borderwidth=0, cursor="hand2")
                suspend_btn.pack(side="left", padx=10)

                row_count += 1  # Increment the row count after each account

        render_table(self.all_accounts)

        # Action Buttons
        self.button_frame = tk.Frame(self.root, bg="#f0f0f0")
        self.button_frame.grid(row=3, column=0, columnspan=5, pady=10)
                
        style_btn = lambda text, cmd, color: tk.Button(self.button_frame, text=text, command=cmd, bg=color, fg="black", font=("Arial", 12, "bold"), padx=20, pady=5)

        # Back and logout buttons inside the table frame (or you can place them in a separate frame as well)
        style_btn("Back to Dashboard", self.displayAdminPage, "#607d8b").grid(row=0, column=0, padx=10)
        style_btn("View Profiles", self.openManageProfiles, "#3f51b5").grid(row=0, column=1, padx=10)
        style_btn("Add Account", self.displayCreateAccountForm, "#009688").grid(row=0, column=2, padx=10)  

    def suspendUserAccount(self, user_id, currently_suspended):
        self.suspendController = controller.SuspendAccountsController()
        # Create popup window
        popup = tk.Toplevel()
        popup.title("Suspend Account")
        popup.geometry("400x200")
        popup.configure(bg="white")
        popup.resizable(False, False)

        # Border frame
        border = tk.Frame(popup, bg="#add8e6", padx=1, pady=1)
        border.pack(expand=True, fill="both", padx=30, pady=30)

        # Inner frame
        inner = tk.Frame(border, bg="#add8e6")
        inner.pack(expand=True, fill="both", padx=20, pady=20)

        # Dynamically update the button text based on current suspension status
        suspend_button_text = "Suspend" if not currently_suspended else "Reactivate"

        # Message
        tk.Label(inner, text=f"Are you sure you want to {suspend_button_text} this user?", font=("Arial", 12, "bold"), bg="#add8e6",wraplength=300,justify="center").pack(pady=(5, 20))

        
        # Center the window on screen
        popup.update_idletasks()
        width = popup.winfo_width()
        height = popup.winfo_height()
        x = (popup.winfo_screenwidth() // 2) - (width // 2)
        y = (popup.winfo_screenheight() // 2) - (height // 2)
        popup.geometry(f"+{x}+{y}")

        # Buttons
        button_frame = tk.Frame(inner, bg="#add8e6")
        button_frame.pack()

        # Cancel button with styling
        cancel_btn = tk.Button(button_frame, text="Cancel", width=10, command=popup.destroy, highlightbackground="#add8e6", activebackground="#8fc5d8", relief="flat")
        cancel_btn.pack(side="left", padx=10)

        def handle_suspend():
            self.toggleSuspension(user_id, currently_suspended)
            popup.destroy()

        # Suspend button with styling
        suspend_btn = tk.Button(button_frame, text=suspend_button_text, width=10, command=handle_suspend, highlightbackground="#add8e6", activebackground="#8fc5d8", relief="flat")
        suspend_btn.pack(side="left", padx=10)

    def toggleSuspension(self, user_id, currently_suspended):
        # Flip the flag
        success = self.suspendController.setAccountSuspension(user_id, not bool(currently_suspended))

        if success:
            # Feedback
            state = "suspended" if not currently_suspended else "reactivated"
            messagebox.showinfo("Success", f"Account {user_id} {state}.")
            # Refresh the table so status & button update
            self.displayAccountsPage()
        else:
            messagebox.showerror("Error", f"Failed to update suspension status for account {user_id}.")

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
    
    def displayCreateAccountForm(self):
        self.createController = controller.CreateAccountsController()
        self.profileController = controller.ViewProfileController()
        for widget in self.root.winfo_children():
            widget.destroy()

        Label(self.root, text="Create New Account", font=("Arial", 24)).pack(pady=20)

        form_frame = Frame(self.root)
        form_frame.pack(pady=10)

        # Input fields
        Label(form_frame, text="Name").grid(row=0, column=0, sticky='e', padx=5, pady=5)
        name_entry = Entry(form_frame)
        name_entry.grid(row=0, column=1, padx=5, pady=5)

        Label(form_frame, text="Username").grid(row=1, column=0, sticky='e', padx=5, pady=5)
        username_entry = Entry(form_frame)
        username_entry.grid(row=1, column=1, padx=5, pady=5)

        Label(form_frame, text="Password").grid(row=2, column=0, sticky='e', padx=5, pady=5)
        password_entry = Entry(form_frame, show="*")
        password_entry.grid(row=2, column=1, padx=5, pady=5)

        Label(form_frame, text="Confirm Password").grid(row=3, column=0, sticky='e', padx=5, pady=5)
        confirm_password_entry = Entry(form_frame, show="*")
        confirm_password_entry.grid(row=3, column=1, padx=5, pady=5)

        Label(form_frame, text="Email").grid(row=4, column=0, sticky='e', padx=5, pady=5)
        email_entry = Entry(form_frame)
        email_entry.grid(row=4, column=1, padx=5, pady=5)

        tk.Label(form_frame, text="Select New Role:").grid(row=5, column=0, sticky='e', padx=5, pady=5)

        # Fetch roles from controller
        profiles = self.profileController.viewProfiles()
        roleOptions = [profile.role for profile in profiles]
        self.roleMap = {profile.role: profile.role_id for profile in profiles}

        self.selectedRole = tk.StringVar()
        
        #Dropdown menu()
        roleDropdown = tk.OptionMenu(self.root, self.selectedRole, *roleOptions)
        roleDropdown.pack(pady=5)

        # Submit button
        def submit():
            name     = name_entry.get().strip()
            username = username_entry.get().strip()
            password = password_entry.get().strip()
            confirm  = confirm_password_entry.get().strip()
            email    = email_entry.get().strip()
            selected_role_name = self.selectedRole.get()
            role_id  = self.roleMap.get(selected_role_name)
            
            if not all([name, username, password, email, role_id]): 
                messagebox.showerror("Error", "Please fill in all fields")

            if password != confirm:
                messagebox.showerror("Error", "Passwords do not match.")
                return 

            success, = self.createController.createAccount(
                name, username, password, email, role_id
            ) 

            if not success:
                messagebox.showerror("Database Error", "Please check backend." )
                return
            
            messagebox.showinfo("Success", f"Account for {username} created successfully!")

        Button(self.root, text="Submit", command=submit).pack(pady=10)
        Button(self.root, text="Back", command=self.displayAccountsPage).pack(pady=5)

        
    def displayAccountUpdateForm(self, account):
        self.controller = controller.UpdateAccountsController()
        self.profileController = controller.ViewProfileController()
        # Clear existing widgets
        for widget in self.root.winfo_children():
            widget.destroy()

        Label(self.root, text="Update Account", font=("Arial", 24)).pack(pady=20)

        form_frame = Frame(self.root)
        form_frame.pack(pady=10)

        # Fields to update the username, password, and role
        tk.Label(form_frame, text="Name:").grid(row=0, column=0, sticky='e', padx=5, pady=5)
        self.new_name_entry = tk.Entry(form_frame, font=("Arial", 12))
        self.new_name_entry.insert(0, account.name)  # Pre-fill with the current username
        self.new_name_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(form_frame, text="Username:").grid(row=1, column=0, sticky='e', padx=5, pady=5)
        self.new_username_entry = tk.Entry(form_frame, font=("Arial", 12))
        self.new_username_entry.insert(0, account.username)  # Pre-fill with the current username
        self.new_username_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(form_frame, text="New Password:").grid(row=2, column=0, sticky='e', padx=5, pady=5)
        self.new_password_entry = tk.Entry(form_frame, font=("Arial", 12), show="*")
        self.new_password_entry.insert(0, account.password)  # Pre-fill with the current password
        self.new_password_entry.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(form_frame, text="Confirm Password:").grid(row=3, column=0, sticky='e', padx=5, pady=5)
        self.new_confirmpw_entry = tk.Entry(form_frame, font=("Arial", 12), show="*")
        self.new_confirmpw_entry.grid(row=3, column=1, padx=5, pady=5)

        tk.Label(form_frame, text="Email:").grid(row=4, column=0, sticky='e', padx=5, pady=5)
        self.new_email_entry = tk.Entry(form_frame, font=("Arial", 12))
        self.new_email_entry.insert(0, account.email)
        self.new_email_entry.grid(row=4, column=1, padx=5, pady=5)

        tk.Label(form_frame, text="Select New Role:").grid(row=5, column=0, sticky='e', padx=5, pady=5)

        # Fetch roles from controller
        profiles = self.profileController.viewProfiles()
        roleOptions = [profile.role for profile in profiles]
        self.roleMap = {profile.role: profile.role_id for profile in profiles}

        currentRoleName = next((profile.role for profile in profiles if profile.role_id == account.role_id), None)
        self.selectedRole = tk.StringVar()
        self.selectedRole.set(currentRoleName)
        
        #Dropdown menu()
        roleDropdown = tk.OptionMenu(self.root, self.selectedRole, *roleOptions)
        roleDropdown.pack(pady=5)

        # Buttons to submit or cancel the update
        submit_button = tk.Button(self.root, text="Update", command=lambda: self.submitAccUpdate(account.user_id))
        submit_button.pack(pady=10)

        cancel_button = tk.Button(self.root, text="Cancel", command=self.displayAccountsPage)
        cancel_button.pack(pady=10)

    def submitAccUpdate(self, user_id):
        # Get the values entered in the fields
        new_name = self.new_name_entry.get()
        new_username = self.new_username_entry.get()
        new_email =  self.new_email_entry.get()
        new_password = self.new_password_entry.get()
        confirmpw =  self.new_confirmpw_entry.get()
        selected_role_name = self.selectedRole.get()
        new_role_id = self.roleMap[selected_role_name]

        if not all([new_name, new_username, new_email, new_password, confirmpw, selected_role_name]):
            messagebox.showerror("Error", "All fields must be filled out.")
            return
        
        if new_password != confirmpw:
            messagebox.showerror("Error", "Passwords do not match.")
            return
        
        success = self.controller.updateAccount(user_id, new_name, new_username, new_email, new_password, new_role_id)

        if not success:
            messagebox.showerror("Error", "Failed to update account. Please try again.")
            return
     
        messagebox.showinfo("Success", "Account updated.")
        return

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    # User Profile functions
    # Opens the Profile page
    def openManageProfiles(self):
        self.displayProfilesPage()

    def displayProfilesPage(self):
        # Create ViewProfiles controller instance
        self.searchController = controller.SearchProfilesController()

        # Set up the accounts display UI
        for widget in self.root.winfo_children():
            widget.destroy()

         # Set background color
        self.root.configure(bg="#f0f2f5")

        # Title Frame
        title_frame = tk.Frame(self.root, bg="#f0f2f5")
        title_frame.grid(row=0, column=0, columnspan=5, pady=30)  # Title section in grid (row 0)

        # Title Label inside the title frame
        tk.Label(title_frame, text="User Profiles", font=("Arial", 24, "bold"), bg="#f0f2f5", fg="#333").grid(row=0, column=0, padx=200)
        
        # Search Frame
        search_frame = tk.Frame(self.root)
        search_frame.grid(row=1,column=0,columnspan=5, pady=10)

        search_var=tk.StringVar()

        tk.Label(search_frame, text="Search Profile:").grid(row=0, column=0, padx=5)
        self.search_entry = tk.Entry(search_frame, textvariable=search_var, width=30)
        self.search_entry.grid(row=0, column=1, padx=5)

        def perform_search():
            query = self.search_entry.get().strip()
            if query:
                filtered_profiles = self.searchController.searchProfiles(query)
                if not filtered_profiles:
                    messagebox.showerror("No Results", f"No profiles found for '{query}'.")
                else:
                    render_table(filtered_profiles)

        tk.Button(search_frame, text="Search", command=perform_search).grid(row=0, column=2, padx=5)
        tk.Button(search_frame, text="Reset", command=lambda: render_table()).grid(row=0, column=3, padx=5)

         # Table Frame
        table_frame = tk.Frame(self.root, bg="#add8e6")
        table_frame.grid(row=2, column=0, columnspan=4, padx=30, pady=10, sticky="nsew")


        def render_table(profiles=None):
            self.controller = controller.ViewProfileController()
            self.all_profiles = self.controller.viewProfiles()
            if profiles is None:
                profiles = self.controller.viewProfiles()
            self.all_profiles = profiles

            # Clear previous widgets in table frame
            for widget in table_frame.winfo_children():
                widget.destroy()

            headers = ["Role ID", "Role Name","Status", "Actions"]
            header_font = ("Arial", 12, "bold")
            for col, header in enumerate(headers):
                tk.Label(table_frame, text=header, font=header_font, bg="#e6e6e6", fg="#222", padx=15, pady=5).grid(row=0, column=col, sticky="nsew")

            row_count = 1  # Track the number of rows

            for profile in profiles:
                tk.Label(table_frame, text=profile.role_id, font=("Arial", 12), bg="#add8e6", padx=15, pady=5).grid(row=row_count, column=0, sticky="nsew")
                tk.Label(table_frame, text=profile.role, font=("Arial", 12), bg="#add8e6", padx=15, pady=5).grid(row=row_count, column=1, sticky="nsew")

                status = "Suspended" if profile.suspended else "Active"
                tk.Label(table_frame, text=status, font=("Arial", 12), bg="#add8e6", padx=15, pady=5).grid(row=row_count, column=2, sticky="nsew")

                # Action buttons in one frame
                action_frame = tk.Frame(table_frame, bg="#add8e6")
                action_frame.grid(row=row_count, column=3, padx=23, pady=5)

                edit_btn = tk.Button(action_frame, text="Edit", command=lambda prof=profile: self.displayProfileUpdateForm(prof), font=("Arial", 12, "bold"), width=8, borderwidth=0, cursor="hand2",)
                edit_btn.pack(side="left", padx=10)

                suspend_button_text = "Suspend" if not profile.suspended else "Reactivate"
                suspend_btn = tk.Button(action_frame, text=suspend_button_text,  command=lambda prof=profile: self.suspendProfile(prof, not prof.suspended), fg="black", font=("Arial", 12, "bold"), width=8,  borderwidth=0, cursor="hand2")
                suspend_btn.pack(side="left", padx=10)

                row_count += 1  # Increment the row count after each account

        render_table()

        # Action Buttons
        self.button_frame = tk.Frame(self.root, bg="#f0f0f0")
        self.button_frame.grid(row=3, column=0, columnspan=5, pady=10)
                
        style_btn = lambda text, cmd, color: tk.Button(self.button_frame, text=text, command=cmd, bg=color, fg="black", font=("Arial", 12, "bold"), padx=20, pady=5)

        # Back and logout buttons inside the table frame (or you can place them in a separate frame as well)
        style_btn("Back to Dashboard", self.displayAdminPage, "#607d8b").grid(row=0, column=0, padx=10)
        style_btn("View Accounts", self.openManageAccounts, "#3f51b5").grid(row=0, column=1, padx=10)
        style_btn("Add Profile", self.displayAddProfileForm, "#009688").grid(row=0, column=2, padx=10)

    def displayAddProfileForm(self):
        self.addProfcontroller = controller.CreateProfileController()
        # Clear existing widgets
        for widget in self.root.winfo_children():
            widget.destroy()

        # Title for the update page
        tk.Label(self.root, text="Add Profile", font=("Arial", 24)).pack(pady=20)

        # Fields to update the username, password, and role
        tk.Label(self.root, text="Role Name:").pack(pady=5)
        self.roleEntry = tk.Entry(self.root, font=("Arial", 12))
        self.roleEntry.pack(pady=5)

        # Buttons to submit or cancel the update
        submit_button = tk.Button(self.root, text="Add",  command=self.addProfile)
        submit_button.pack(pady=10)

        cancel_button = tk.Button(self.root, text="Cancel", command=self.displayProfilesPage)
        cancel_button.pack(pady=10)

    def addProfile(self):
        # Get the values entered in the fields
        roleName = self.roleEntry.get()

        if not roleName:
            messagebox.showerror("Error", "All fields must be filled out.")
            return
        
        success = self.addProfcontroller.createProfile(roleName)

        if not success:
            messagebox.showerror("Error", "Failed to add profile. Please try again.")
            return
    
        messagebox.showinfo("Success", "Profile added")
        self.displayProfilesPage()
        return
    
    def suspendProfile(self, profile, activate: bool):
        self.susController = controller.SuspendProfileController()
        """
        Pops up a Yes/No dialog to suspend or reactivate,
        then calls the controller and refreshes the table.
        """
        verb = "suspend" if not profile.suspended else "reactivate"
        msg = f"Are you sure you want to {verb} role #{profile.role_id} ({profile.role})?"
        if not messagebox.askyesno("Please confirm", msg):
            return

        success = self.susController.setProfileSuspension(profile.role_id, activate)
        if success:
            messagebox.showinfo("Success", f"Role has been {verb}d.")
        else:
            messagebox.showerror("Error", f"Failed to {verb} role.")
        # Refresh your listing
        self.displayProfilesPage()


    def displayProfileUpdateForm(self, profile):
        self.controller = controller.UpdateProfileController()
        # Clear existing widgets
        for widget in self.root.winfo_children():
            widget.destroy()

        # Title for the update page
        tk.Label(self.root, text="Update Profile", font=("Arial", 24)).pack(pady=20)

        # Fields to update the username, password, and role
        tk.Label(self.root, text="New Role Name:").pack(pady=5)
        self.new_role_entry = tk.Entry(self.root, font=("Arial", 12))
        self.new_role_entry.insert(0, profile.role)  # Pre-fill with the current username
        self.new_role_entry.pack(pady=5)

        # Buttons to submit or cancel the update
        submit_button = tk.Button(self.root, text="Update", command=lambda: self.submitProfUpdate(profile.role_id))
        submit_button.pack(pady=10)

        cancel_button = tk.Button(self.root, text="Cancel", command=self.displayProfilesPage)
        cancel_button.pack(pady=10)

    def submitProfUpdate(self, role_id):
        # Get the values entered in the fields
        new_role = self.new_role_entry.get()

        if not new_role:
            messagebox.showerror("Error", "All fields must be filled out.")
            return
        
        success = self.controller.updateProfile(role_id, new_role)

        if not success:
            messagebox.showerror("Error", "Failed to update profile. Please try again.")
            return
        
        messagebox.showinfo("Success", "Profile updated")

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
        # Create controller instance
        self.addServiceController = controller.AddServiceController()
        self.fetchCategoriesController = controller.FetchCategoriesController()
        self.fetchServicesByCategoryController = controller.FetchServicesByCategoryController()
        for widget in self.root.winfo_children():
            widget.destroy()
        

        Label(self.root, text=f"Cleaner Dashboard", font=("Arial", 24)).pack(pady=30)
        Label(self.root, text=f"Welcome, {self.user.username}").pack(pady=10)
        Label(self.root, text=f"Role ID: {self.user.role_id}").pack(pady=5)
        # live metrics
        profCounts = controller.CleanerProfViewsController().getViewCount(self.user.user_id)
        shortlistCounts = controller.CleanerShortlistsViewsController().getShortlistCount(self.user.user_id)
        tk.Label(self.root, text=f"Profile views:{profCounts}").pack()
        tk.Label(self.root, text=f"Times shortlisted: {shortlistCounts}").pack(pady=(0,10))

        
        Button(self.root, text="View Services", command=self.displayMyServicesPage).pack(pady=5)
        Button(self.root, text="Add Services", command=self.openCreateServiceForm).pack(pady=5)
        Button(self.root, text="View Job History", command=self.viewJobHistory).pack(pady=5)
        Button(self.root, text="Logout", command=self.logout).pack(pady=20)
    
    def displayMyServicesPage(self):
        # Create controller instance
        self.fetchServiceController = controller.FetchCleanerAllServicesController()
        self.searchSeriveController = controller.SearchServiceController()
        for widget in self.root.winfo_children():
            widget.destroy()

        # Configure background
        self.root.configure(bg="#f0f2f5")

        # Title Frame
        title_frame = tk.Frame(self.root, bg="#f0f2f5")
        title_frame.grid(row=0, column=0, columnspan=5, pady=30)
        tk.Label(
            title_frame,
            text="My Services",
            font=("Arial", 24, "bold"),
            bg="#f0f2f5",
            fg="#333"
        ).grid(row=0, column=0, padx=200)

        # Search Frame
        search_frame = tk.Frame(self.root, bg="#f0f2f5")
        search_frame.grid(row=1, column=0, columnspan=5, pady=10)
        search_var = tk.StringVar()
        tk.Label(search_frame, text="Search Service:", bg="#f0f2f5").grid(row=0, column=0, padx=5)
        self.search_entry = tk.Entry(search_frame, textvariable=search_var, width=30)
        self.search_entry.grid(row=0, column=1, padx=5)

        def perform_search():
            query = self.search_entry.get().strip()
            if query:
                filtered = self.searchSeriveController.searchService(query, self.user.user_id)
                if not filtered:
                    messagebox.showerror("No Results", f"No services found for '{query}'.")
                    return
                render_table(filtered)
        
        # Fetch all services for this cleaner
        all_services = self.fetchServiceController.fetchCleanerAllService(self.user.user_id)
        print("Fetched services:", all_services)
        print("Fetched id:", self.user.user_id)

        tk.Button(search_frame, text="Search", command=perform_search).grid(row=0, column=2, padx=5)
        tk.Button(
            search_frame,
            text="Reset",
            command=lambda: render_table(all_services)
        ).grid(row=0, column=3, padx=5)

        # Table Frame
        table_frame = tk.Frame(self.root, bg="#add8e6")
        table_frame.grid(row=2, column=0, columnspan=5, padx=30, pady=10, sticky="nsew")

        # Nested function to render table with original styling
        def render_table(services):
            # Clear previous rows
            for widget in table_frame.winfo_children():
                widget.destroy()

            # Headers
            headers = ["Category", "Service", "Price", "Description", "Actions"]
            for col, header in enumerate(headers):
                tk.Label(
                    table_frame,
                    text=header,
                    font=("Arial", 12, "bold"),
                    borderwidth=1,
                    relief="solid",
                    padx=10,
                    pady=5,
                    bg="#d3d3d3",
                    fg="black"
                ).grid(row=0, column=col, sticky="nsew")

            # Rows
            for row, svc in enumerate(services, start=1):
                row_color = "#add8e6"
                tk.Label(
                    table_frame,
                    text=svc.category_name,
                    borderwidth=1,
                    relief="solid",
                    padx=10,
                    pady=5,
                    bg=row_color
                ).grid(row=row, column=0, sticky="nsew")
                tk.Label(
                    table_frame,
                    text=svc.service_name,
                    borderwidth=1,
                    relief="solid",
                    padx=10,
                    pady=5,
                    bg=row_color
                ).grid(row=row, column=1, sticky="nsew")
                tk.Label(
                    table_frame,
                    text=svc.price,
                    borderwidth=1,
                    relief="solid",
                    padx=10,
                    pady=5,
                    bg=row_color
                ).grid(row=row, column=2, sticky="nsew")
                tk.Label(
                    table_frame,
                    text=svc.description,
                    borderwidth=1,
                    relief="solid",
                    padx=10,
                    pady=5,
                    bg=row_color
                ).grid(row=row, column=3, sticky="nsew")

                # Actions
                action_frame = tk.Frame(table_frame, bg=row_color)
                action_frame.grid(row=row, column=4, sticky="nsew")
                tk.Button(
                    action_frame,
                    text="Edit",
                    command=lambda s=svc: self.openUpdateServiceForm(s.cleaner_id, s.service_id, s.price, s.description),
                    font=("Arial", 10, "bold"),
                    bg="#87CEEB",
                    fg="black",
                    relief="solid",
                    padx=10,
                    pady=5
                ).grid(row=0, column=0, padx=5, pady=5)
                tk.Button(
                    action_frame,
                    text="Delete",
                    command=lambda s=svc: self.deleteService(s.cleaner_id, s.service_id),
                    font=("Arial", 10, "bold"),
                    bg="#FF7F7F",
                    fg="black",
                    relief="solid",
                    padx=10,
                    pady=5
                ).grid(row=0, column=1, padx=5, pady=5)

        render_table(all_services)

        # Navigation Buttons (bottom)
        btn_frame = tk.Frame(self.root, bg="#f0f2f5")
        btn_frame.grid(row=3, column=0, columnspan=5, pady=30)
        tk.Button(
            btn_frame,
            text="Back to Dashboard",
            command=self.displayCleanerPage,
            font=("Arial", 12, "bold"),
            bg="#A9A9A9",
            fg="black",
            padx=20,
            pady=10
        ).grid(row=0, column=0, padx=10)

        
    def openCreateServiceForm(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        # Display form title
        tk.Label(self.root, text="Add Service", font=("Arial", 18)).pack(pady=20)

        # Category selection (Dropdown)
        tk.Label(self.root, text="Choose a Category:").pack(pady=5)
        self.categoryCombobox = ttk.Combobox(self.root, state="readonly")
        self.categoryCombobox.pack(pady=5)

        # Fetch categories and populate the dropdown
        categories = self.fetchCategoriesController.fetchCategories()
        self.categoryCombobox['values'] = [cat.cat_sv_name for cat in categories]
        self.categoryCombobox.bind("<<ComboboxSelected>>", self.onCategorySelected)

        # Service selection (Dropdown
        self.serviceCombobox = ttk.Combobox(self.root, state="readonly")
        self.serviceCombobox.pack(pady=5)

        # Price input
        tk.Label(self.root, text="Price:").pack(pady=5)
        self.priceEntry = tk.Entry(self.root)
        self.priceEntry.pack(pady=5)

        # Description input
        tk.Label(self.root, text="Description:").pack(pady=5)
        self.descriptionEntry = tk.Entry(self.root)
        self.descriptionEntry.pack(pady=5)

        # Submit button
        tk.Button(self.root, text="Add Service", command=self.addService).pack(pady=20)

        tk.Button(self.root, text="Back", command=self.displayCleanerPage).pack(pady=20)

    def getCategoryIdByName(self, categoryName):
        # Return category ID based on category name
        categories = self.fetchCategoriesController.fetchCategories()
        for category in categories:
            if category.cat_sv_name == categoryName:
                return category.catsv_id
        return  None
        
    def getServiceIdByName(self, serviceName):
        # Return service ID based on service name
        # Get the selected category ID
        selectedCategory = self.categoryCombobox.get()
        categoryId = self.getCategoryIdByName(selectedCategory)

        # Fetch the services for this category
        services = self.fetchServicesByCategoryController.fetchServicesByCategory(categoryId)

        # Find the service ID
        for service in services:
            if service.cat_sv_name == serviceName:
                return service.catsv_id
        return None

    def onCategorySelected(self,event):
        # Fetch and display services based on the selected category
        selectedCategory = self.categoryCombobox.get()
        # Get the category ID by fetching it from the database
        catsv_id = self.getCategoryIdByName(selectedCategory)
        print(f"Selected category ID: {catsv_id}")

        # Fetch services based on the selected category ID
        services = self.fetchServicesByCategoryController.fetchServicesByCategory(catsv_id)

        # Update the service dropdown
        self.serviceCombobox['values'] = [service.cat_sv_name for service in services]

    def addService(self):
        # Get values from input fields
        categoryName = self.categoryCombobox.get()
        serviceName = self.serviceCombobox.get()
        price = self.priceEntry.get()
        description = self.descriptionEntry.get()

        if categoryName and serviceName and price and description:
            # Add the service using the controller
            category_id = self.getCategoryIdByName(categoryName)
            service_id = self.getServiceIdByName(serviceName)
            # Call addService method
            success = self.addServiceController.addService(self.user.user_id, category_id ,service_id, price, description)

            if success:
                messagebox.showinfo("Success", "Service added successfully!")
                self.displayCleanerPage()
            else:
                messagebox.showerror("Error", "Failed to add service.")
        else:
            messagebox.showerror("Error", "All fields are required.")

    def openUpdateServiceForm(self, cleaner_id, service_id, current_price, current_desc):
        for widget in self.root.winfo_children():
            widget.destroy()

        print(f"Opening update form for cleaner_id: {cleaner_id}, service_id: {service_id}")

        # Display form title
        tk.Label(self.root, text="Edit Service", font=("Arial", 18)).pack(pady=20)

        # Price input
        tk.Label(self.root, text="New Price:").pack(pady=5)
        self.priceEntry = tk.Entry(self.root)
        self.priceEntry.insert(0, str(current_price))  # pre-fill with current price
        self.priceEntry.pack(pady=5)

        # Description input
        tk.Label(self.root, text="New Description:").pack(pady=5)
        self.descriptionEntry = tk.Entry(self.root)
        self.descriptionEntry.insert(0, current_desc)  # pre-fill with current description
        self.descriptionEntry.pack(pady=5)

        # Update button
        tk.Button(self.root, text="Update Service", command=lambda: self.updateService(cleaner_id, service_id)).pack(pady=20)


    def updateService(self, cleaner_id, service_id):
        self.updateServiceController = controller.UpdateServiceController()
        new_price = self.priceEntry.get().strip()
        new_desc  = self.descriptionEntry.get().strip()

        if not all([new_price, new_desc]):
            messagebox.showerror("Error", "All fields must be filled out.")
            return 

        try:
            price_value = float(new_price)
        except ValueError:
            messagebox.showerror("Invalid Input", "Price must be a number.")
            return 

        success = self.updateServiceController.updateService(
            cleaner_id,
            service_id,
            price_value,
            new_desc
        )

        if success:
            messagebox.showinfo("Success", "Service updated successfully.")
            self.displayMyServicesPage()
        else:
            messagebox.showerror("Error", "Failed to update service. Please try again.")

        return 
    
    def deleteService(self, cleaner_id, service_id):
        try:
            self.deleteServiceController = controller.DeleteServiceController()
            success = self.deleteServiceController.deleteService(cleaner_id, service_id)
            if success:
                messagebox.showinfo("Success", "Service deleted successfully!")
                self.displayMyServicesPage()
            else:
                messagebox.showerror("Error", "Failed to delete service.")
        except Exception as e:
            messagebox.showerror("Exception", f"An error occurred: {e}")

    def viewJobHistory(self):
        # Create a controller instance to fetch job history
        self.jobHistoryController = controller.JobHistoryController()

        # Clear existing widgets
        for widget in self.root.winfo_children():
            widget.destroy()

        # Set default background color
        self.root.configure(bg="#f0f2f5")  # Light background

        # Header
        tk.Label(self.root, text="Job History", font=("Arial", 24, "bold"), bg="#f0f2f5", fg="black").pack(pady=20)

        # Filter Frame
        filter_frame = tk.Frame(self.root, bg="#f0f2f5")  # Match background color
        filter_frame.pack(pady=10)

        # Date Filter Dropdown
        tk.Label(filter_frame, text="Sort by Date:", font=("Arial", 12), bg="#f0f2f5", fg="black").grid(row=0, column=0, padx=5)
        self.date_sort_var = tk.StringVar(value="None")
        date_sort_dropdown = ttk.Combobox(filter_frame, textvariable=self.date_sort_var, state="readonly", width=15)
        date_sort_dropdown['values'] = ["None", "Ascending", "Descending"]
        date_sort_dropdown.grid(row=0, column=1, padx=5)

        # Service Type Filter Dropdown
        tk.Label(filter_frame, text="Filter by Service Type:", font=("Arial", 12), bg="#f0f2f5", fg="black").grid(row=0, column=2, padx=5)
        self.service_filter_var = tk.StringVar(value="All")
        service_filter_dropdown = ttk.Combobox(filter_frame, textvariable=self.service_filter_var, state="readonly", width=20)
        service_filter_dropdown['values'] = ["All", "Steam Cleaning", "Extraction", "Leather Cleaning", "Kitchen Deep Clean", "Bathroom Scrub Down", "Bedroom Deep Clean", "UV-C Cleaning"]
        service_filter_dropdown.grid(row=0, column=3, padx=5)

        # Apply Filter Button
        tk.Button(filter_frame, text="Apply Filters", command=self.applyFilters, font=("Arial", 12), bg="#f0f2f5", fg="blue").grid(row=0, column=4, padx=10)

        # Table Frame
        self.table_frame = tk.Frame(self.root, bg="#ffffff", bd=2, relief="solid")  # White table background
        self.table_frame.pack(padx=40, pady=20, fill="both", expand=True)

        # Fetch and display job history
        self.displayJobHistory()

        # Back to Dashboard Button
        Button(self.root, text="Back to Dashboard", command=self.displayCleanerPage, font=("Arial", 12), bg="#f0f2f5", fg="blue").pack(pady=20)
        
    def applyFilters(self):
        # Get selected filters
        date_sort = self.date_sort_var.get()
        service_filter = self.service_filter_var.get()

        # Fetch filtered job history
        try:
            job_history = self.jobHistoryController.fetchJobHistory(self.user.user_id)

            # Apply service type filter
            if service_filter != "All":
                # Ensure case-insensitive comparison and strip any extra whitespace
                job_history = [job for job in job_history if job['service_provided'].strip().lower() == service_filter.strip().lower()]

            # Apply date sort filter
            if date_sort == "Ascending":
                job_history.sort(key=lambda x: x['booked_at'])
            elif date_sort == "Descending":
                job_history.sort(key=lambda x: x['booked_at'], reverse=True)

            # Update the table
            self.displayJobHistory(job_history)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to apply filters: {e}")

    def displayJobHistory(self, job_history=None):
        if job_history is None:
            try:
                job_history = self.jobHistoryController.fetchJobHistory(self.user.user_id)
            except Exception as e:
                messagebox.showerror("Error", f"Failed to fetch job history: {e}")
                return

        # Clear the table frame
        for widget in self.table_frame.winfo_children():
            widget.destroy()

        # Check if job history is empty
        if not job_history:
            tk.Label(self.table_frame, text="No job history found.", font=("Arial", 12), bg="#ffffff", fg="black").pack(pady=20)
            return

        # Table Headers
        headers = ["No.", "Booked By", "Service Provided", "Total Charged", "Booked At"]
        for col, header in enumerate(headers):
            tk.Label(self.table_frame, text=header, font=("Arial", 12, "bold"), bg="#ffffff", fg="black", borderwidth=1, relief="solid").grid(row=0, column=col, sticky="nsew")

        # Table Rows
        for row_num, job in enumerate(job_history, start=1):
            tk.Label(self.table_frame, text=row_num, font=("Arial", 12), bg="#ffffff", fg="black", borderwidth=1, relief="solid").grid(row=row_num, column=0, sticky="nsew")
            tk.Label(self.table_frame, text=job["booked_by"], font=("Arial", 12), bg="#ffffff", fg="black", borderwidth=1, relief="solid").grid(row=row_num, column=1, sticky="nsew")  # Booked By
            tk.Label(self.table_frame, text=job["service_provided"], font=("Arial", 12), bg="#ffffff", fg="black", borderwidth=1, relief="solid").grid(row=row_num, column=2, sticky="nsew")  # Service Provided
            tk.Label(self.table_frame, text=job["total_charged"], font=("Arial", 12), bg="#ffffff", fg="black", borderwidth=1, relief="solid").grid(row=row_num, column=3, sticky="nsew")  # Total Charged
            tk.Label(self.table_frame, text=job["booked_at"], font=("Arial", 12), bg="#ffffff", fg="black", borderwidth=1, relief="solid").grid(row=row_num, column=4, sticky="nsew")  # Booked At

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
        self.profViewsCtl = controller.CleanerProfViewsController()

    def displayHomeOwnerPage(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        Label(self.root, text=f"Home Owner Dashboard", font=("Arial", 24)).pack(pady=30)
        Label(self.root, text=f"Welcome, {self.user.username}").pack(pady=10)
        Label(self.root, text=f"Role ID: {self.user.role_id}").pack(pady=5)

        Button(self.root, text="View Services", command=self.displayAvailableServicePage).pack(pady=5)
        Button(self.root, text="View Shortlist", command=self.displayShortlistPage).pack(pady=5)
        Button(self.root, text="View Services Booked", command=self.viewBookedServices).pack(pady=5)
        Button(self.root, text="Logout", command=self.logout).pack(pady=20)

    def displayAvailableServicePage(self):
        # Clear existing widgets
        for widget in self.root.winfo_children():
            widget.destroy()

        # Set default background color
        self.root.configure(bg="#f0f2f5")  # Light background

        # Header
        tk.Label(self.root, text="Available Services", font=("Arial", 24, "bold"), bg="#f0f2f5", fg="black").pack(pady=20)

        # Filter Frame
        filter_frame = tk.Frame(self.root, bg="#f0f2f5")  # Match background color
        filter_frame.pack(pady=10)

        # Category Filter Dropdown
        tk.Label(filter_frame, text="Search by Category or Services", font=("Arial", 12), bg="#f0f2f5", fg="black").grid(row=0, column=0, padx=5)
        self.category_filter_var = tk.StringVar(value="All")
        category_filter_dropdown = ttk.Combobox(filter_frame, textvariable=self.category_filter_var, state="readonly", width=20)
        category_filter_dropdown['values'] = [
                    "All",
                    "Sofa Cleaning",
                    "Mattress Cleaning",
                    "Aircon Servicing",
                    "Deep Cleaning",
                    "Steam Cleaning",
                    "Extraction",
                    "Leather Cleaning",
                    "Kitchen Deep Clean",
                    "Bathroom Scrub Down",
                    "Bedroom Deep Clean",
                    "UV-C Cleaning"
                ]
        category_filter_dropdown.grid(row=0, column=1, padx=5)

        # Apply Filter Button
        tk.Button(filter_frame, text="Search", command=self.applySearchByCategory, font=("Arial", 12), bg="#f0f2f5", fg="blue").grid(row=0, column=2, padx=10)

        # Table Frame (for displaying services)
        self.table_frame = tk.Frame(self.root, bg="#add8e6", bd=2, relief="solid")  # White table background
        self.table_frame.pack(padx=40, pady=20, fill="both", expand=True)

        # Fetch and display all available services initially
        self.displayAllServices()

        # Back to Dashboard Button
        tk.Button(self.root, text="Back to Dashboard", command=self.displayHomeOwnerPage, font=("Arial", 12), bg="#f0f2f5", fg="blue").pack(pady=20)

    def applySearchByCategory(self):
        # Get selected category from dropdown
        selected_category = self.category_filter_var.get()

        # Fetch services based on selected category
        if selected_category != "All":
            # Apply filter for specific category
            search_service_controller = controller.SearchAllAvailableServicesController()
            filtered_services = search_service_controller.searchAllServices(selected_category)
        else:
            # No filter, get all services
            search_service_controller = controller.ViewAllAvailableServicesController()
            filtered_services = search_service_controller.getAllAvailableService()

        # Display the fetched services
        self.displayAllServices(filtered_services)

    def displayAllServices(self, services=None):
        if services is None:
            # If no filtered services, fetch all services
            service_controller = controller.ViewAllAvailableServicesController()
            services = service_controller.getAllAvailableService()

        # Clear existing table widgets
        for widget in self.table_frame.winfo_children():
            widget.destroy()

         # Create canvas and scrollbar inside the table_frame
        canvas = tk.Canvas(self.table_frame, bg="#add8e6", highlightthickness=0)
        scrollbar = tk.Scrollbar(self.table_frame, orient="vertical", command=canvas.yview)
        canvas.configure(yscrollcommand=scrollbar.set)

        scrollbar.pack(side="right", fill="y")
        canvas.pack(side="left", fill="both", expand=True)

        # Frame inside canvas for the scrollable content
        scrollable_frame = tk.Frame(canvas, bg="#add8e6")
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

        # Scroll region update
        def on_frame_configure(event):
            canvas.configure(scrollregion=canvas.bbox("all"))

        scrollable_frame.bind("<Configure>", on_frame_configure)

        # Table Headers
        headers = ["Cleaner ID", "Category", "Service Name", "Price", "Actions"]
        for col, header in enumerate(headers):
            tk.Label(scrollable_frame, text=header, font=("Arial", 12, "bold"), bg="#e6e6e6", width=20).grid(row=0, column=col, pady=5)

        # Table Rows
        for row, service in enumerate(services, start=1):
            # Cleaner ID
            tk.Label(scrollable_frame, text=service.cleaner_id, bg="#add8e6", width=20).grid(row=row, column=0, sticky="nsew", pady=5)

            # Category
            tk.Label(scrollable_frame, text=service.category_name, bg="#add8e6", width=20).grid(row=row, column=1, sticky="nsew", pady=5)

            # Service Name
            tk.Label(scrollable_frame, text=service.service_name, bg="#add8e6", width=20).grid(row=row, column=2, sticky="nsew", pady=5)

            # Price
            tk.Label(scrollable_frame, text=f"${service.price}", bg="#add8e6", width=20).grid(row=row, column=3, sticky="nsew", pady=5)

            # Actions (Hire and View Profile buttons)
            action = tk.Frame(scrollable_frame, bg="#add8e6")
            action.grid(row=row, column=4, sticky="nsew", padx=10, pady=5)

    
            tk.Button(action, text="Shortlist",command=lambda cid=service.cleaner_id, cat=service.category_id, sid=service.service_id: 
                self.shortlistService(cid, cat, sid), width=12).pack(side="left", padx=5)
            tk.Button(action, text="View Profile", command=lambda cleaner_id=service.cleaner_id: self.displayCleanerProfilePage(cleaner_id), width=14).pack(side="left", padx=5)

            row += 1
    
    def shortlistService(self, cleaner_id, category_id, service_id):
        shortListController = controller.AddShortlistController()
        added = shortListController.addShortlist(cleaner_id, self.user.user_id,category_id, service_id)
        print(f"Shortlist result from shortlist() method: {added}")  # Debugging output
    
        if added:
            messagebox.showinfo("Shortlist", "Cleaner has been shortlisted!")
        else:
            messagebox.showinfo("Shortlist", "Cleaner is already shortlisted.")

    def removeShortlist(self, cleaner_id, category_id, service_id):
        self.removeShortlistController = controller.RemoveShortlistController()
        removed = self.removeShortlistController.removeShortlist(cleaner_id, self.user.user_id,category_id, service_id)

        if removed:
            messagebox.showinfo("Shortlist", "Shortlist removed!")
            self.displayShortlistPage()

        else:
            messagebox.showwarning("Shortlist", "No matching shortlist entry found or failed to remove!")

        
    def displayCleanerProfilePage(self,cleaner_id):
        countsCtl = controller.CleanerAnalyticsController()
        countsCtl.logView(cleaner_id, self.user.user_id)
        # Clear existing widgets
        for widget in self.root.winfo_children():
            widget.destroy()

        # Set background color
        self.root.configure(bg="#f0f2f5")

        # Fetch cleaner profile info
        cleaner_controller = controller.FetchCleanerProfileController()
        cleaner_services = cleaner_controller.fetchCleanerProfileResult(cleaner_id)

        if not cleaner_services:
            tk.Label(self.root, text="Cleaner not found.", font=("Arial", 16), bg="#f0f2f5", fg="red").pack(pady=20)
            return

        # Extract cleaner basic info from the first service entry
        first_entry = cleaner_services[0]
        cleaner_name = first_entry[1]  # cleaner_name
        cleaner_email = first_entry[2]  # cleaner_email

        # Header Section: Cleaner Info
        profile_frame = tk.Frame(self.root, bg="#ffffff", bd=2, relief="solid")
        profile_frame.pack(padx=40, pady=20, fill="x")

        tk.Label(profile_frame, text=f"Cleaner Name: {cleaner_name}", font=("Arial", 16), bg="#ffffff", anchor="w").pack(pady=5, padx=10, fill="x")
        tk.Label(profile_frame, text=f"Cleaner Email: {cleaner_email}", font=("Arial", 16), bg="#ffffff", anchor="w").pack(pady=5, padx=10, fill="x")

        # Table Section: Services
        table_frame = tk.Frame(self.root, bg="#add8e6", bd=2, relief="solid")
        table_frame.pack(padx=40, pady=20, fill="both", expand=True)

        table_frame.grid_rowconfigure(0, weight=0)
        table_frame.grid_columnconfigure(0, weight=1, uniform="group1")
        table_frame.grid_columnconfigure(1, weight=1, uniform="group1")
        table_frame.grid_columnconfigure(2, weight=2, uniform="group1")
        table_frame.grid_columnconfigure(3, weight=1, uniform="group1")

        # Table Headers
        headers = ["Category", "Service Name", "Description", "Price"]
        for col, header in enumerate(headers):
            tk.Label(table_frame, text=header, font=("Arial", 12, "bold"), bg="#e6e6e6", width=20,
                    anchor="center").grid(row=0, column=col, pady=5, sticky="nsew")

        # Table Rows
        for row, service in enumerate(cleaner_services, start=1):
            category_name = service[4]
            service_name = service[6]
            description = service[8]
            price = service[7]
            bg_color = "#add8e6"  # Keep background consistent or alternate if needed

            tk.Label(table_frame, text=category_name, bg=bg_color, anchor="nw", justify="left",
                    wraplength=150).grid(row=row, column=0, sticky="nw", padx=5, pady=3)
            tk.Label(table_frame, text=service_name, bg=bg_color, anchor="nw", justify="left",
                    wraplength=150).grid(row=row, column=1, sticky="nw", padx=5, pady=3)
            tk.Label(table_frame, text=description, bg=bg_color, anchor="nw", justify="left",
                    wraplength=300).grid(row=row, column=2, sticky="nw", padx=5, pady=3)
            tk.Label(table_frame, text=f"${price}", bg=bg_color, anchor="nw", justify="left").grid(row=row, column=3, sticky="nw", padx=5, pady=3)

        # Back Button
        tk.Button(self.root, text="Back", command=self.displayAvailableServicePage, font=("Arial", 12), bg="#f0f2f5", fg="blue").pack(pady=20)

    def displayShortlistPage(self):
        # Clear existing widgets
        for widget in self.root.winfo_children():
            widget.destroy()

        # Set default background color
        self.root.configure(bg="#f0f2f5")  # Light background

        # Header
        tk.Label(self.root, text="Shortlist", font=("Arial", 24, "bold"), bg="#f0f2f5", fg="black").pack(pady=20)

        # Filter Frame
        filter_frame = tk.Frame(self.root, bg="#f0f2f5")  # Match background color
        filter_frame.pack(pady=10)

        # Category Filter Dropdown
        tk.Label(filter_frame, text="Search by Category or Services:", font=("Arial", 12), bg="#f0f2f5", fg="black").grid(row=0, column=0, padx=5)
        self.category_filter_var = tk.StringVar(value="All")
        category_filter_dropdown = ttk.Combobox(filter_frame, textvariable=self.category_filter_var, state="readonly", width=20)
        category_filter_dropdown['values'] = [
                    "All",
                    "Sofa Cleaning",
                    "Mattress Cleaning",
                    "Aircon Servicing",
                    "Deep Cleaning",
                    "Steam Cleaning",
                    "Extraction",
                    "Leather Cleaning",
                    "Kitchen Deep Clean",
                    "Bathroom Scrub Down",
                    "Bedroom Deep Clean",
                    "UV-C Cleaning"
                ]
        category_filter_dropdown.grid(row=0, column=1, padx=5)

        # Apply Filter Button
        tk.Button(filter_frame, text="Search", command=self.applySearchShortlistByCategory, font=("Arial", 12), bg="#f0f2f5", fg="blue").grid(row=0, column=2, padx=10)

        # Store table_frame in the object for reference
         # Table Frame (for displaying categories)
        self.table_frame = tk.Frame(self.root, bg="#add8e6", bd=2, relief="solid")  # Table background
        self.table_frame.pack(padx=40, pady=20, fill="both", expand=True)

        # Fetch and display shortlist
        self.displayShortlistServices()

        # Back to Dashboard Button
        tk.Button(self.root, text="Back to Dashboard", command=self.displayHomeOwnerPage, font=("Arial", 12), bg="#f0f2f5", fg="blue").pack(pady=20)

    def applySearchShortlistByCategory(self):
    # Get selected category from dropdown
        selected_category = self.category_filter_var.get()

        # Fetch shortlisted services based on selected category
        if selected_category != "All":
            # Apply filter for specific category for shortlisted services
            search_service_controller = controller.SearchShortlistedServicesController()
            filtered_services = search_service_controller.fetchShortlistedServiceCategoryResult(self.user.user_id, selected_category)
            print(f"[DEBUG] Filtered services for '{selected_category}':", filtered_services)
        else:
            # No filter, get all shortlisted services
            search_service_controller = controller.ViewShortlistedServicesController()
            filtered_services = search_service_controller.getShortlistedServices(self.user.user_id)

        # Display the fetched shortlisted services
        self.displayShortlistServices(filtered_services)

    def displayShortlistServices(self, services=None):
        if services is None:
          # If no filtered services, fetch all services
            shortlistController = controller.ViewShortlistedServicesController()
            shortlistedServices = shortlistController.getShortlistedServices(self.user.user_id)
        else:
            shortlistedServices = services

        # Clear existing widgets inside table_frame only (this will reset the table each time it's updated)
        for widget in self.table_frame.winfo_children():
            widget.destroy()

        # Create canvas and scrollbar inside the table_frame
        canvas = tk.Canvas(self.table_frame, bg="#add8e6", highlightthickness=0)
        scrollbar = tk.Scrollbar(self.table_frame, orient="vertical", command=canvas.yview)
        canvas.configure(yscrollcommand=scrollbar.set)

        scrollbar.pack(side="right", fill="y")
        canvas.pack(side="left", fill="both", expand=True)

        # Frame inside canvas for the scrollable content
        scrollable_frame = tk.Frame(canvas, bg="#add8e6")
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

        # Scroll region update
        def on_frame_configure(event):
            canvas.configure(scrollregion=canvas.bbox("all"))

        scrollable_frame.bind("<Configure>", on_frame_configure)

        # Table Headers
        headers = ["Cleaner ID", "Category", "Service Name", "Price", "Actions"]
        for col, header in enumerate(headers):
            tk.Label(scrollable_frame, text=header, font=("Arial", 12, "bold"), bg="#e6e6e6", width=20).grid(row=0, column=col, sticky="nsew", pady=5)

        # Table Rows
        for row, service in enumerate(shortlistedServices, start=1):
            # Cleaner ID
            tk.Label(scrollable_frame, text=service.cleaner_id, bg="#add8e6", width=20).grid(row=row, column=0, sticky="nsew", pady=5)

            # Category
            tk.Label(scrollable_frame, text=service.category_name, bg="#add8e6", width=20).grid(row=row, column=1, sticky="nsew", pady=5)

            # Service Name
            tk.Label(scrollable_frame, text=service.service_name, bg="#add8e6", width=20).grid(row=row, column=2, sticky="nsew", pady=5)

            # Price
            tk.Label(scrollable_frame, text=f"${service.price}", bg="#add8e6", width=20).grid(row=row, column=3, sticky="nsew", pady=5)

            # Actions (Remove and View Profile buttons)
            action = tk.Frame(scrollable_frame, bg="#add8e6")
            action.grid(row=row, column=4, sticky="nsew", padx=10, pady=5)

            tk.Button(action, text="Remove", command=lambda cid=service.cleaner_id, cat=service.category_id, sid=service.service_id: 
                    self.removeShortlist(cid, cat, sid), width=12).pack(side="left", padx=5)
            tk.Button(action, text="View Profile", command=lambda cleaner_id=service.cleaner_id: self.displayCleanerProfilePage(cleaner_id), width=14).pack(side="left", padx=5)

        

    def viewBookedServices(self):
        # Clear existing widgets
        for widget in self.root.winfo_children():
            widget.destroy()

        # Header
        tk.Label(self.root, text="Booked Services", font=("Arial", 24, "bold"), bg="#f0f2f5", fg="black").pack(pady=20)

        # Filter Frame
        filter_frame = tk.Frame(self.root, bg="#f0f2f5")  # Match background color
        filter_frame.pack(pady=10)

        # Name Filter
        tk.Label(filter_frame, text="Search by Name:", font=("Arial", 12), bg="#f0f2f5", fg="black").grid(row=0, column=0, padx=5)
        name_filter_var = tk.StringVar()
        name_filter_entry = tk.Entry(filter_frame, textvariable=name_filter_var, width=20)
        name_filter_entry.grid(row=0, column=1, padx=5)

        # Month Filter
        tk.Label(filter_frame, text="Filter by Month:", font=("Arial", 12), bg="#f0f2f5", fg="black").grid(row=0, column=2, padx=5)
        month_filter_var = tk.StringVar(value="All")
        month_filter_dropdown = ttk.Combobox(filter_frame, textvariable=month_filter_var, state="readonly", width=15)
        month_filter_dropdown['values'] = ["All", "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
        month_filter_dropdown.grid(row=0, column=3, padx=5)

        # Apply Filter Button
        def apply_filters():
            name_filter = name_filter_var.get().strip().lower()
            selected_month = month_filter_var.get()

            # Fetch booked services from the controller
            booked_services_controller = controller.BookedServicesController()
            booked_services = booked_services_controller.fetchBookedServices(self.user.user_id)

            # Filter by name
            name_filter = name_filter.strip().lower()
            if name_filter:
                booked_services = [
                service for service in booked_services
                if name_filter in service["service_name"].lower()
             ]

            # Filter by month
            if selected_month != "All":
                month_index = month_filter_dropdown['values'].index(selected_month)  # Get the month index
                booked_services = [
                    service for service in booked_services
                    if service["booked_at"].month == month_index
                ]

            # Update the table with filtered results
            render_table(booked_services)

        tk.Button(filter_frame, text="Apply Filters", command=apply_filters, font=("Arial", 12), bg="#f0f2f5", fg="blue").grid(row=0, column=4, padx=10)

        # Table Frame
        table_frame = tk.Frame(self.root, bg="#add8e6", bd=2, relief="solid")  # Light blue table background
        table_frame.pack(padx=40, pady=20, fill="both", expand=True)

        # Function to render the table
        def render_table(booked_services):
            # Clear existing table widgets
            for widget in table_frame.winfo_children():
                widget.destroy()

            # Table Headers
            headers = ["Cleaner ID", "Cleaner Name", "Category ID", "Service Name", "Total Charged", "Booked At"]
            for col, header in enumerate(headers):
                tk.Label(table_frame, text=header, font=("Arial", 12, "bold"), bg="#e6e6e6", fg="black", borderwidth=1, relief="solid").grid(row=0, column=col, sticky="nsew")

            # Table Rows
            for row_num, service in enumerate(booked_services, start=1):
                tk.Label(table_frame, text=service["cleaner_id"], font=("Arial", 12), bg="#ffffff", fg="black", borderwidth=1, relief="solid").grid(row=row_num, column=0, sticky="nsew")
                tk.Label(table_frame, text=service["cleaner_name"], font=("Arial", 12), bg="#ffffff", fg="black", borderwidth=1, relief="solid").grid(row=row_num, column=1, sticky="nsew")
                tk.Label(table_frame, text=service["category_id"], font=("Arial", 12), bg="#ffffff", fg="black", borderwidth=1, relief="solid").grid(row=row_num, column=2, sticky="nsew")
                tk.Label(table_frame, text=service["service_name"], font=("Arial", 12), bg="#ffffff", fg="black", borderwidth=1, relief="solid").grid(row=row_num, column=3, sticky="nsew")
                tk.Label(table_frame, text=f"${service['total_charged']}", font=("Arial", 12), bg="#ffffff", fg="black", borderwidth=1, relief="solid").grid(row=row_num, column=4, sticky="nsew")
                tk.Label(table_frame, text=service["booked_at"], font=("Arial", 12), bg="#ffffff", fg="black", borderwidth=1, relief="solid").grid(row=row_num, column=5, sticky="nsew")

        # Fetch and display all booked services initially
        booked_services_controller = controller.BookedServicesController()
        booked_services = booked_services_controller.fetchBookedServices(self.user.user_id)
        render_table(booked_services)

        # Back to Dashboard Button
        tk.Button(self.root, text="Back to Dashboard", command=self.displayHomeOwnerPage, font=("Arial", 12), bg="#f0f2f5", fg="blue").pack(pady=20)
        
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
        Button(self.root, text="View Cleaning Categories", command=self.viewCategoriesPage).pack(pady=5)
        Button(self.root, text="View Reports", command=self.displayReportsPage).pack(pady=5)

        Button(self.root, text="Logout", command=self.logout).pack(pady=20)
    
    def _parse_date(self, s: str, label: str) -> datetime.date | None:
        """
        Convert 'YYYY-MM-DD' string to date.
        Shows an error and returns None on bad input.
        """
        try:
            return datetime.date.fromisoformat(s.strip())
        except ValueError:
            messagebox.showerror("Date error",
                f"Please enter {label} in YYYY-MM-DD format.")
            return None

    # --------------------------------------------------------------
    #  Reports UI
    # --------------------------------------------------------------
    def displayReportsPage(self):

        for w in self.root.winfo_children():
            w.destroy()

        tk.Label(self.root, text="Platform Reports",
                font=("Arial", 24)).pack(pady=20)

        # ───── period selector frame ──────────────────────────────────────
        sel = tk.Frame(self.root); sel.pack(pady=10)
        bg = "#2b2b2b"

        # --- DAILY --------------------------------------------------------
        row1 = tk.Frame(self.root, bg=bg); row1.pack(pady=4)
        tk.Label(row1, text="Daily", bg=bg, fg="white").pack(side="left", padx=8)

        self.day_var  = tk.StringVar(value=str(datetime.date.today()))
        tk.Entry(row1, textvariable=self.day_var, width=10).pack(side="left")

        tk.Button(row1, text="Show",
                command=lambda: (
                    (d := self._parse_date(self.day_var.get(), "a date"))
                    and self.showReport("daily", d, d)
                )).pack(side="left", padx=6)

        # --- WEEKLY -------------------------------------------------------
        row2 = tk.Frame(self.root, bg=bg); row2.pack(pady=4)
        tk.Label(row2, text="Week containing", bg=bg, fg="white")\
        .pack(side="left", padx=8)

        self.week_var = tk.StringVar(value=str(datetime.date.today()))
        tk.Entry(row2, textvariable=self.week_var, width=10).pack(side="left")

        tk.Button(row2, text="Show",
                command=self._handle_week).pack(side="left", padx=6)

        # --- MONTHLY ------------------------------------------------------
        row3 = tk.Frame(self.root, bg=bg); row3.pack(pady=4)
        tk.Label(row3, text="Month (YYYY-MM)", bg=bg, fg="white")\
        .pack(side="left", padx=8)

        self.month_var = tk.StringVar(value=datetime.date.today().strftime("%Y-%m"))
        tk.Entry(row3, textvariable=self.month_var, width=7).pack(side="left")

        tk.Button(row3, text="Show",
                command=self._handle_month).pack(side="left", padx=6)

        # headline result
        self.result = tk.Label(self.root, font=("Consolas", 14), justify="left")
        self.result.pack(pady=10)

        tk.Button(self.root, text="Back",
                command=self.PlatformMngrPage).pack(pady=10)

    def _handle_week(self):
        any_day = self._parse_date(self.week_var.get(), "a date")
        if not any_day:
            return
        start = any_day - datetime.timedelta(days=any_day.weekday())  # Monday
        end   = start + datetime.timedelta(days=6)                    # Sunday
        self.showReport("weekly", start, end)

    def _handle_month(self):
        try:
            first = datetime.datetime.strptime(self.month_var.get().strip(),
                                            "%Y-%m").date().replace(day=1)
        except ValueError:
            messagebox.showerror("Date error",
                                "Enter month as YYYY-MM, e.g. 2025-05")
            return
        days = calendar.monthrange(first.year, first.month)[1]
        last = first.replace(day=days)
        self.showReport("monthly", first, last)

    def _render_report(self, period: str, frm: datetime.date, to: datetime.date):

        if period == "daily":
            rep = controller.DailyReportController()
        elif period == "weekly":
            rep = controller.WeeklyReportController()
        else:                     # monthly
            rep = controller.MonthlyReportController()

        cat_data     = rep.category_report(frm, to)
        cleaners     = rep.distinct_cleaners(frm, to)
        cleaner_data = rep.cleaner_report(frm, to)

        self.result.config(text=f"Unique cleaners booked: {cleaners}")

        if not cat_data:
            messagebox.showinfo("No data")
            return

        pretty = {"daily":   "Daily",
                "weekly":  "Weekly",
                "monthly": "Monthly"}[period]
        
        range_txt = f"{frm:%d %b %Y} – {to:%d %b %Y}"

        # bookings by category chart
        fig1, ax1 = plt.subplots(figsize=(6, 3.5))
        bars = ax1.bar(cat_data.keys(), cat_data.values(), width=0.55)
        ax1.set_title(f"{pretty} bookings ({range_txt})")
        ax1.set_ylabel("Bookings")
        ax1.set_xticks(range(len(cat_data)))
        ax1.set_xticklabels(cat_data.keys(), rotation=25, ha="right")
        fig1.tight_layout()

        # bookings by cleaner chart
        fig2, ax2 = plt.subplots(figsize=(6, 2.8))
        ax2.bar(cleaner_data.keys(), cleaner_data.values(),
                width=0.55, color="#4c72b0")
        ax2.set_title(f"{pretty} cleaners booked ({range_txt})")
        ax2.set_ylabel("Count")
        ax2.set_xticks(range(len(cleaner_data)))
        ax2.set_xticklabels(cleaner_data.keys(), rotation=25, ha="right")
        for side in ("top", "right"):
            ax2.spines[side].set_visible(False)
        fig2.tight_layout()

        if hasattr(self, "chart_frame"):
            self.chart_frame.destroy()           # clear old charts if they exist
        self.chart_frame = tk.Frame(self.root, bg="#ffffff", relief="sunken")
        self.chart_frame.pack(fill="both", expand=True, padx=20, pady=10)

        for f in (fig1, fig2):                   # embed both charts
            cvs = FigureCanvasTkAgg(f, master=self.chart_frame)
            cvs.draw()
            cvs.get_tk_widget().pack(
                side="top", fill="both", expand=True, pady=6)
            
    def showReport(self, period: str,
                   frm: datetime.date, to: datetime.date):
        self.root.after_idle(
            lambda: self._render_report(period, frm, to))

    def viewCategoriesPage(self):
    # Clear the current page, but leave the search bar and buttons intact
        for widget in self.root.winfo_children():
            widget.destroy()

        self.viewCategories = controller.FetchCategoriesController()

        # Set default background color
        self.root.configure(bg="#f0f2f5")  # Light background

        Label(self.root, text="Cleaning Categories", font=("Arial", 20)).pack(pady=20)

        # Create a frame to hold search bar and button
        search_frame = tk.Frame(self.root, bg="#f0f2f5")
        search_frame.pack(pady=20)

        # Create a search bar inside the frame
        self.searchEntry = StringVar()  # StringVar to hold the search query
        search_bar = Entry(search_frame, textvariable=self.searchEntry, font=("Arial", 14), width=30)
        search_bar.pack(side="left", padx=5)

        # Create a search button to the right of the search bar
        search_button = Button(search_frame, text="Search", command=self.searchCategories, font=("Arial", 12))
        search_button.pack(side="left", padx=5)

        # Add Category button (new button to add category)
        add_category_button = Button(self.root, text="Add Category", command=lambda: self.openAddCategoryForm(), font=("Arial", 12))
        add_category_button.pack(pady=10)

        addServiceButton = Button(self.root, text="Add Service", command=lambda: self.openAddServiceForm(), font=("Arial", 12))
        addServiceButton.pack(pady=10)

        # Store table_frame in the object for reference
         # Table Frame (for displaying categories)
        self.table_frame = tk.Frame(self.root, bg="#add8e6", bd=2, relief="solid")  # Table background
        self.table_frame.pack(padx=40, pady=20, fill="both", expand=True)

        self.displayCategories()

        Button(self.root, text="Back", command=self.PlatformMngrPage).pack(pady=20)

    def searchCategories(self):
        self.searchAllCategories = controller.SearchCategoryController()

        search_query = self.searchEntry.get().strip()
        if search_query:
            # call the controller’s method you just wrote
            categories = self.searchAllCategories.searchCategories(search_query)
        else:
            # if the box is empty, fall back to showing all
            categories = self.viewCategories.fetchCategories()
        # refresh the table with whatever list we got back
        self.displayCategories(categories)

    def displayCategories(self, categories=None):
        if categories is None:
            categories = self.viewCategories.fetchCategories()

        # Clear existing widgets in table_frame only
        for widget in self.table_frame.winfo_children():
            widget.destroy()

        # Create canvas and scrollbar
        canvas = tk.Canvas(self.table_frame, bg="#add8e6", highlightthickness=0)
        scrollbar = tk.Scrollbar(self.table_frame, orient="vertical", command=canvas.yview)
        canvas.configure(yscrollcommand=scrollbar.set)

        scrollbar.pack(side="right", fill="y")
        canvas.pack(side="left", fill="both", expand=True)

        # Frame inside canvas
        scrollable_frame = tk.Frame(canvas, bg="#add8e6")
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

        # Scroll region update
        def on_frame_configure(event):
            canvas.configure(scrollregion=canvas.bbox("all"))

        scrollable_frame.bind("<Configure>", on_frame_configure)


        # Table Headers
        headers = ["Category ID", "Category Name", "Description", "Actions"]
        for col, header in enumerate(headers):
            tk.Label(scrollable_frame, text=header, font=("Arial", 12, "bold"), bg="#e6e6e6", width=20).grid(row=0, column=col, pady=5)

    
        # Rows
        for row, category in enumerate(categories, start=1):
            # Category ID
            tk.Label(scrollable_frame, text=category.catsv_id, bg="#add8e6", width=20).grid(row=row, column=0, pady=5)

            # Category Name
            tk.Label(scrollable_frame, text=category.cat_sv_name, bg="#add8e6", width=20).grid(row=row, column=1, pady=5)

            # Category Description
            tk.Label(scrollable_frame, text=category.cat_desc, bg="#add8e6", width=20).grid(row=row, column=2, pady=5)

            # Actions (View, Update, and Delete buttons)
            action = tk.Frame(scrollable_frame, bg="#add8e6")
            action.grid(row=row, column=3, pady=5)

            tk.Button(action, text="View Services", command=lambda c=category: dummy(c), width=12).pack(side="left", padx=5)
            tk.Button(action, text="Update", command=lambda c=category: self.openUpdateCategoryForm(c), width=12).pack(side="left", padx=5)
            tk.Button(action, text="Delete", command=lambda c=category: self.deleteCategory(c), width=12).pack(side="left", padx=5)

    
    def openAddCategoryForm(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        # Display form title
        tk.Label(self.root, text="Add Category", font=("Arial", 18)).pack(pady=20)

        # Price input
        tk.Label(self.root, text="Category Name:").pack(pady=5)
        self.nameEntry = tk.Entry(self.root)
        self.nameEntry.pack(pady=5)

        # Description input
        tk.Label(self.root, text="Description:").pack(pady=5)
        self.descriptionEntry = tk.Entry(self.root)
        self.descriptionEntry.pack(pady=5)

        # Submit button
        tk.Button(self.root, text="Add Category", command=self.addCategory).pack(pady=20)

        tk.Button(self.root, text="Back", command=self.viewCategoriesPage).pack(pady=20)

    def addCategory(self):
        self.addCategoryController = controller.AddCategoryController()
        catName = self.nameEntry.get().strip()
        catDesc = self.descriptionEntry.get().strip()

        if not catName:
            messagebox.showwarning("Input Error", "Category name is required.")
            return

        success = self.addCategoryController.addCategory(catName, catDesc)

        if success:
            messagebox.showinfo("Success", f"Category '{catName}' added successfully.")
            self.viewCategoriesPage()
        else:
            messagebox.showerror("Error", "Failed to add category. Check the database or try again.")

    def openAddServiceForm(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        # Display form title
        tk.Label(self.root, text="Add Services", font=("Arial", 18)).pack(pady=20)

        # Fetch existing categories
        fetchController= controller.FetchCategoriesController()
        self.categories = fetchController.fetchCategories() 

         # Check if categories are found, otherwise show an error message
        if not self.categories:
            tk.Label(self.root, text="No categories available. Please add categories first.", font=("Arial", 12), fg="red").pack(pady=10)
            return  # Exit the function if no categories are found

        # Category dropdown (combobox)
        category_names = [cat.cat_sv_name for cat in self.categories]  # Assuming the second item in tuple is the category name
        tk.Label(self.root, text="Select Category:", font=("Arial", 12)).pack(pady=10)
    
        # Create a combobox for category selection
        self.category_combobox = ttk.Combobox(self.root, values=category_names, width=30)
        self.category_combobox.pack(pady=10)

        # Service Name input
        tk.Label(self.root, text="Service Name:", font=("Arial", 12)).pack(pady=10)
        self.servNameEntry = tk.Entry(self.root, width=30)
        self.servNameEntry.pack(pady=10)

        # Add Service Button
        add_service_button = tk.Button(self.root, text="Add Service", font=("Arial", 12), command=self.addNewService)
        add_service_button.pack(pady=20)

    def addNewService(self): # OUT OF SCOPE
        cat_sv_name = self.servNameEntry.get()  
        selected_category_name  = self.category_combobox.get()
        print("Selected:", selected_category_name) 

        for cat in self.categories:
            print("Comparing to:", cat.cat_sv_name)
            if cat.cat_sv_name.strip() == selected_category_name.strip():
                parentCat_id = cat.catsv_id
                break

        # Call the controller's add function
        self.addPlatServiceController = controller.AddPlatformServiceController()

        parentCat_id = None
        for cat in self.categories:
            print("Comparing to:", cat.cat_sv_name)
            if cat.cat_sv_name.strip() == selected_category_name.strip():
                parentCat_id = cat.catsv_id
                break

        if parentCat_id is None:
            print("Error: Selected category not found.")
        else:
            cat_sv_name = self.servNameEntry.get()
            # Now use the correct ID
            success = self.addPlatServiceController.addService(cat_sv_name, parentCat_id)
        
        if success:
            print("Service successfully added!")
        else:
            print("Failed to add service.")
        
    def deleteCategory(self, category):
        self.deleteCat = controller.DeleteCategoryController()
        confirm = messagebox.askyesno("Confirm Deletion", f"Are you sure you want to delete category '{category.cat_sv_name}'?")
        if confirm:
            success = self.deleteCat.deleteCategory(category.catsv_id)
            if success:
                messagebox.showinfo("Success", f"Category '{category.cat_sv_name}' has been deleted.")
                self.displayCategories()  # Refresh the table
            else:
                messagebox.showerror("Error", "Failed to delete the category.")

    def openUpdateCategoryForm(self, category):
        for widget in self.root.winfo_children():
            widget.destroy()

        # Display form title
        tk.Label(self.root, text="Update Category Description", font=("Arial", 18)).pack(pady=20)

        # Category Description
        tk.Label(self.root, text="Category Description:", font=("Arial", 12)).pack(pady=10)
        self.descEntry = tk.Entry(self.root, width=30)
        desc_text = str(category.cat_desc) if category.cat_desc is not None else ""
        self.descEntry.insert(tk.END, desc_text)  # Set default value
        self.descEntry.pack(pady=10)

        # Update Button
        updateCategoryButton = tk.Button(
            self.root,
            text="Update Category",
            font=("Arial", 12),
            command=lambda c=category: self.updateCategory(c)
        )
        updateCategoryButton.pack(pady=20)

    def updateCategory(self, category):
        self.updateCatDesc = controller.UpdateCategoryController()
        newCatDesc = self.descEntry.get()

        # Update the category
        success = self.updateCatDesc.updateCategoryDesc(category.catsv_id,newCatDesc)
        if success:
            messagebox.showinfo(
                "Success",
                f"Category '{category.cat_sv_name}' has been updated."
            )
            self.viewCategoriesPage()  # Refresh the table
        else:
            messagebox.showerror("Error", "Failed to update the category.")
      


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
