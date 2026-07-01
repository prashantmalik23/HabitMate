import json

def register_user():
    name = input("Enter Your Name: ")
    phone = input("Enter Your Phone Number: ")
    password = input("Create a Password: ")

    with open("data/users.json", "r") as file:
        users = json.load(file)

    new_user = {
        "name": name,
        "phone": phone,
        "password": password
    }

    users.append(new_user)

    with open("data/users.json", "w") as file:
        json.dump(users, file, indent=4)

    print("User registered successfully.")

register_user()