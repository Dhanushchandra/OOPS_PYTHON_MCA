class employee:
    raise_amt=0.5
    def init(self):
        self.first=""
        self.last=""
        self.empid=""
        self.pay=""

    def apply_raise(self):
        self.pay=int(self.pay*self.raise_amt)

    def get_data(self):
        self.first = input("Enter first: ")
        self.last = input("Enter last: ")
        self.empid = input("Enter empid: ")
        self.pay =  int(input("Enter pay: "))

    def display(self):
        print("first name of the employee: ",self.first)
        print("last name of the employee: ",self.last)
        print("employee id:",self.empid)
        print("employee pay:",self.pay)

class developer(employee):
    raise_amt=1.05
    def apply_raise(self):
        self.pay=int(self.pay*self.raise_amt)

class manager(employee):
    raise_amt=1.06
    def apply_raise(self):
        self.pay=int(self.pay*self.raise_amt)

while True:
    n = int(input("Enter number of employees"))
    for i in range(0,n+1):
        print("1.Developer \n2.Manager \n 3.Exit")
        op = int(input("Enter choice"))
        if op==1:
            e1=developer()
            e1.get_data()
            e1.apply_raise()
            e1.display()
        elif op==2:
            e2=manager()
            e2.get_data()
            e2.apply_raise()
            e2.display()
        elif op==3:
            break
        else:
            print("Invalid")

    break




