from database_operations import (
    add_employee,
    view_employees,
    update_employee,
    delete_employee
)


def main():

    while True:

        print("\n========== EMPLOYEE MANAGEMENT SYSTEM ==========")
        print("1. Add Employee")
        print("2. View Employees")
        print("3. Update Employee")
        print("4. Delete Employee")
        print("5. Exit")

        choice = input("Enter your choice: ")

        # ADD EMPLOYEE
        if choice == "1":
            print("\n--- Add Employee ---")

            name = input("Enter name: ")
            email = input("Enter email: ")
            department = input("Enter department: ")

            while True:
                try:
                    salary = float(input("Enter salary: "))

                    if salary < 0:
                        print("Salary cannot be negative.")
                        continue

                    break

                except ValueError:
                    print("Please enter a valid number.")

            add_employee(name, email, department, salary)

        # VIEW EMPLOYEES
        elif choice == "2":
            print("\n--- Employee List ---")
            view_employees()

        # UPDATE EMPLOYEE
        elif choice == "3":
            print("\n--- Update Employee ---")

            try:
                employee_id = int(input("Enter employee ID: "))

                name = input("Enter new name: ")
                email = input("Enter new email: ")
                department = input("Enter new department: ")

                while True:
                    try:
                        salary = float(input("Enter new salary: "))

                        if salary < 0:
                            print("Salary cannot be negative.")
                            continue

                        break

                    except ValueError:
                        print("Please enter a valid number.")

                update_employee(
                    employee_id,
                    name,
                    email,
                    department,
                    salary
                )

            except ValueError:
                print("Employee ID must be a number.")

        # DELETE EMPLOYEE
        elif choice == "4":
            print("\n--- Delete Employee ---")

            try:
                employee_id = int(input("Enter employee ID: "))
                delete_employee(employee_id)

            except ValueError:
                print("Employee ID must be a number.")

        # EXIT
        elif choice == "5":
            print("Thank you for using Employee Management System!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()