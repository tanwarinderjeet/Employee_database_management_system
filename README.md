# Employee Management System

A Python-based Employee Management System that performs CRUD (Create, Read, Update, Delete) operations using MySQL.

This is a menu-driven console application developed using Python, Object-Oriented Programming (OOP), MySQL, and SQL. The application allows users to add, view, update, and delete employee records stored in a MySQL database.

## Features

* Add new employees
* View all employees
* Update employee details
* Delete employees
* Salary input validation
* Employee ID validation
* MySQL database integration
* Exception handling
* Menu-driven console interface
* Secure database credentials using environment variables

## Technologies Used

* Python
* Object-Oriented Programming (OOP)
* MySQL
* SQL
* mysql-connector-python
* python-dotenv

## Project Structure

```text
EmployeeManagementSystem/
│
├── main.py
├── employee.py
├── database_operations.py
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

### File Description

| File                     | Description                                                  |
| ------------------------ | ------------------------------------------------------------ |
| `main.py`                | Contains the main menu and handles user input                |
| `employee.py`            | Contains the `Employee` class                                |
| `database_operations.py` | Handles MySQL connection and CRUD operations                 |
| `.env`                   | Stores database credentials locally                          |
| `.gitignore`             | Prevents sensitive and unnecessary files from being uploaded |
| `requirements.txt`       | Contains required Python packages                            |
| `README.md`              | Project documentation                                        |

## Database Setup

Open MySQL Workbench and create the database:

```sql
CREATE DATABASE employee_management;
```

Select the database:

```sql
USE employee_management;
```

Create the `employees` table:

```sql
CREATE TABLE employees (
    employee_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    department VARCHAR(100) NOT NULL,
    salary DECIMAL(10, 2) NOT NULL
);
```

## Environment Variables

The project uses a `.env` file to keep database credentials separate from the source code.

Create a `.env` file in the project root directory:

```text
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=your_mysql_password
DB_NAME=employee_management
```

Replace `your_mysql_password` with your local MySQL password.

**Do not upload the `.env` file to GitHub.**

The `.env` file is included in `.gitignore` to protect database credentials.

## Installation

### 1. Clone the repository

```bash
git clone <your-github-repository-url>
```

### 2. Navigate to the project directory

```bash
cd EmployeeManagementSystem
```

### 3. Install the required packages

```bash
py -m pip install -r requirements.txt
```

### 4. Configure the environment variables

Create the `.env` file and add your MySQL credentials:

```text
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=your_mysql_password
DB_NAME=employee_management
```

### 5. Set up the MySQL database

Create the `employee_management` database and `employees` table using the SQL commands provided above.

## How to Run

Run the application using:

```bash
py main.py
```

The application will display the following menu:

```text
========== EMPLOYEE MANAGEMENT SYSTEM ==========
1. Add Employee
2. View Employees
3. Update Employee
4. Delete Employee
5. Exit
```

Select an option and follow the instructions displayed in the console.

## CRUD Operations

### Create

Add a new employee by providing:

* Name
* Email
* Department
* Salary

### Read

View all employee records stored in the MySQL database.

### Update

Update an existing employee using the employee ID.

### Delete

Delete an employee using the employee ID.

## Input Validation

The application performs basic input validation, including:

* Preventing negative salary values
* Checking that salary input is a valid number
* Checking that employee ID input is a valid number
* Handling invalid menu choices

## Security

Database credentials are not hard-coded into the Python source code.

The project uses `python-dotenv` to load database credentials from the `.env` file.

The `.env` file is excluded from Git using `.gitignore`.

## Future Improvements

Possible future improvements include:

* Add employee search functionality
* Add email validation
* Add department filtering
* Add a graphical user interface
* Add logging
* Improve exception handling
* Add automated unit tests
* Add employee sorting functionality