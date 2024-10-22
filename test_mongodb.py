import pymongo

client = pymongo.MongoClient('localhost:27017')


# List databases
db_list = client.list_database_names()

# Check connection by printing databases
def main() :
    if db_list:
        print("Connected successfully!")
        print("Databases:", db_list)
    else:
        print("No databases found or failed to connect.")

if __name__ == "__main__" :
    main()
