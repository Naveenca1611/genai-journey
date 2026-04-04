import requests
import json

url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url)
data = response.json()

# Save data to file
with open("users.json", "w") as file:
    json.dump(data, file, indent=4)

print("\nData saved to users.json")

# Read data from file
with open("users.json", "r") as file:
    users = json.load(file)

print("\n--- Reading from JSON file ---\n")

for user in users[:3]:
    print(f"Name: {user['name']}")
    print(f"Email: {user['email']}")
    print(f"Company: {user['company']['name']}")
    print(f"City: {user['address']['city']}")
    print("-" * 30)
