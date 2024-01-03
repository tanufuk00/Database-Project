#--------------------------------------------------------------------------------------------------
#Libraries

#GUI Libraries
import tkinter as tk
from tkinter import simpledialog, messagebox

#Other Libraries...
from pymongo import MongoClient  # pymongo kütüphanesini ekledik

username = "erselekmen"
password = "VV4J5jV9&q*3XrY"
DATABASE_URL = "mongodb+srv://" + username + ":" + password + "@cluster0.eh8uyv7.mongodb.net/?retryWrites=true&w=majority"



mongodb_client = MongoClient(DATABASE_URL)
mongodb = mongodb_client['cs306']
collections = mongodb['first_collection']


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
    # 1- Create a collection.
    def create_collection(self):
        messagebox.showinfo("Create Collection", "You selected option 1. Performing 'Create a collection' operation.")
        collection_name = 'collection'
        mongodb.create_collection(collection_name)

#----------------------------------------------
    # 2- Read all data in a collection.
    
    '''
    def read_all_data(self):
        # 2. seçeneğe özel MongoDB okuma işlemleri
        client = MongoClient("mongodb://localhost:27017/")  # MongoDB bağlantısı
        db = client["review_portal"]  # Veritabanı seçimi (var olan bir veritabanı adını kullanın veya yeni bir tane oluşturun)
        collection = db["reviews"]  # Koleksiyon seçimi (var olan bir koleksiyon adını kullanın veya yeni bir tane oluşturun)

        # Tüm verileri okuma
        data = collection.find()
        result = ""
        for record in data:
            result += f"Name: {record['name']}, Review: {record['review_message']}, Rating: {record['given_star']}\n"
        
        messagebox.showinfo("Read All Data", result)
    '''

#----------------------------------------------
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

#----------------------------------------------
    # 4- Insert data.
    def insert_data(self):
        messagebox.showinfo("Insert Data", "You selected option 4. Performing 'Insert data' operation.")

#----------------------------------------------
    # 5- Delete data.
    def delete_data(self):
        messagebox.showinfo("Delete Data", "You selected option 5. Performing 'Delete data' operation.")

#----------------------------------------------
    # 6- Update data.
    def update_data(self):
        messagebox.showinfo("Update Data", "You selected option 6. Performing 'Update data' operation.")
#----------------------------------------------
        
#--------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    root = tk.Tk()
    app = ReviewPortalGUI(root)
    root.mainloop()
