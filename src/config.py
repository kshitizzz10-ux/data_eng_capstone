import os
from dotenv import load_dotenv

# Load the environment variables from the .env file
load_dotenv()

# Fetch the API key
API_KEY = os.getenv("API_KEY")

# Print it out to test if it worked (We will remove this print statement later for security!)
if __name__ == "__main__":
    if API_KEY:
        print(f"Success! Loaded API Key: {API_KEY}")
    else:
        print("Error: API Key not found. Check your .env file.")