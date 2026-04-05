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
        print(f"\nNo data found.\n")

while True:
    print("\n1. Add Users")
    print("2. View Users")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_user()
    elif choice == "2":
        view_users()
    elif choice == "3":
        print("Exiting...")
        break
    else:
        print("Invalid choice!")
    
