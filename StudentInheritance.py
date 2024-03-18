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




def manage_students():
    pgstudents = []
    ugstudents = []


def manage_students():
    pg_students = []
    ug_students = []

    while True:
        print("1: Under Graduation \n2: Post Graduation \n3: Display All Students \n4: Exit")
        option = input("Enter the option: ")

        if option == '1':
            num = int(input("Enter the no of students: "))
            for i in range(0, num ):
                ug_student = UgStudent()
                ug_student.getdata()
                ug_students.append(ug_student)

        elif option == '2':
            num = int(input("Enter the no of students: "))
            for i in range(0, num):
                pg_student = PgStudent()
                pg_student.getdata()
                pg_students.append(pg_student)

        elif option == '3':
            print("\n===== Post Graduation Students =====")
            for pg_student in pg_students:
                pg_student.display()
                print()
            print("\n===== Under Graduation Students =====")
            for ug_student in ug_students:
                ug_student.display()
                print()

        elif option == '4':
            break

        else:
            print("Invalid Input")

manage_students()
