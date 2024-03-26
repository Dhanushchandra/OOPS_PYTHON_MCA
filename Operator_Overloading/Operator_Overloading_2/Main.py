from Operator import *

obj1 = op()
obj2 = op()
obj1.input()
obj2.input()
while True:
    print("\n 0.Exit \n 1.Addition \n 2.Subtraction \n 3.Multiplication \n 4.Floor Division")
    ch = int(input("Enter your choice: "))
    if ch == 0:
        break
    elif ch == 1:
        obj1 + obj2
    elif ch == 2:
        obj1 - obj2
    elif ch == 3:
        obj1 * obj2
    elif ch == 4:
        obj1 // obj2
    else:
        print("Invalid Input")
