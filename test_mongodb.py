import pymongo

# Check connection by printing databases
def test_conn(db_list) :
    if db_list:
        print("Connected successfully!")
        print("Databases:", db_list)
    else:
        print("No databases found or failed to connect.")

def get_data(client,db,collection):
    documents = collection.find()
    # Print the documents
    for i in documents:
        print(i)

def put_data(client,db,collection):
    documents_to_insert = [
        {"name": "John Doe", "age": 30, "city": "New York"},
        {"name": "Jane Smith", "age": 25, "city": "London"},
        {"name": "Alice Johnson", "age": 35, "city": "Paris"},
        {"name": "Bob Brown", "age": 40, "city": "Berlin"}
    ]

    # Insert multiple documents into the collection
    insert_result = collection.insert_many(documents_to_insert)
    print(f"Data inserted with IDs: {insert_result.inserted_ids}")
    
if __name__ == "__main__" :
    client = pymongo.MongoClient('mongodb://localhost:27017')
    # List databases
    db_list = client.list_database_names()
    db = client['test_db']
    collection = db['collection']
    test_conn(db_list)
    get_data(client,db,collection)
    put_data(client,db,collection)
