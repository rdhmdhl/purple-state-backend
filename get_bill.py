from dotenv import load_dotenv
import requests
import xml.etree.ElementTree as ET
import os
load_dotenv()

def get_bill():
    # Replace 'api_key' with your actual API key
    api_key = os.getenv("CONGRESS_API_KEY")
    url = f"https://www.congress.gov/118/bills/hr7521/BILLS-118hr7521ih.xml?api_key={api_key}"
    7521
    # Making the GET request
    response = requests.get(url)

    # Checking if the request was successful
    if response.status_code == 200:
        # If the response is JSON, you might prefer to print it in a more readable format
        try:
            return response.text
        except ValueError:
            print("Response is not in JSON format.")
    else:
        print("Failed to retrieve tree:", response.status_code)
