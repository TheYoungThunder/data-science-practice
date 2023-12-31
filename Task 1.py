import requests
import pandas as pd

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

if __name__ == "__main__":
    main()
