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

        if not user:
            messagebox.showerror("Login Failed", "Invalid credentials.")
            return

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

            # Clear existing button_frame if it exists (to avoid duplicate buttons)
            if hasattr(self, 'button_frame') and self.button_frame:
                self.button_frame.destroy()

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

            # Action Buttons
            self.button_frame = tk.Frame(self.root, bg="#f0f0f0")
            self.button_frame.grid(row=row_count, column=0, columnspan=5, pady=10)
                
            style_btn = lambda text, cmd, color: tk.Button(self.button_frame, text=text, command=cmd, bg=color, fg="black", font=("Arial", 12, "bold"), padx=20, pady=5)

            # Back and logout buttons inside the table frame (or you can place them in a separate frame as well)
            style_btn("Back to Dashboard", self.displayAdminPage, "#607d8b").grid(row=0, column=0, padx=10)
            style_btn("View Profiles", self.openManageProfiles, "#3f51b5").grid(row=0, column=1, padx=10)
            style_btn("Add Account", self.displayCreateAccountForm, "#009688").grid(row=0, column=2, padx=10)

        render_table(self.all_accounts)

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

        # Message
        tk.Label(inner, text="Are you sure you want to suspend this user?", font=("Arial", 12, "bold"), bg="#add8e6",wraplength=300,justify="center").pack(pady=(5, 20))

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

        # Dynamically update the button text based on current suspension status
        suspend_button_text = "Suspend" if not currently_suspended else "Reactivate"
        
        def handle_suspend():
            self.toggleSuspension(user_id, currently_suspended)
            popup.destroy()

        # Suspend button with styling
        suspend_btn = tk.Button(button_frame, text=suspend_button_text, width=10, command=handle_suspend, highlightbackground="#add8e6", activebackground="#8fc5d8", relief="flat")
        suspend_btn.pack(side="left", padx=10)

    def toggleSuspension(self, user_id, currently_suspended):
        # Flip the flag
        self.suspendController.setAccountSuspension(user_id, not bool(currently_suspended))
        # Feedback
        state = "suspended" if not currently_suspended else "reactivated"
        messagebox.showinfo("Success", f"Account {user_id} {state}.")
        # Refresh the table so status & button update
        self.displayAccountsPage()

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
    
    def displayCreateAccountForm(self,):
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
            name = name_entry.get()
            username = username_entry.get()
            password = password_entry.get()
            confirm = confirm_password_entry.get()
            email = email_entry.get()
            selected_role_name = self.selectedRole.get()
            role_id = self.roleMap[selected_role_name]

            if password != confirm:
                messagebox.showerror("Error", "Passwords do not match.")
                return
            
            try:
                self.createController.createAccount(name, username, password ,email, role_id)
                # Controller: Return Data
                messagebox.showinfo("Success", f"Account for {username} created successfully!")
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {e}")

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

        cancel_button = tk.Button(self.root, text="Cancel", command=self.cancelAccUpdate)
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

        if new_password != confirmpw:
            messagebox.showerror("Error", "Passwords do not match.")
            return

        # Validate the input
        if not new_username or not new_password or not new_role_id:
            messagebox.showerror("Error", "All fields must be filled out")
            return

        try:
            # Call the controller's update method with the correct parameters
            self.controller.updateAccount(user_id, new_name, new_username, new_email, new_password, new_role_id)
            messagebox.showinfo("Success", "Account updated successfully!")
            self.displayAccountsPage()  # Refresh the accounts page after successful update
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    def cancelAccUpdate(self):
        # Simply go back to the accounts page without making any changes
        self.displayAccountsPage()

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    # User Profile functions
    # Opens the Profile page
    def openManageProfiles(self):
        self.displayProfilesPage()

    def displayProfilesPage(self):
        # Create ViewProfiles controller instance
        self.controller = controller.ViewProfileController()
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
                render_table(filtered_profiles)

        tk.Button(search_frame, text="Search", command=perform_search).grid(row=0, column=2, padx=5)
        tk.Button(search_frame, text="Reset", command=lambda: render_table(self.controller.viewProfiles())).grid(row=0, column=3, padx=5)

         # Table Frame
        table_frame = tk.Frame(self.root, bg="#add8e6")
        table_frame.grid(row=2, column=0, columnspan=4, padx=30, pady=10, sticky="nsew")


        self.all_profiles = self.controller.viewProfiles()

        def render_table(profiles):
            # Clear previous widgets in table frame
            for widget in table_frame.winfo_children():
                widget.destroy()

            # Clear existing button_frame if it exists (to avoid duplicate buttons)
            if hasattr(self, 'button_frame') and self.button_frame:
                self.button_frame.destroy()

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
                suspend_btn = tk.Button(action_frame, text=suspend_button_text,  command=dummy, fg="black", font=("Arial", 12, "bold"), width=8,  borderwidth=0, cursor="hand2")
                suspend_btn.pack(side="left", padx=10)

                row_count += 1  # Increment the row count after each account

            # Action Buttons
            self.button_frame = tk.Frame(self.root, bg="#f0f0f0")
            self.button_frame.grid(row=row_count, column=0, columnspan=5, pady=10)
                
            style_btn = lambda text, cmd, color: tk.Button(self.button_frame, text=text, command=cmd, bg=color, fg="black", font=("Arial", 12, "bold"), padx=20, pady=5)

            # Back and logout buttons inside the table frame (or you can place them in a separate frame as well)
            style_btn("Back to Dashboard", self.displayAdminPage, "#607d8b").grid(row=0, column=0, padx=10)
            style_btn("View Accounts", self.openManageAccounts, "#3f51b5").grid(row=0, column=1, padx=10)
            style_btn("Add Account", self.displayCreateAccountForm, "#009688").grid(row=0, column=2, padx=10)


        render_table(self.all_profiles)

        


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

        cancel_button = tk.Button(self.root, text="Cancel", command=self.cancelProfUpdate)
        cancel_button.pack(pady=10)

    def submitProfUpdate(self, role_id):
        # Get the values entered in the fields
        new_role = self.new_role_entry.get()

        # Validate the input
        if not new_role:
            messagebox.showerror("Error", "All fields must be filled out")
            return

        try:
            # Call the controller's update method with the correct parameters
            self.controller.updateProfile(role_id, new_role)
            messagebox.showinfo("Success", "Profile updated successfully!")
            self.displayProfilesPage()  # Refresh the accounts page after successful update
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    def cancelProfUpdate(self):
        # Simply go back to the accounts page without making any changes
        self.displayProfilesPage()

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
        counts = controller.CleanerAnalyticsController().getCounts(self.user.user_id)
        tk.Label(self.root, text=f"Profile views: {counts['views']}").pack()
        tk.Label(self.root, text=f"Times shortlisted: {counts['shortlists']}").pack(pady=(0,10))


        # Add Admin features here
        Button(self.root, text="View Services", command=dummy).pack(pady=5)
        Button(self.root, text="Add Services", command=self.createCategoryServiceForm).pack(pady=5)
        Button(self.root, text="View Interest Metrics", command=dummy).pack(pady=5)

        Button(self.root, text="Logout", command=self.logout).pack(pady=20)
    
    def createCategoryServiceForm(self):
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

        # Service selection (Dropdown) - initially empty
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
            service_id = self.getServiceIdByName(serviceName)
            success = self.addServiceController.addService(self.user.user_id, service_id, price, description)

            if success:
                messagebox.showinfo("Success", "Service added successfully!")
                self.displayCleanerPage()
            else:
                messagebox.showerror("Error", "Failed to add service.")
        else:
            messagebox.showerror("Error", "All fields are required.")
    


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
        self.analyticsCtl = controller.CleanerAnalyticsController()


    def displayHomeOwnerPage(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        Label(self.root, text=f"Home Owner Dashboard", font=("Arial", 24)).pack(pady=30)
        Label(self.root, text=f"Welcome, {self.user.username}").pack(pady=10)
        Label(self.root, text=f"Role ID: {self.user.role_id}").pack(pady=5)

        # Add Admin features here
        Button(self.root, text="View Cleaners Available",
            command=self.displayCleanersPage).pack(pady=5)



        Button(self.root, text="Logout", command=self.logout).pack(pady=20)

    def displayCleanersPage(self):
        # wipe current widgets
        for w in self.root.winfo_children():
            w.destroy()

        tk.Label(self.root,
                text="Available Cleaners",
                font=("Arial", 24)).pack(pady=20)

        table = tk.Frame(self.root, bg="#add8e6")
        table.pack(padx=40, pady=10)

        cleaners = controller.ViewAccountsController().viewAccounts()

        headers = ["Cleaner", "Actions"]
        for col, h in enumerate(headers):
            tk.Label(table, text=h, font=("Arial", 12, "bold"),
                    bg="#e6e6e6", width=20).grid(row=0, column=col, pady=5)

        row = 1
        for c in cleaners:
            if c.role_id != 2:   # only cleaners
                continue

            # name
            tk.Label(table, text=c.username, bg="#add8e6", width=20)\
            .grid(row=row, column=0, pady=5)

            # fetch current shortlist status once per cleaner
            countsCtl = controller.CleanerAnalyticsController()
            is_shortlisted = countsCtl.model.shortlist_count_for_user(
                                cleaner_id=c.user_id,
                                homeowner_id=self.user.user_id)

            btn_text = "Remove from shortlist" if is_shortlisted else "Shortlist"

            # frame to hold the two buttons
            action = tk.Frame(table, bg="#add8e6")
            action.grid(row=row, column=1, pady=5)

            def open_profile(uid=c.user_id):
                countsCtl.logView(uid, self.user.user_id)
                # in a real app you'd show profile details here
                messagebox.showinfo("Profile", f"Opened cleaner {uid}'s profile")

            tk.Button(action, text="Open profile",
                    command=open_profile, width=16).pack(side="left", padx=5)

            def toggle(uid=c.user_id):
                countsCtl.toggleShortlist(uid, self.user.user_id)
                # redraw the cleaners page so button text refreshes
                self.displayCleanersPage()

            tk.Button(action, text=btn_text,
                    command=toggle, width=18).pack(side="left", padx=5)

            row += 1

        # back nav
        tk.Button(self.root, text="Back",
                command=self.displayHomeOwnerPage).pack(pady=20)

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
