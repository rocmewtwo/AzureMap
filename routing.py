import os
from dotenv import load_dotenv
import requests

# Load the environment variables from the .env file
load_dotenv()

# Load the subscription key
subscription_key = os.getenv("AZURE_MAPS_SUBSCRIPTION_KEY")

# Define the start and end points (latitude, longitude)
start_point = (47.6062, -122.3321)  # Example: Seattle, WA
end_point = (47.6205, -122.3493)    # Example: Space Needle, Seattle, WA

# Construct the URL for the Azure Maps Route API
url = f"https://atlas.microsoft.com/route/directions/json?api-version=1.0&subscription-key={
    subscription_key}&query={start_point[0]},{start_point[1]}:{end_point[0]},{end_point[1]}"

# Make the request to the Azure Maps Route API
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    route_data = response.json()
    print("Route data:", route_data)
else:
    print("Error:", response.status_code, response.text)
