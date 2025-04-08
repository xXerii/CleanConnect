import controller
import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox, filedialog

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

        self.controller = controller.UserLoginController()  # create controller instance

        username = self.username_entry.get()
        password = self.password_entry.get()

        user = self.controller.loginAccount(username ,password)


        if user:
            print(f"Role ID: {user.role_id}")
            if user.role_id == 1:
                print ("Role: Admin")
            elif user.role_id == 2:
                print ("Role: Cleaner")
            else:
                print("Role not found")
            
                
            print (f"User ID: {user.id}")
            messagebox.showinfo("Login Successful", f"Welcome {user.username}!")
            # You could navigate to a new page class here
        else:
            messagebox.showerror("Login Failed", "Invalid credentials.")
        


def page():
    window = Tk()
    window.geometry("1280x720")
    window.title('CleanConnect')
    window.minsize(960,540)
    LoginPage(window)
    window.mainloop()

if __name__ == '__main__':
    page()
