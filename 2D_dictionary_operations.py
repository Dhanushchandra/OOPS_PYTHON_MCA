class Employee:
    def __init__(self):
        self.employees = {}

    def add_employee(self):

        n = int(input("Enter no of employee: "))

        for i in range(1, n + 1):
            temp = dict()
            empno = input("Enter empno: ")
            temp["name"] = input("Enter a Name: ")
            temp["address"] = input("Enter a Address: ")
            temp["pan"] = input("Enter a PAN: ")
            temp["basic"] = input("Enter a Basic: ")
            temp["tds"] = input("Enter a TDS: ")
            temp["deduct"] = input("Enter a Deduct: ")
            temp["hra"] = input("Enter a HRA: ")
            temp["da"] = input("Enter a DA: ")
            temp["salary"] = self.cal_salary(temp)
            self.employees[empno] = temp

    def update_employee(self):
        empno = input("Enter employee ID: ")
        if empno in self.employees:
            print("Update Employee Details:")
            employee = self.employees[empno]
            for key in employee.keys():
                if key != "empno":
                    if key == "salary":
                        continue
                    new_value = input("Enter new {} (Press enter to keep the same): ".format(key))
                    if new_value:
                        employee[key] = new_value
            employee["salary"] = self.cal_salary(employee)
            print("Employee details updated successfully.")
        else:
            print("Employee with ID {} not found.".format(empno))

    def clear_employee(self):
        empno = input("Enter employee ID: ")
        if empno in self.employees:
            del self.employees[empno]
            print("Employee with the ID {} Deleted".format(empno))
        else:
            print("Employee with the ID {} not found.".format(empno))

    def cal_salary(self, employee):
        basic = employee["basic"]
        hra = employee["hra"]
        da = employee["da"]
        deduct = employee["deduct"]
        tds = employee["tds"]
        salary = int(basic) + int(hra) + int(da) - int(deduct) - int(tds)
        return salary

    def display_employees(self):
        for empno, employee in self.employees.items():
            print("Employee ID: ", empno)
            for key, value in employee.items():
                print(f"{key}: {value}")

    def display_an_employee(self):
        empno = input("Enter employee ID: ")
        if empno in self.employees:
            employee = self.employees[empno]
            print("Employee ID: ", empno)
            for key, value in employee.items():
                print(f"{key}: {value}")
        else:
            print("Employee with ID {} not found.".format(empno))


emp1 = Employee()

while True:
    print("1: Add\n2: Display all employees\n3: Display an employee\n4: Delete Employee\n5: Update Employee\n6: Exit")

    op = int(input("Enter your choice: "))

    if op == 1:
        emp1.add_employee()

    elif op == 2:
        emp1.display_employees()

    elif op == 3:
        emp1.display_an_employee()

    elif op == 4:
        emp1.clear_employee()

    elif op == 5:
        emp1.update_employee()

    elif op == 6:
        break

    else:
        print("Invaild input")
