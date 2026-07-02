from auth import register_user, login_user
from dashboard import dashboard
from utils import show_title


def main():
    while True:
        show_title()

        print("1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input("\nEnter Your Choice: ")

        if choice == "1":
            register_user()

        elif choice == "2":
            logged_in_user = login_user()
            if logged_in_user:
                dashboard(logged_in_user)

        elif choice == "3":
            print("\nThank you for using HabitTracker.")
            break

        else:
            print("\nInvalid Choice! Please try again.")

if __name__ == "__main__":
    main()