import os
import requests

ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
USERNAME = "BALADURGAG24"  # Replace with your GitHub username

headers = {
    "Authorization": f"token {ACCESS_TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}

# Fetch user profile data
response = requests.get(f"https://api.github.com/users/{USERNAME}", headers=headers)
data = response.json()

# ✅ Create the directory if it doesn't exist
os.makedirs("generated", exist_ok=True)

# Save data to a file
with open("generated/overview.txt", "w") as f:
    f.write(str(data))

print("GitHub user data saved to generated/overview.txt")
