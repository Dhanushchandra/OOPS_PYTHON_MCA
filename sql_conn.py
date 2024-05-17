import mysql.connector

# Function to create a connection to the MySQL database
def create_connection():
    conn = mysql.connector.connect(
        host="172.16.34.43",
        user="mca041",
        password="mca041",
        database="db_mca034",
        auth_plugin="mysql_native_password"
    )
    return conn

# Function to create the employee table
def create_table(conn):
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS employees (
            slno INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255),
            address VARCHAR(255),
            empcode VARCHAR(50),
            dateofbirth DATE,
            age INT,
            mobile VARCHAR(20),
            status VARCHAR(50),
            designation VARCHAR(255)
        )
    """)
    print("Table 'employees' created successfully!")

# Function to add details of an employee
def add_employee(conn, name, address, empcode, dateofbirth, age, mobile, status, designation):
    cursor = conn.cursor()
    sql = "INSERT INTO employees (name, address, empcode, dateofbirth, age, mobile, status, designation) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    values = (name, address, empcode, dateofbirth, age, mobile, status, designation)
    cursor.execute(sql, values)
    conn.commit()
    print("Employee added successfully!")

# Function to search for an employee by ID
def search_employee(conn, emp_id):
    cursor = conn.cursor()
    sql = "SELECT * FROM employees WHERE slno = %s"
    cursor.execute(sql, (emp_id,))
    employee = cursor.fetchone()
    if employee:
        print("Employee found:")
        print("Serial No:", employee[0])
        print("Name:", employee[1])
        print("Address:", employee[2])
        print("Employee Code:", employee[3])
        print("Date of Birth:", employee[4])
        print("Age:", employee[5])
        print("Mobile:", employee[6])
        print("Status:", employee[7])
        print("Designation:", employee[8])
    else:
        print("Employee not found!")

# Function to delete an employee by ID
def delete_employee(conn, emp_id):
    cursor = conn.cursor()
    sql_select = "SELECT * FROM employees WHERE slno = %s"
    cursor.execute(sql_select, (emp_id,))
    employee = cursor.fetchone()

    if employee:
        sql_delete = "DELETE FROM employees WHERE slno = %s"
        cursor.execute(sql_delete, (emp_id,))
        conn.commit()
        print("Employee with Serial No", emp_id, "deleted successfully.")
    else:
        print("Employee with Serial No", emp_id, "not found.")

# Function to update employee details by ID
def update_employee(conn, emp_id, designation, salary):
    cursor = conn.cursor()
    sql = "UPDATE employees SET designation = %s, salary = %s WHERE id = %s"
    values = (designation, salary, emp_id)
    cursor.execute(sql, values)
    conn.commit()
    print("Employee details updated successfully!")

# Function to print all employees
def print_all_employees(conn):
    cursor = conn.cursor()
    sql = "SELECT * FROM employees"
    cursor.execute(sql)
    employees = cursor.fetchall()
    if employees:
        print("All Employees:")
        for employee in employees:
            print("Serial No:", employee[0])
            print("Name:", employee[1])
            print("Address:", employee[2])
            print("Employee Code:", employee[3])
            print("Date of Birth:", employee[4])
            print("Age:", employee[5])
            print("Mobile:", employee[6])
            print("Status:", employee[7])
            print("Designation:", employee[8])
            print("-----------------------")
    else:
        print("No employees found!")

# Main function
def main():
    # Create a connection to the MySQL database
    conn = create_connection()

    # Create the employee table if it doesn't exist
    create_table(conn)

    # Menu-driven interface
    while True:
        print("\nMENU:")
        print("1. Add Employee")
        print("2. Search Employee")
        print("3. Update Employee")
        print("4. Delete Employee")
        print("5. Print All Employees")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter employee name: ")
            address = input("Enter employee address: ")
            empcode = input("Enter employee code: ")
            dateofbirth = input("Enter employee date of birth (YYYY-MM-DD): ")
            age = int(input("Enter employee age: "))
            mobile = input("Enter employee mobile number: ")
            status = input("Enter employee status: ")
            designation = input("Enter employee designation: ")
            add_employee(conn, name, address, empcode, dateofbirth, age, mobile, status, designation)
        elif choice == "2":
            emp_id = int(input("Enter employee Serial No to search: "))
            search_employee(conn, emp_id)
        elif choice == "3":
            emp_id = int(input("Enter employee Serial No to update: "))
            designation = input("Enter new designation: ")
            salary = float(input("Enter new salary: "))
            update_employee(conn, emp_id, designation, salary)
        elif choice == "4":
            emp_id = int(input("Enter employee Serial No to delete: "))
            delete_employee(conn, emp_id)
        elif choice == "5":
            print_all_employees(conn)
        elif choice == "6":
            break
        else:
            print("Invalid choice! Please enter a valid option.")

    # Close the database connection
    conn.close()
    print("Connection closed.")

main()