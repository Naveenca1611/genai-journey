users = []

for i in range(2):
    print(f"\nEnter details for Users {i+1}")

    name = input("Name: ")
    role = input("Role: ")
    age = input("Age: ")

    user = {
        "name": name,
        "role": role,
        "age": age
    }

    users.append(user)

print("\n--- All Users ---")

for user in users:
    print(f"{user['name']} | {user['role']} | {user['age']}")
