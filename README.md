# Library Management System

![License](https://img.shields.io/badge/license-MIT-blue.svg)

This lightweight Library Management System is built with Django, providing efficient management of books, borrowers, and library resources. This system is designed to streamline library operations, allowing librarians to manage books, borrowers, and book loans effectively.

## Team Members

### Ahmed Magdy

- GitHub: [Ahmed Magdy](https://github.com/AhmedMagdy98)
- LinkedIn: [Ahmed Magdy](https://www.linkedin.com/in/ahmed-magdy-282838189/)

### Zeyad Slama

- GitHub: [Zeyad Slama](https://github.com/ZeyadSlama)
- LinkedIn: [Zeyad Slama](https://www.linkedin.com/in/zeyadslama/)

## Features

- **Book Management:** Add, edit, and remove books from the library inventory.
- **Borrower Management:** Manage borrower information and track their borrowing history.
- **Book Loan Tracking:** Keep track of book loans, including issue and return dates.
- **User Authentication:** Secure login and registration system for librarians and borrowers.
- **User Roles:** Distinct roles for librarians and borrowers with specific permissions.

## Getting Started

To set up and run this Library Management System locally, follow these steps:

1. **Clone the repository:**

   ```
   bash
   git clone https://github.com/Demo-23home/ITI_Final-Library_Managemet_System.git
   cd ITI_Final-Library_Managemet_System
   ```
2.Create a virtual environment and install dependencies:
```
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
pip install -r requirements.txt
```
3.Apply migrations and create a superuser:
```
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```
4.Access the admin panel at: http://localhost:8000/admin/ and the Library Management System at http://localhost:8000/

5.Usage
Librarian: Log in to the admin panel to manage books, borrowers, and book loans.
Borrower: Log in to the Library Management System to borrow and return books.
Contributing
If you'd like to contribute to this project, please follow our contribution guidelines.

6.License
This project is licensed under the MIT License.



