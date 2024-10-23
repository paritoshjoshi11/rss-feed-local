import json
import time
from pymongo import MongoClient
from requests_sse import EventSource

def listen_to_firehose(url, mongo_uri, db_name, collection_name):
    # Set up MongoDB connection
    client = MongoClient(mongo_uri)
    db = client[db_name]
    collection = db[collection_name]

    with EventSource(url) as event_source:
        print("Listening for events...")
        for event in event_source:
            # Each event is a string in JSON format
            data = json.loads(event.data)
            print("Received data:", data)  # Process the data as needed
            
            # Write the data to MongoDB
            collection.insert_one(data)
            print("Data inserted into MongoDB.")

            # Sleep for 60 seconds before processing the next event
            #time.sleep(3)

if __name__ == "__main__":
    firehose_url = 'http://github-firehose.libraries.io/events'
    mongo_uri = 'mongodb://localhost:27017'  # Adjust this to your MongoDB URI
    db_name = 'test_db'                    # Replace with your database name
    collection_name = 'github_event'          # Replace with your collection name
    try :
        listen_to_firehose(firehose_url, mongo_uri, db_name, collection_name)
    except KeyboardInterrupt :
        pass
