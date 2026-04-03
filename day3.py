import requests

url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url)

data = response.json()

print("\n--- Users Data from API ---\n")

for user in data[:3]:  # first 3 users
    print(f"Name: {user['name']}")
    print(f"Email: {user['email']}")
    print("-" * 30)
