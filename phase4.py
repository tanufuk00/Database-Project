#--------------------------------------------------------------------------------------------------
#Libraries

#GUI Libraries
import tkinter as tk
from tkinter import simpledialog, messagebox

#Other Libraries...


#--------------------------------------------------------------------------------------------------

class ReviewPortalGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Review Portal")
        self.master.configure(bg="white")

        self.welcome_label = tk.Label(master, text="Welcome to Review Portal!\n", bg="white", fg="black")
        self.welcome_label.pack()

        self.user_id_label = tk.Label(master, text="Please enter your user id:", bg="white", fg="black")
        self.user_id_label.pack()

        self.user_id_entry = tk.Entry(master, bg="white", fg="black", bd=1, relief="solid")
        self.user_id_entry.pack()

        self.options_label = tk.Label(master, text="\nPlease pick the option that you want to proceed.", bg="white", fg="black")
        self.options_label.pack()

        options = [
            "1- Create a collection.",
            "2- Read all data in a collection.",
            "3- Read some part of the data while filtering.",
            "4- Insert data.",
            "5- Delete data.",
            "6- Update data.\n"
        ]

        for option in options:
            tk.Label(master, text=option, bg="white", fg="black").pack()

        self.selected_option_label = tk.Label(master, text="Selected option:", bg="white", fg="black")
        self.selected_option_label.pack()

        self.selected_option_entry = tk.Entry(master, bg="white", fg="black", bd=1, relief="solid")
        self.selected_option_entry.pack()

        self.selected_option_button = tk.Button(master, text="Select Option", command=self.select_option, bg="white", fg="black")
        self.selected_option_button.pack()

    def select_option(self):
        selected_option = self.selected_option_entry.get()

        if selected_option.isdigit():
            selected_option = int(selected_option)

            if 1 <= selected_option <= 6:
                if selected_option == 1:
                    self.create_collection()
                elif selected_option == 2:
                    self.read_all_data()
                elif selected_option == 3:
                    self.read_filtered_data()
                elif selected_option == 4:
                    self.insert_data()
                elif selected_option == 5:
                    self.delete_data()
                elif selected_option == 6:
                    self.update_data()
            else:
                messagebox.showwarning("Invalid Option", "Please enter a valid option (1-6).")
        else:
            messagebox.showwarning("Invalid Input", "Please enter a numeric option.")

#----------------------------------------------
    def create_collection(self):
        messagebox.showinfo("Create Collection", "You selected option 1. Performing 'Create a collection' operation.")

#----------------------------------------------
    def read_all_data(self):
        messagebox.showinfo("Read All Data", "You selected option 2. Performing 'Read all data in a collection' operation.")

#----------------------------------------------
    def read_filtered_data(self):
        messagebox.showinfo("Read Filtered Data", "You selected option 3. Performing 'Read some part of the data while filtering' operation.")

#----------------------------------------------
    def insert_data(self):
        messagebox.showinfo("Insert Data", "You selected option 4. Performing 'Insert data' operation.")

#----------------------------------------------
    def delete_data(self):
        messagebox.showinfo("Delete Data", "You selected option 5. Performing 'Delete data' operation.")

#----------------------------------------------
    def update_data(self):
        messagebox.showinfo("Update Data", "You selected option 6. Performing 'Update data' operation.")
#----------------------------------------------
        
#--------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    root = tk.Tk()
    app = ReviewPortalGUI(root)
    root.mainloop()
