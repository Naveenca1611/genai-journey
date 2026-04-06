import json

filename = "user_data.json"

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
    except:
        users = []

    users.append(user)

    with open(filename, "w") as file:
        json.dump(users, file, indent=4)

    print("\nUser added successfully\n")

def view_users():
    try:
        with open(filename, "r") as file:
            users = json.load(file)

        print("\n--- Stored Users ---\n")

        for user in users:
            print(f"{user['name']} | {user['role']} | {user['age']}")
    except:
        print("\nNo data found.\n")

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

    except:
        print("\nNo data found.")

def delete_user():
    name = input("Enter name to delete: ")

    try:
        with open(filename, "r") as file:
            users = json.load(file)

        new_users = [user for user in users if user['name'].lower() != name.lower()]

        with open(filename, "w") as file:
            json.dump(new_users, file, indent=4)

        print("\nUser deleted (if existed).")

    except:
        print("\nNo data found.")

while True:
    print("\n1. Add Users")
    print("2. View Users")
    print("3. Search User")
    print("4. Delete User")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_user()
    elif choice == "2":
        view_users()
    elif choice == "3":
        search_user()
    elif choice == "4":
        delete_user()
    elif choice == "5":
        break
    else:
        print("Invalid choice!")
    
