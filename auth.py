import json

def register_user():
    """
    Registers a new user by collecting user details,
    checking for duplicate phone numbers, and saving
    the user's information to the JSON database.
    """
    name = input("Enter Your Name: ")
    phone_number = input("Enter Your Phone Number: ")
    password = input("Create a Password: ")

    with open("data/users.json", "r") as file:
        users = json.load(file)
    for user in users:
        if user["phone"] == phone_number:
            print("Phone number already registered. Please sign in or use another phone number.")
            return

    new_user = {
        "name": name,
        "phone": phone_number,
        "password": password
    }

    users.append(new_user)

    with open("data/users.json", "w") as file:
        json.dump(users, file, indent=4)

    print("User registered successfully.")


def login_user():
    """
    Authenticates an existing user using phone number
    and password. Returns the logged-in user's data
    if the credentials are valid.
    """
    phone_number = input("Enter phone number: ")
    password = input("Enter your password: ")
    
    with open("data/users.json", "r") as file:
        users = json.load(file)
    
    for user in users:
        if user["phone"] == phone_number and user["password"] == password:
            print(f"\nWelcome back, {user['name']}!")
            return user
        
    print("Invalid Credentials")