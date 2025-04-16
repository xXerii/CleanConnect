import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox, filedialog

# Please use this dummy function as placeholder for the buttons if needed
def dummy():
    messagebox.showinfo("Clicked", "Feature coming soon.")

# ADMIN PAGE
class AdminPage:
    def __init__(self, root):
        self.root = root
        #self.user = user
        # Create ViewAccounts controller instance
        self.displayAdminPage()

    def displayAdminPage(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        Label(self.root, text=f"Admin Dashboard", font=("Arial", 24)).pack(pady=30)
        Label(self.root, text=f"Welcome, Test").pack(pady=10)
        Label(self.root, text=f"Role ID: 1").pack(pady=5)

        # Add Admin features here
        Button(self.root, text="View Reports", command=dummy).pack(pady=5)
        Button(self.root, text="Manage Users", command=self.openManageAccounts).pack(pady=5)

        Button(self.root, text="Logout", command=self.logout).pack(pady=20)

    def displayCreateAccountForm(self):
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

        # Submit button
        def submit():
            name = name_entry.get()
            username = username_entry.get()
            password = password_entry.get()
            confirm = confirm_password_entry.get()
            email = email_entry.get()

            if password != confirm:
                messagebox.showerror("Error", "Passwords do not match.")
                return

            # Controller: Return Data
            messagebox.showinfo("Success", f"Account for {username} created successfully!")

        Button(self.root, text="Submit", command=submit).pack(pady=10)
        Button(self.root, text="Back", command=self.displayAccountsPage).pack(pady=5)

    def displayUpdateAccountForm(self, user_data):
        for widget in self.root.winfo_children():
            widget.destroy()

        Label(self.root, text="Update Account", font=("Arial", 24)).pack(pady=20)

        form_frame = Frame(self.root)
        form_frame.pack(pady=10)

        # Input fields
        Label(form_frame, text="Name").grid(row=0, column=0, sticky='e', padx=5, pady=5)
        name_entry = Entry(form_frame)
        name_entry.insert(0, user_data.get("name", ""))
        name_entry.grid(row=0, column=1, padx=5, pady=5)

        Label(form_frame, text="Username").grid(row=1, column=0, sticky='e', padx=5, pady=5)
        username_entry = Entry(form_frame)
        username_entry.insert(0, user_data.get("username", ""))
        username_entry.grid(row=1, column=1, padx=5, pady=5)

        Label(form_frame, text="New Password").grid(row=2, column=0, sticky='e', padx=5, pady=5)
        password_entry = Entry(form_frame, show="*")
        password_entry.grid(row=2, column=1, padx=5, pady=5)

        Label(form_frame, text="Confirm Password").grid(row=3, column=0, sticky='e', padx=5, pady=5)
        confirm_password_entry = Entry(form_frame, show="*")
        confirm_password_entry.grid(row=3, column=1, padx=5, pady=5)

        Label(form_frame, text="Email").grid(row=4, column=0, sticky='e', padx=5, pady=5)
        email_entry = Entry(form_frame)
        email_entry.insert(0, user_data.get("email", ""))
        email_entry.grid(row=4, column=1, padx=5, pady=5)

        # Submit button logic
        def submit_update():
            name = name_entry.get()
            username = username_entry.get()
            password = password_entry.get()
            confirm = confirm_password_entry.get()
            email = email_entry.get()

            if password != confirm:
                messagebox.showerror("Error", "Passwords do not match.")
                return

            # Example: self.controller.updateAccount(user_id, name, username, password, email)
            messagebox.showinfo("Success", f"Account '{username}' updated successfully!")

        Button(self.root, text="Update", command=submit_update).pack(pady=10)
        Button(self.root, text="Back", command=self.displayAccountsPage).pack(pady=5)

    # Opens the Accounts page
    def openManageAccounts(self):
        self.displayAccountsPage()
    
    def displayAccountsPage(self):
        # self.controller = controller.ViewAccountsController()
        # Set up the accounts display UI
        for widget in self.root.winfo_children():
            widget.destroy()
         # Frame for the title
        title_frame = tk.Frame(self.root)
        title_frame.grid(row=0, column=0, columnspan=5, pady=30)  # Title section in grid (row 0)

    # Title Label inside the title frame
        tk.Label(title_frame, text="User Accounts", font=("Arial", 24)).grid(row=0, column=0, padx=200)

    # Frame for the account table
        table_frame = tk.Frame(self.root)
        table_frame.grid(row=1, column=0, columnspan=5, pady=10)  # Table section in grid (row 1)

    # Table Headers inside table frame
        headers = ["User ID", "Username", "Role", "Actions"]
        for col, header in enumerate(headers):
            tk.Label(table_frame, text=header, font=("Arial", 12, "bold")).grid(row=0, column=col, padx=15, pady=5)

    
        row = 1  # Start placing accounts from the second row
        
        
        # Back and logout buttons inside the table frame
        tk.Button(table_frame, text="Back to Dashboard", command=self.displayAdminPage).grid(row=row, column=0, padx=10, pady=10)
        tk.Button(table_frame, text="View Profiles", command=self.openManageProfiles).grid(row=row, column=1, padx=10, pady=10)
        tk.Button(table_frame, text="Add Account", command=self.displayCreateAccountForm).grid(row=row, column=2, padx=10, pady=10)  # Add Account in column 2
        tk.Button(table_frame, text="Update Account", command=lambda: self.displayUpdateAccountForm(user_data = {
            "name": "Alice",
            "username": "alice123",
            "email": "alice@example.com"
        })).grid(row=row, column=3, padx=10, pady=10)  # Move Update Account to column 3

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
    
    # Opens the Accounts page
    def openManageProfiles(self):
        self.displayProfilesPage()

    def displayProfilesPage(self):
        # self.controller = controller.ViewProfileController()
        # Set up the accounts display UI
        for widget in self.root.winfo_children():
            widget.destroy()
         # Frame for the title
        title_frame = tk.Frame(self.root)
        title_frame.grid(row=0, column=0, columnspan=5, pady=30)  # Title section in grid (row 0)

    # Title Label inside the title frame
        tk.Label(title_frame, text="User Profiles", font=("Arial", 24)).grid(row=0, column=0, padx=200)

    # Frame for the account table
        table_frame = tk.Frame(self.root)
        table_frame.grid(row=1, column=0, columnspan=5, pady=10)  # Table section in grid (row 1)

    # Table Headers inside table frame
        headers = ["Role ID", "Role Name","Status","Actions"]
        for col, header in enumerate(headers):
            tk.Label(table_frame, text=header, font=("Arial", 12, "bold")).grid(row=0, column=col, padx=15, pady=5)

        row = 1  # Start placing accounts from the second row

    # Back and logout buttons inside the table frame (or you can place them in a separate frame as well)
        tk.Button(table_frame, text="Back to Dashboard ", command=self.displayAdminPage).grid(row=row, column=0, padx=10, pady=10)
        tk.Button(table_frame, text="View Accounts", command=self.openManageAccounts).grid(row=row, column=1, padx=10, pady=10)
        tk.Button(table_frame, text="Add Profile", command=dummy).grid(row=row, column=2, padx=10, pady=10) # THIS IS THE ADD Profile BUTTON (Funtion goes after command)
        

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
    AdminPage(window)
    window.mainloop()

if __name__ == '__main__':
    page()
