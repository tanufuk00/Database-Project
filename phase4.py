import tkinter as tk
from tkinter import simpledialog, messagebox

class ReviewPortalGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Review Portal")
        self.master.configure(bg="white")  # Arkaplan rengini beyaz yapar.

        self.welcome_label = tk.Label(master, text="Welcome to Review Portal!\n", bg="white", fg="black")
        self.welcome_label.pack()

        self.user_id_label = tk.Label(master, text="Please enter your user id:", bg="white", fg="black")
        self.user_id_label.pack()

        self.user_id_entry = tk.Entry(master, bg="white", fg="black", bd=1, relief="solid")  # bd: border width, relief: border style
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
                if selected_option == 4:
                    self.insert_data()
                else:
                    messagebox.showinfo("Selected Option", f"You selected option {selected_option}")
            else:
                messagebox.showwarning("Invalid Option", "Please enter a valid option (1-6).")
        else:
            messagebox.showwarning("Invalid Input", "Please enter a numeric option.")

    def insert_data(self):
        collection = simpledialog.askstring("Insert Data", "Please select the collection you want to insert data:",
                                            parent=self.master)

        if collection:
            self.insert_data_action(collection)
        else:
            messagebox.showwarning("Incomplete Data", "Please provide the collection.")

    def insert_data_action(self, collection):
        messagebox.showinfo("Insert Data", f"You selected option 4. Please select the collection: {collection}")

if __name__ == "__main__":
    root = tk.Tk()
    app = ReviewPortalGUI(root)
    root.mainloop()
