# --------------------------------------------------------------------------------------------------
# Libraries

# GUI Libraries
import tkinter as tk
from tkinter import simpledialog, messagebox

# Other Libraries...
from pymongo import MongoClient  # pymongo kütüphanesini ekledik

client = MongoClient("mongodb+srv://selenaybuse09:01032002@cluster0.mjnpjnq.mongodb.net/test")
db = client["306"]

collection_names = db.list_collection_names()
collections = {collection_name: list(db[collection_name].find()) for collection_name in collection_names}

# --------------------------------------------------------------------------------------------------


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

        self.options_label = tk.Label(master, text="\nPlease pick the option that you want to proceed.", bg="white",
                                      fg="black")
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

        self.selected_option_button = tk.Button(master, text="Select Option", command=self.select_option, bg="white",
                                                fg="black")
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

    # ----------------------------------------------
    # 1- Create a collection.

    def create_collection(self, mongodb=None):
        new_collection_name = input("Please enter the collection name you want to use: ")

        if new_collection_name in collection_names:
            print("Name already exists.")

        else:

            attributes = []
            response = input("Please enter the attributes in the collection (Enter 0 to exit): ")
            attributes.append(response)
            while response != "0":
                response = input("Please enter the attributes in the collection (Enter 0 to exit): ")
                if response != "0":
                    attributes.append(response)

            # print(attributes)
            default_data = {attr: "null" for attr in attributes}
            data ={}

            for attr in attributes:
                value = input(f"Enter the value for '{attr}': ")
                data[attr] = value

            db[new_collection_name].insert_one(data)
            messagebox.showinfo("Collection Created",
                                f"The collection '{new_collection_name}' was successfully created.")

    # ----------------------------------------------
    # 2- Read all data in a collection.

    def read_all_data(self):    # 2. seçeneğe özel MongoDB okuma işlemleri

        # Display available collections
        for idx, collection_name in enumerate(collections.keys(), start=1):
            print(f"{idx} - {collection_name}")

        collection_number = input("Please select the collection you want to read: ")
        collection_index = int(collection_number)

        if 1 <= collection_index <= len(collection_names):

            selected_collection_name = list(collections.keys())[collection_index - 1]
            print("Selected option: ", str(collection_number))

            cursor = db[selected_collection_name].find()

            for data in cursor:
                print(data)

        else:
            messagebox.showwarning("Index Error!","Invalid Collection Number")

    # ----------------------------------------------
    # 3- Read some part of the data while filtering.

    def read_filtered_data(self):

        filter_criteria = {}
        # Display available collections
        for idx, collection_name in enumerate(collections.keys(), start=1):
            print(f"{idx} - {collection_name}")

        collection_number = input("Please select the collection you want to read: ")
        collection_index = int(collection_number)

        if 1 <= collection_index <= len(collection_names):

            selected_collection_name = list(collections.keys())[collection_index - 1]
            print("Selected option: ", str(collection_number))

            while True:
                field_name = input("Enter the criteria you want to filter (or press Enter to finish): ")
                if not field_name:
                    break
                field_value = input("Enter field value: ")
                filter_criteria[field_name] = field_value

            cursor = db[selected_collection_name].find(filter_criteria)

            for data in cursor:
                print(data)

        else:
            messagebox.showwarning("Index Error!","Invalid Collection Number")
    # ----------------------------------------------
    # 4- Insert data.
    def insert_data(self):
        # Display available collections
        for idx, collection_name in enumerate(collections.keys(), start=1):
            print(f"{idx} - {collection_name}")

        collection_number = input("Please select the collection you want to insert data: ")
        print("Selected option: ", str(collection_number))

        print("Please enter the data fields: ")
        selected_collection_name = list(collections.keys())[int(collection_number) - 1]
        field_names = list(collections[selected_collection_name][0].keys())
        # print(field_names)

        data = {}

        for field_name in field_names:
            if field_name != "_id":
                field_value = input(f"{field_name}: ")
                data[field_name] = field_value

        # Insert data into MongoDB
        db[selected_collection_name].insert_one(data)
        messagebox.showinfo("Data inserted", "Data was successfully inserted!")
    # ----------------------------------------------
    # 5- Delete data.

    def delete_data(self):
        # Display available collections
        for idx, collection_name in enumerate(collections.keys(), start=1):
            print(f"{idx} - {collection_name}")

        collection_number = input("Please select the collection you want to delete the data from: ")
        print("Selected option: ", str(collection_number))

        print("Please enter the data fields: ")  # modify
        selected_collection_name = list(collections.keys())[int(collection_number) - 1]
        field_names = list(collections[selected_collection_name][0].keys())
        # print(field_names)

        data = {}

        for field_name in field_names:
            if field_name != "_id":
                field_value = input(f"{field_name}: ")
                data[field_name] = field_value

        # Check if data exists in the selected collection
        if db[selected_collection_name].count_documents(data) > 0:
            # Delete data from MongoDB
            db[selected_collection_name].delete_one(data)
            messagebox.showinfo("Data deleted", "Data was successfully deleted!")
        else:
            messagebox.showwarning("Invalid data", "No such data found in the collection.")

    # ----------------------------------------------
    # 6- Update data.
    def update_data(self):
        # Display available collections
        for idx, collection_name in enumerate(collections.keys(), start=1):
            print(f"{idx} - {collection_name}")

        collection_number = input("Enter the collection you want to update: ")
        print("Selected option: ", collection_number)
        print("Please enter the original data fields you want to update: ")

        selected_collection_name = list(collections.keys())[int(collection_number) - 1]
        field_names = list(collections[selected_collection_name][0].keys())
        # print(field_names)

        original_data = {}

        for field_name in field_names:
            if field_name != "_id":
                field_value = input(f"{field_name}: ")
                original_data[field_name] = field_value

        if db[selected_collection_name].find_one(original_data):
            print("Please enter the new data fields: ")

            new_data = {}

            for field_name in field_names:
                if field_name != "_id":
                    field_value = input(f"{field_name}: ")
                    new_data[field_name] = field_value

            db[selected_collection_name].update_one(original_data, {"$set": new_data})
            messagebox.showinfo("Data updated", "Data was successfully updated!")

        else:
            messagebox.showwarning("Update error", "No such data was found!")


# ----------------------------------------------

# --------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    root = tk.Tk()
    app = ReviewPortalGUI(root)
    root.mainloop()