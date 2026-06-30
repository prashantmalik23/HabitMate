# 📝 HabitTracker

A command-line based Habit Tracker application built with **Python** that helps users create, manage, and track their daily habits. The application stores user and habit data using **JSON**, maintains daily progress history, and provides the foundation for reports, streak tracking, and productivity analytics.

This project is being developed as a long-term portfolio project to demonstrate software engineering principles, clean architecture, Object-Oriented Programming (OOP), file handling, and modular Python development.

---

## 🚀 Features

### User Management

* User Registration
* User Login
* Input Validation
* Persistent User Data (JSON)

### Habit Management

* Add New Habit
* View Habits
* Delete Habit (Soft Delete)
* Habit Categories
* Daily/Weekly Habit Frequency

### Progress Tracking

* Mark Habit as Completed
* Daily Progress History
* Completion Date & Time Tracking

### Upcoming Features

* Edit Habit
* Weekly Reports
* Monthly Reports
* Habit Streak Calculation
* Productivity Analytics
* Graphical Reports
* Password Hashing
* SQLite Database Support
* GUI / Web Version

---

## 🛠️ Technologies Used

* Python 3
* Object-Oriented Programming (OOP)
* JSON
* File Handling
* Git & GitHub

---

## 📁 Project Structure

```text
HabitTracker/
│
├── main.py
├── config.py
├── README.md
├── requirements.txt
├── .gitignore
│
├── data/
│   ├── users.json
│   ├── habits.json
│   └── progress.json
│
├── models/
│   ├── user.py
│   ├── habit.py
│   └── progress.py
│
├── services/
│   ├── auth_service.py
│   ├── habit_service.py
│   └── progress_service.py
│
├── utils/
│   ├── file_handler.py
│   └── validation.py
│
├── reports/
│
└── assets/
```

---

## ▶️ Getting Started

### Clone the Repository

```bash
git clone https://github.com/your-username/HabitTracker.git
```

### Move to the Project Folder

```bash
cd HabitTracker
```

### Run the Project

```bash
python main.py
```

---

## 📌 Current Development Status

* ✅ User Authentication
* ✅ Habit Management
* ✅ Daily Progress Tracking
* 🚧 Reports (In Progress)
* 🚧 Streak System (Planned)
* 🚧 Analytics Dashboard (Planned)

---

## 🎯 Learning Objectives

This project demonstrates:

* Clean Project Architecture
* Modular Programming
* Object-Oriented Programming
* JSON File Handling
* Python Best Practices
* Separation of Concerns
* Git Version Control
* Software Design Principles

---

## 📈 Future Improvements

* SQLite Database Integration
* Password Encryption
* Habit Reminders
* Email Notifications
* Export Reports (PDF/CSV)
* Graphs & Charts
* Desktop GUI (CustomTkinter)
* Web Application (Flask)
* REST API
* Unit Testing

---

## 👨‍💻 Author

**Prashant Malik**

B.Tech Computer Science Student

This project is part of my software development portfolio and is being continuously improved as I learn new technologies and best practices.
