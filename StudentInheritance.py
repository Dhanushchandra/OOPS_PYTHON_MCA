class Student:
    def __init__(self):
        self.USN = ""
        self.name = ""
        self.age = ""

    def display(self):
        print("USN: " + self.USN)
        print("NAME: " + self.name)
        print("AGE: " + self.age)


class PgStudent(Student):
    def __init__(self):
        super().__init__()
        self.stip = ""
        self.sem = ""
        self.fees = ""

    def getdata(self):
        print("================Post Graduation================")
        self.USN = input("Enter the USN: ")
        self.name = input("Enter the NAME: ")
        self.age = input("Enter the AGE: ")
        self.sem = input("Enter the SEM: ")
        self.stip = input("Enter the Stipend: ")
        self.fees = input("Enter the Fees: ")

    def display(self):
        print("================Post Graduation================")
        print("USN: " + self.USN)
        print("NAME: " + self.name)
        print("AGE: " + self.age)
        print("SEMESTER: " + self.sem)
        print("STIPEND: " + self.stip)
        print("FEES: " + self.fees)


class UgStudent(Student):
    def __init__(self):
        super().__init__()
        self.stip = ""
        self.sem = ""
        self.fees = ""

    def getdata(self):
        print("================Under Graduation================")
        self.USN = input("Enter the USN: ")
        self.name = input("Enter the NAME: ")
        self.age = input("Enter the AGE: ")
        self.sem = input("Enter the SEM: ")
        self.stip = input("Enter the Stipend: ")
        self.fees = input("Enter the Fees: ")

    def display(self):
        print("================Under Graduation================")
        print("USN: " + self.USN)
        print("NAME: " + self.name)
        print("AGE: " + self.age)
        print("SEMESTER: " + self.sem)
        print("STIPEND: " + self.stip)
        print("FEES: " + self.fees)


p1 = PgStudent()
u1 = UgStudent()

while True:
    print("1: Under Graduation \n2: Post Graduation \n3: Exit")

    op = int(input("Enter the option: "))

    if op == 1:
        while True:
            print("1: Enter Data \n2: Display Data \n3: Exit")
            ch = int(input("Enter the option: "))

            if ch == 1:
                u1.getdata()
            elif ch == 2:
                u1.display()
            elif ch == 3:
                break
            else:
                print("Invalid Input")

    elif op == 2:
        while True:
            print("1: Enter Data \n2: Display Data \n3: Exit")
            ch = int(input("Enter the option: "))

            if ch == 1:
                p1.getdata()
            elif ch == 2:
                p1.display()
            elif ch == 3:
                break
            else:
                print("Invalid Input")

    elif op == 3:
        break

    else:
        print("Invalid Input")
