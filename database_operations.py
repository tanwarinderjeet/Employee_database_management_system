import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()


def get_connection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )


def add_employee(name, email, department, salary):

    connection = None
    cursor = None

    try:
        connection = get_connection()
        cursor = connection.cursor()

        query = """
        INSERT INTO employees (name, email, department, salary)
        VALUES (%s, %s, %s, %s)
        """

        values = (name, email, department, salary)

        cursor.execute(query, values)
        connection.commit()

        print("Employee added successfully!")

    except mysql.connector.Error as error:
        print("Database error:", error)

    finally:
        if cursor:
            cursor.close()

        if connection:
            connection.close()


def view_employees():

    connection = get_connection()
    cursor = connection.cursor()

    query = "SELECT * FROM employees"
    cursor.execute(query)

    employees = cursor.fetchall()

    print("\n========== EMPLOYEE LIST ==========")

    for employee in employees:
        print(f"ID         : {employee[0]}")
        print(f"Name       : {employee[1]}")
        print(f"Email      : {employee[2]}")
        print(f"Department : {employee[3]}")
        print(f"Salary     : {employee[4]}")
        print("-----------------------------------")

    cursor.close()
    connection.close()


def update_employee(employee_id, name, email, department, salary):

    connection = get_connection()
    cursor = connection.cursor()

    query = """
    UPDATE employees
    SET name = %s,
        email = %s,
        department = %s,
        salary = %s
    WHERE employee_id = %s
    """

    values = (name, email, department, salary, employee_id)

    cursor.execute(query, values)
    connection.commit()

    if cursor.rowcount > 0:
        print("Employee updated successfully!")
    else:
        print("Employee not found.")

    cursor.close()
    connection.close()


def delete_employee(employee_id):

    connection = get_connection()
    cursor = connection.cursor()

    query = "DELETE FROM employees WHERE employee_id = %s"

    cursor.execute(query, (employee_id,))
    connection.commit()

    if cursor.rowcount > 0:
        print("Employee deleted successfully!")
    else:
        print("Employee not found.")

    cursor.close()
    connection.close()