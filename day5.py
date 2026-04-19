from ai_log_analyzer import analyze_logs
import json
import requests
import time
import logging

logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def print_line():
    print("=" * 40)

def print_menu():
    print_line()
    print("     USER MANAGEMENT SYSTEM")
    print_line()
    print("1. Add User")
    print("2. View Users")
    print("3. Search User")
    print("4. Delete User")
    print("5. Fetch Users from API")
    print("6. Exit")
    print("7. Analyze Logs")
    print_line()

def pause():
    input("\nPress Enter to continue...")

filename = "users_data.json"


def add_user():
    name = input("Enter Name: ")
    role = input("Enter Role: ")
    age = input("Enter Age: ")

    user = {
        "name": name,
        "role": role,
        "age": age
    }

    try:
        with open(filename, "r") as file:
            users = json.load(file)
    except Exception as e:
        logging.error(f"Error adding user: {str(e)}")
        user = []

    users.append(user)

    with open(filename, "w") as file:
        json.dump(users, file, indent=4)

    print("\nUser added successfully\n")
    logging.info(f"User added: {name}")


def view_users():
    try:
        with open(filename, "r") as file:
            users = json.load(file)

        print("\n--- Stored Users ---\n")

        for i, user in enumerate(users, start=1):
            print(f"{i}. {user['name']} | {user['role']} | {user['age']}")

        print(f"\nTotal Users: {len(users)}")

    except Exception as e:
        logging.error(f"Error reading file: {str(e)}")

    logging.info("Viewed all users")

   
def search_user():
    name = input("Enter name to search: ")

    try:
        with open(filename, "r") as file:
            users = json.load(file)

        found = False

        for user in users:
            if user['name'].lower() == name.lower():
                print(f"\nFound: {user['name']} | {user['role']} | {user['age']}")
                found = True

        if not found:
            print("\nUser not found.")

    except Exception as e:
        logging.error(f"Error searching user: {str(e)}")

    logging.info(f"User searched: {name}")

def delete_user():
    name = input("Enter name to delete: ")

    try:
        with open(filename, "r") as file:
            users = json.load(file)

        new_users = [user for user in users if user['name'].lower() != name.lower()]

        with open(filename, "w") as file:
            json.dump(new_users, file, indent=4)

        print("\nUser deleted (if existed).")

    except Exception as e:
        logging.error(f"Error deleting user: {str(e)}")

    logging.info(f"User deleted: {name}")

def fetch_users_api():
    url = "https://jsonplaceholder.typicode.com/users"

    print("\nFetching data from API...\n")
    time.sleep(1)

    try:
        response = requests.get(url)
        data = response.json()

        print("\n--- Users from API ---\n")

        for user in data[:3]:
            print(f"Name: {user['name']}")
            print(f"Email: {user['email']}")
            print(f"Company: {user['company']['name']}")
            print(f"City: {user['address']['city']}")
            print("-" * 30)

        logging.info("API data fetched successfully")

        # Ask permission
        permission = input("\nDo you want to save these users? (yes/no): ").strip().lower()

        if permission == "yes":
            try:
                with open(filename, "r") as file:
                    users = json.load(file)
            except Exception as e:
                logging.error(f"Error reading file before saving API data: {str(e)}")
                users = []

            # Prevent duplicates & map API data
            for api_user in data[:3]:
                exists = any(u['name'] == api_user['name'] for u in users)

                if not exists:
                    users.append({
                        "name": api_user['name'],
                        "role": api_user['company']['name'],
                        "age": "N/A"
                    })

            with open(filename, "w") as file:
                json.dump(users, file, indent=4)

            print("\nUsers saved successfully!")

        else:
            print("\nUsers not saved.")

    except Exception as e:
        print("\nFailed to fetch data.")
        logging.error(f"API fetch failed: {str(e)}")


# Main loop
while True:
    print_menu()
    choice = input("Enter choice: ")


    if choice == "1":
        add_user()
        pause()
    elif choice == "2":
        view_users()
        pause()
    elif choice == "3":
        search_user()
        pause()
    elif choice == "4":
        delete_user()
        pause()
    elif choice == "5":
        fetch_users_api()
        pause()
    elif choice == "6":
        print("\nThank you for using the app\n")
        break
    elif choice == "7":
        analyze_logs()
        pause()