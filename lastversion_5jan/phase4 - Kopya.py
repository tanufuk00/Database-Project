# --------------------------------------------------------------------------------------------------
# Libraries

# GUI Libraries
import tkinter as tk
from tkinter import simpledialog, messagebox

# Other Libraries...
from pymongo import MongoClient  # pymongo kütüphanesini ekledik

client = MongoClient("mongodb://localhost:27017")
db = client["database"]

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
        new_collection_name = simpledialog.askstring("New Collection", "Please enter the collection name you want to use:")

        if new_collection_name in collection_names:
            messagebox.showwarning("Warning", "Name already exists.")
            return

        attributes = []
        while True:
            response = simpledialog.askstring("Attributes", "Please enter the attributes in the collection (Enter 0 to exit):")
            if response == "0":
                break
            if response:  # Make sure it's not an empty string
                attributes.append(response)

        if not attributes:
            messagebox.showwarning("Warning", "No attributes provided.")
            return

        data = {}
        for attr in attributes:
            value = simpledialog.askstring("Attribute Value", f"Enter the value for '{attr}':")
            data[attr] = value if value is not None else "null"

        db[new_collection_name].insert_one(data)
        messagebox.showinfo("Collection Created", f"The collection '{new_collection_name}' was successfully created.")

    # ----------------------------------------------
    # 2- Read all data in a collection.

    def read_all_data(self):    # 2. seçeneğe özel MongoDB okuma işlemleri

        for idx, collection_name in enumerate(collections.keys(), start=1):
            print(f"{idx} - {collection_name}")

        collection_to_read = input("Please enter the collection number you want to read: ")

        # Tüm verileri okuma
        data = collection_to_read.find()

        for record in data:
            print(record)

        # messagebox.showinfo("Read All Data", record)

    # ----------------------------------------------
    # 3- Read some part of the data while filtering.

    '''
    def read_filtered_data(self):
        # 3. seçeneğe özel MongoDB filtreli okuma işlemleri
        client = MongoClient("mongodb://localhost:27017/")  # MongoDB bağlantısı
        db = client["review_portal"]  # Veritabanı seçimi (var olan bir veritabanı adını kullanın veya yeni bir tane oluşturun)
        collection = db["reviews"]  # Koleksiyon seçimi (var olan bir koleksiyon adını kullanın veya yeni bir tane oluşturun)

        # Kullanıcıdan filtre terimi al
        filter_term = simpledialog.askstring("Filter Data", "Enter filter term:")

        # Filtrelenmiş verileri okuma
        data = collection.find({"name": {"$regex": filter_term, "$options": "i"}})  # Case-insensitive regex kullanarak filtreleme
        result = ""
        for record in data:
            result += f"Name: {record['name']}, Review: {record['review_message']}, Rating: {record['given_star']}\n"
    '''

    # ----------------------------------------------
    # 4- Insert data.
    def insert_data(self):
        messagebox.showinfo("Insert Data", "You selected option 4. Performing 'Insert data' operation.")
        
        # Display available collections and let user select one
        collection_list = "\n".join([f"{idx} - {name}" for idx, name in enumerate(collections.keys(), start=1)])
        messagebox.showinfo("Available Collections", f"Please select a collection to insert data:\n{collection_list}")
        collection_number = simpledialog.askinteger("Collection Selection", "Enter the collection number:")

        if collection_number is None or collection_number < 1 or collection_number > len(collections):
            messagebox.showwarning("Invalid Selection", "Invalid collection number.")
            return

        selected_collection_name = list(collections.keys())[collection_number - 1]
        field_names = list(collections[selected_collection_name][0].keys())

        data = {}
        for field_name in field_names:
            if field_name != "_id":  # Exclude the '_id' field
                field_value = simpledialog.askstring("Data Entry", f"Enter value for '{field_name}':")
                if field_value is not None:
                    data[field_name] = field_value

        if data:
            db[selected_collection_name].insert_one(data)
            messagebox.showinfo("Data Inserted", "Data was successfully inserted into the collection.")
        else:
            messagebox.showwarning("No Data", "No data was entered.")
    # ----------------------------------------------
    # 5- Delete data.

    def delete_data(self):
        messagebox.showinfo("Delete Data", "You selected option 5. Performing 'Delete data' operation.")
        
        # Display available collections and let user select one
        collection_list = "\n".join([f"{idx} - {name}" for idx, name in enumerate(collections.keys(), start=1)])
        messagebox.showinfo("Available Collections", f"Please select a collection to delete data from:\n{collection_list}")
        collection_number = simpledialog.askinteger("Collection Selection", "Enter the collection number:")

        if collection_number is None or collection_number < 1 or collection_number > len(collections):
            messagebox.showwarning("Invalid Selection", "Invalid collection number.")
            return

        selected_collection_name = list(collections.keys())[collection_number - 1]
        field_names = list(collections[selected_collection_name][0].keys())

        data = {}
        for field_name in field_names:
            if field_name != "_id":  # Exclude the '_id' field
                field_value = simpledialog.askstring("Data Entry", f"Enter value for '{field_name}' to delete:")
                if field_value is not None:
                    data[field_name] = field_value

        # Check if data exists in the selected collection
        if data and db[selected_collection_name].count_documents(data) > 0:
            # Delete data from MongoDB
            db[selected_collection_name].delete_one(data)
            messagebox.showinfo("Data Deleted", "Data was successfully deleted from the collection.")
        else:
            messagebox.showwarning("No Data Found", "No matching data found in the collection.")

    # ----------------------------------------------
    # 6- Update data.
    def update_data(self):
        # Display available collections and let user select one
        collection_list = "\n".join([f"{idx} - {name}" for idx, name in enumerate(collections.keys(), start=1)])
        messagebox.showinfo("Available Collections", f"Please select a collection to update data:\n{collection_list}")
        collection_number = simpledialog.askinteger("Collection Selection", "Enter the collection number:")

        if collection_number is None or collection_number < 1 or collection_number > len(collections):
            messagebox.showwarning("Invalid Selection", "Invalid collection number.")
            return

        selected_collection_name = list(collections.keys())[collection_number - 1]
        field_names = list(collections[selected_collection_name][0].keys())

        # Get original data from the user
        original_data = {}
        for field_name in field_names:
            if field_name != "_id":  # Exclude the '_id' field
                field_value = simpledialog.askstring("Original Data Entry", f"Enter original value for '{field_name}':")
                if field_value is not None:
                    original_data[field_name] = field_value

        # Check if the original data exists
        if db[selected_collection_name].find_one(original_data):
            # Get new data from the user
            new_data = {}
            for field_name in field_names:
                if field_name != "_id":
                    field_value = simpledialog.askstring("New Data Entry", f"Enter new value for '{field_name}':")
                    if field_value is not None:
                        new_data[field_name] = field_value

            # Update data in MongoDB
            db[selected_collection_name].update_one(original_data, {"$set": new_data})
            messagebox.showinfo("Data Updated", "Data was successfully updated in the collection.")
        else:
            messagebox.showwarning("No Data Found", "No matching data found in the collection.")


# ----------------------------------------------

# --------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    root = tk.Tk()
    app = ReviewPortalGUI(root)
    root.mainloop()