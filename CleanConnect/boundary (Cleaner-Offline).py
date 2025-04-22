import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox, filedialog

# Please use this dummy function as placeholder for the buttons if needed
def dummy():
    messagebox.showinfo("Clicked", "Feature coming soon.")

# CLEANER PAGE
class CleanerPage:
    def __init__(self, root):
        self.root = root
        #self.user = user
        self.displayCleanerPage()

    def displayCleanerPage(self):
        # Create controller instance
        for widget in self.root.winfo_children():
            widget.destroy()
        

        Label(self.root, text=f"Cleaner Dashboard", font=("Arial", 24)).pack(pady=30)
        Label(self.root, text=f"Welcome, cleaner1").pack(pady=10)
        Label(self.root, text=f"Role ID: 000").pack(pady=5)

        # Add Admin features here
        Button(self.root, text="View Services", command=dummy).pack(pady=5)
        Button(self.root, text="Add Services", command=dummy).pack(pady=5)
        Button(self.root, text="View Interest Metrics", command=dummy).pack(pady=5)

        Button(self.root, text="Logout", command=self.logout).pack(pady=20)
    

    # Please modify this as method as you please 
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

def page():
    window = Tk()
    window.geometry("1280x720")
    window.title('CleanConnect')
    window.minsize(960,540)
    CleanerPage(window)
    window.mainloop()

if __name__ == '__main__':
    page()
