def dashboard(user):
    """
    Displays the user dashboard after successful login
    and provides options to manage habits or logout.
    """
    while True:
        print("\n========================")
        print(f"Welcome, {user['name']}")
        print("========================")
        print("1. Add Habits")
        print("2. View Habits")
        print("3. Mark Habit Complete")
        print("4. Logout")

        choice = input("\nEnter Your Choice: ")

        if choice == "1":
            print("\nAdd Habit feature is under development.")
        elif choice == "2":
            print("View Habits")
        elif choice == "3":
            print("coming soon...")
        elif choice == "4":
            print("\nLogged out successfully.")
            return 
        else:
            print("\nInvalid Choice! Please try again.")