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
        

    # Back and logout buttons inside the table frame (or you can place them in a separate frame as well)
        tk.Button(table_frame, text="Back to Dashboard", command=self.displayAdminPage).grid(row=row, column=0, padx=10, pady=10)
        tk.Button(table_frame, text="View Profiles", command=self.openManageProfiles).grid(row=row, column=1, padx=10, pady=10)
        tk.Button(table_frame, text="Add Account", command=dummy).grid(row=row, column=2, padx=10, pady=10) # THIS IS THE ADD ACCOUNT BUTTON (Funtion goes after command)

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
