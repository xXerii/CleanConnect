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
        # Create ViewAccounts controller instance
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

        # Clear the existing window
        for widget in self.root.winfo_children():
            widget.destroy()

        # Set background color
        self.root.configure(bg="#f0f2f5")

        # Title Frame
        title_frame = tk.Frame(self.root, bg="#f0f2f5")
        title_frame.grid(row=0, column=0, columnspan=5, pady=30)

        tk.Label(title_frame, text="User Accounts", font=("Arial", 24, "bold"), bg="#f0f2f5", fg="#333").grid(row=0, column=0, padx=200)

        # Table Frame
        table_frame = tk.Frame(self.root, bg="#add8e6")
        table_frame.grid(row=1, column=0, columnspan=4, padx=30, pady=10, sticky="nsew")

        headers = ["User ID", "Username", "Role", "Actions"]
        header_font = ("Arial", 12, "bold")

        for col, header in enumerate(headers):
            tk.Label(table_frame, text=header, font=header_font, bg="#e6e6e6", fg="#222", padx=15, pady=5).grid(row=0, column=col, sticky="nsew")
        
        # Display account data inside table frame
            accounts = self.controller.fetchAllAccounts()
            row = 1

            for account in accounts:
                tk.Label(table_frame, text=account.id, font=("Arial", 12), bg="#add8e6", padx=15, pady=5).grid(row=row, column=0, sticky="nsew")
                tk.Label(table_frame, text=account.username, font=("Arial", 12), bg="#add8e6", padx=15, pady=5).grid(row=row, column=1, sticky="nsew")
                tk.Label(table_frame, text=account.role, font=("Arial", 12), bg="#add8e6", padx=15, pady=5).grid(row=row, column=2, sticky="nsew")

                # Action buttons in one frame
                action_frame = tk.Frame(table_frame, bg="#add8e6")
                action_frame.grid(row=row, column=3, padx=10, pady=5)

                edit_btn = tk.Button(action_frame, text="Edit", command=dummy, fg="black", font=("Arial", 12, "bold"), width=8, borderwidth=0, cursor="hand2")
                edit_btn.pack(side="left", padx=10)

                suspend_btn = tk.Button(action_frame, text="Suspend", command=self.suspendUserAccount, fg="black", font=("Arial", 12, "bold"), width=8,  borderwidth=0, cursor="hand2")
                suspend_btn.pack(side="left", padx=10)

                row += 1 # Increment for the next account

                # Action Buttons
                button_frame = tk.Frame(self.root)
                button_frame.grid(row=2, column=0, columnspan=5, pady=10)
                
                style_btn = lambda text, cmd, color: tk.Button(button_frame, text=text, command=cmd, bg=color, fg="black", font=("Arial", 12, "bold"), padx=20, pady=5)

            # Back and logout buttons inside the table frame (or you can place them in a separate frame as well)
                style_btn("Back to Dashboard", self.displayAdminPage, "#607d8b").grid(row=0, column=0, padx=10)
                style_btn("View Profiles", self.openManageProfiles, "#3f51b5").grid(row=0, column=1, padx=10)
                style_btn("Add Account", dummy, "#009688").grid(row=0, column=2, padx=10)

    def suspendUserAccount(self):
        # Create popup window
        popup = tk.Toplevel()
        popup.title("Suspend Account")
        popup.geometry("400x200")
        popup.configure(bg="white")
        popup.resizable(False, False)

        # Center the window on screen
        popup.update_idletasks()
        width = popup.winfo_width()
        height = popup.winfo_height()
        x = (popup.winfo_screenwidth() // 2) - (width // 2)
        y = (popup.winfo_screenheight() // 2) - (height // 2)
        popup.geometry(f"+{x}+{y}")

        # Border frame
        border = tk.Frame(popup, bg="#add8e6", padx=1, pady=1)
        border.pack(expand=True, fill="both", padx=30, pady=30)

        # Inner frame
        inner = tk.Frame(border, bg="#add8e6")
        inner.pack(expand=True, fill="both", padx=20, pady=20)

        # Message
        tk.Label(inner, text="Are you sure you want to suspend this user?", font=("Arial", 12, "bold"), bg="#add8e6").pack(pady=(5, 20))

        # Buttons
        button_frame = tk.Frame(inner, bg="#add8e6")
        button_frame.pack()

        # Cancel button with styling
        cancel_btn = tk.Button(button_frame, text="Cancel", width=10, command=popup.destroy, bg="#add8e6", highlightbackground="#add8e6", activebackground="#8fc5d8", relief="flat")
        cancel_btn.pack(side="left", padx=10)
        
        def handle_suspend():
            popup.destroy()
            messagebox.showinfo("Success", "User account has been suspended.")

        # Suspend button with styling
        suspend_btn = tk.Button(button_frame, text="Suspend", width=10, command=handle_suspend, bg="#add8e6", highlightbackground="#add8e6", activebackground="#8fc5d8", relief="flat")
        suspend_btn.pack(side="left", padx=10)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
    
    # Opens the Accounts page
    def openManageProfiles(self):
        self.displayProfilesPage()

    def displayProfilesPage(self):
        self.controller = controller.ViewProfileController()

        # Clear the existing window
        for widget in self.root.winfo_children():
            widget.destroy()

    # Set background color
        self.root.configure(bg="#f0f2f5")

    # Frame for the title
        title_frame = tk.Frame(self.root, bg="#f0f2f5")
        title_frame.grid(row=0, column=0, columnspan=5, pady=30)

    # Title Label inside the title frame
        tk.Label(title_frame, text="User Profiles", font=("Arial", 24, "bold"), bg="#f0f2f5", fg="#333").grid(row=0, column=0, padx=200)

    # Frame for the account table
        table_frame = tk.Frame(self.root, bg="#add8e6")
        table_frame.grid(row=1, column=0, columnspan=4, padx=30, pady=10, sticky="nsew")

    # Table Headers inside table frame
        headers = ["Role ID", "Role Name", "Status", "Actions"]
        header_font = ("Arial", 12, "bold")

        for col, header in enumerate(headers):
            tk.Label(table_frame, text=header, font=header_font, bg="#e6e6e6", fg="#222", padx=15, pady=5).grid(row=0, column=col, sticky="nsew")

        # Display profile data inside table frame
        profiles = self.controller.fetchAllProfiles()
        row = 1

        for profile in profiles:
            tk.Label(table_frame, text=profile.role_id, font=("Arial", 12), bg="#add8e6", padx=15, pady=5).grid(row=row, column=0, sticky="nsew")
            tk.Label(table_frame, text=profile.role, font=("Arial", 12), bg="#add8e6", padx=15, pady=5).grid(row=row, column=1, sticky="nsew")
            tk.Label(table_frame, text=profile.suspended, font=("Arial", 12), bg="#add8e6", padx=15, pady=5).grid(row=row, column=2, sticky="nsew")

            # Action buttons in one frame
            action_frame = tk.Frame(table_frame, bg="#add8e6")
            action_frame.grid(row=row, column=3, padx=10, pady=5)

            edit_btn = tk.Button(action_frame, text="Edit", command=dummy, fg="black", font=("Arial", 12, "bold"), width=8, bg="#add8e6", activebackground="#add8e6", borderwidth=0, relief="flat", cursor="hand2")
            edit_btn.pack(side="left", padx=10)

            suspend_btn = tk.Button(action_frame, text="Suspend", command=self.suspendUserProfile, fg="black", font=("Arial", 12, "bold"), width=8, bg="#add8e6", activebackground="#add8e6", borderwidth=0, relief="flat", cursor="hand2")
            suspend_btn.pack(side="left", padx=10)

            row += 1  # Move to next profile

        # Back and logout buttons inside the table frame (or you can place them in a separate frame as well)
        button_frame = tk.Frame(self.root, bg="#f0f2f5")
        button_frame.grid(row=2, column=0, columnspan=5, pady=10)

        style_btn = lambda text, cmd, color: tk.Button(button_frame, text=text, command=cmd, bg=color, fg="black", font=("Arial", 12, "bold"), padx=20, pady=5)

        style_btn("Back to Dashboard", self.displayAdminPage, "#607d8b").grid(row=0, column=0, padx=10)
        style_btn("View Accounts", self.openManageAccounts, "#3f51b5").grid(row=0, column=1, padx=10)
        style_btn("Add Profile", dummy, "#009688").grid(row=0, column=2, padx=10)

    def suspendUserProfile(self):
        # Create popup window
        popup = tk.Toplevel()
        popup.title("Suspend User Profile")
        popup.geometry("400x200")
        popup.configure(bg="white")
        popup.resizable(False, False)

        # Center the window on screen
        popup.update_idletasks()
        width = popup.winfo_width()
        height = popup.winfo_height()
        x = (popup.winfo_screenwidth() // 2) - (width // 2)
        y = (popup.winfo_screenheight() // 2) - (height // 2)
        popup.geometry(f"+{x}+{y}")

        # Border frame
        border = tk.Frame(popup, bg="#add8e6", padx=1, pady=1)
        border.pack(expand=True, fill="both", padx=30, pady=30)

        # Inner frame
        inner = tk.Frame(border, bg="#add8e6")
        inner.pack(expand=True, fill="both", padx=20, pady=20)

        # Message
        tk.Label(inner, text="Are you sure you want to suspend this user profile?", font=("Arial", 12, "bold"), bg="#add8e6").pack(pady=(5, 20))

        # Buttons
        button_frame = tk.Frame(inner, bg="#add8e6")
        button_frame.pack()

        # Cancel button with styling
        cancel_btn = tk.Button(button_frame, text="Cancel", width=10, command=popup.destroy, bg="#add8e6", highlightbackground="#add8e6", activebackground="#8fc5d8", relief="flat")
        cancel_btn.pack(side="left", padx=10)
        
        def handle_suspend():
            popup.destroy()
            messagebox.showinfo("Success", "User profile has been suspended.")

        # Suspend button with styling
        suspend_btn = tk.Button(button_frame, text="Suspend", width=10, command=handle_suspend, bg="#add8e6", highlightbackground="#add8e6", activebackground="#8fc5d8", relief="flat")
        suspend_btn.pack(side="left", padx=10)

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