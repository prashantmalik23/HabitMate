import json
from datetime import date

def add_habit(user):
    """
    Add a new habit for the logged-in user.
    """
    category = None
    while True:
        print("Select Category")
        print("1. Health")
        print("2. Study")
        print("3. Fitness")
        print("4. Work")
        print("5. Personal")
        print("6. Other")
        category_choice = input("Choice: ")
        if category_choice == "1":
            category = "Health"
        elif category_choice == "2":
            category = "Study"
        elif category_choice == "3":
            category = "Fitness"
        elif category_choice == "4":
            category = "Work"
        elif category_choice == "5":
            category = "Personal"
        elif category_choice == "6":
            category = "Other"
        else:
            print("Invalid Input")
            continue
        break

    habit_name = input("Enter Your Habit Name: ")

    with open("data/habits.json", "r") as file:
        habits = json.load(file)

    habit_id = len(habits) + 1

    while True:
        print("\nSelect Frequency")
        print("1. Daily")
        print("2. Weekly")

        choice = input("Choice: ")

        if choice == "1":
            frequency = "Daily"
            break

        elif choice == "2":
            frequency = "Weekly"
            break

        else:
            print("Invalid Choice")
    

    new_habit = {
        "habit_id": habit_id,
        "user_phone": user["phone"],
        "habit_name": habit_name,
        "frequency": frequency,
        "category": category,
        "created_at": str(date.today()),
        "completed_dates": [],
        "streak": 0,
        "status": "Active"
    }
    
    habits.append(new_habit)

    with open("data/habits.json", "w") as file:
        json.dump(habits, file, indent=4)

    print("\nHabit added successfully!")


