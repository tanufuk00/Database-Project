import json
from pymongo import MongoClient

# Connect to MongoDB Atlas
client = MongoClient("mongodb+srv://selenaybuse09:01032002@cluster0.mjnpjnq.mongodb.net/test")
db = client["306"]

collection_names = db.list_collection_names()
collections = {collection_name: list(db[collection_name].find()) for collection_name in collection_names}


# print(collections)


def insert_data():
    # Display available collections
    for idx, collection_name in enumerate(collections.keys(), start=1):
        print(f"{idx} - {collection_name}")

    collection_number = input("Please select the collection you want to insert data: ")
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

    # Insert data into MongoDB
    db[selected_collection_name].insert_one(data)
    print("Data was successfully inserted!")


if __name__ == "__main__":
    # Assume you have some collections already defined in 'collections' variable
    # e.g., collections = {'Film Reviews': [{'name': '...', 'review_message': '...', 'given_star': 5}], ...}

    # Run the event loop
    insert_data()
