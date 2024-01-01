import requests
import pandas as pd
from dotenv import load_dotenv
from pymongo import MongoClient
import os

# Load environment variables from .env file
load_dotenv()

# Access the MongoDB Atlas connection string from environment variables
connection_string = os.getenv("MONGODB_URI")
print(f"Connection string: {connection_string}")

def main():
    api_url = 'https://jsonplaceholder.typicode.com/posts'
    response = requests.get(api_url)
    json_data = 0
    if response.status_code == 200:
        json_data = response.json()
    else:
        print(f"Error: Unable to fetch data from {api_url}")
        return None

    if json_data:
        df = pd.DataFrame(json_data)
        print("DataFrame from JSON data:")
        print(df)


    # Connect to MongoDB Atlas
    client = MongoClient(connection_string)
    db = client.gettingStarted
    collection = db.posts
    # Convert DataFrame to Dictionary
    dictionary_representation = df.to_dict(orient='records')
    # Insert data into MongoDB
    collection.insert_many(dictionary_representation)
    print("Data inserted into MongoDB")
    client.close()


if __name__ == "__main__":
    main()
