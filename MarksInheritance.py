class StudentInfo:

    def setdata(self):
        self.USN = input("Enter USN: ")
        self.name = input("Enter Name: ")
        self.age = input("Enter Age: ")
        self.sem = input("Enter Semester: ")


class StudentMarks(StudentInfo):

    def entermarks(self):
        self.sub1 = int(input("Enter Subject 1 marks: "))
        self.sub2 = int(input("Enter Subject 2 marks: "))
        self.sub3 = int(input("Enter Subject 3 marks: "))
        self.sub4 = int(input("Enter Subject 4 marks: "))
        self.sub5 = int(input("Enter Subject 5 marks: "))


class StudentDetails(StudentMarks):

    def display(self):
        print("USN: " + self.USN)
        print("Name: " + self.name)
        print("Age: " + self.age)
        print("Semester: " + self.sem)
        print("SUB 1: " + str(self.sub1))
        print("SUB 2: " + str(self.sub2))
        print("SUB 3: " + str(self.sub3))
        print("SUB 4: " + str(self.sub4))
        print("SUB 5: " + str(self.sub5))
        print("Total: " + str(self.sub1 + self.sub2 + self.sub3 + self.sub4 + self.sub5))
        print("Total: " + str((self.sub1 + self.sub2 + self.sub3 + self.sub4 + self.sub5)/500 * 100))


class StudentInfo:
    def setdata(self):
        self.USN = input("Enter USN: ")
        self.name = input("Enter Name: ")
        self.age = input("Enter Age: ")
        self.sem = input("Enter Semester: ")


class StudentMarks(StudentInfo):
    def entermarks(self):
        self.sub1 = int(input("Enter Subject 1 marks: "))
        self.sub2 = int(input("Enter Subject 2 marks: "))
        self.sub3 = int(input("Enter Subject 3 marks: "))
        self.sub4 = int(input("Enter Subject 4 marks: "))
        self.sub5 = int(input("Enter Subject 5 marks: "))


class StudentDetails(StudentMarks):
    def display(self):
        print("USN: " + self.USN)
        print("Name: " + self.name)
        print("Age: " + self.age)
        print("Semester: " + self.sem)
        print("SUB 1: " + str(self.sub1))
        print("SUB 2: " + str(self.sub2))
        print("SUB 3: " + str(self.sub3))
        print("SUB 4: " + str(self.sub4))
        print("SUB 5: " + str(self.sub5))
        total_marks = self.sub1 + self.sub2 + self.sub3 + self.sub4 + self.sub5
        print("Total: " + str(total_marks))
        percentage = (total_marks / 500) * 100
        print("Percentage: {:.2f}%".format(percentage))


def enter_student_data():
    student = StudentDetails()
    student.setdata()
    student.entermarks()
    return student


num_students = int(input("Enter the number of students: "))
students = []

for _ in range(num_students):
        student = enter_student_data()
        students.append(student)

print("\nStudent Details:")
for student in students:
    student.display()
