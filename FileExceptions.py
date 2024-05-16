while True:
    print("1. Value Error")
    print("2. File not Found Error")
    print("3. Type Error")
    print("4. IO Error")
    print("5. Name Error")
    print("6. Exit")
    n = int(input("Enter your choice: "))
    if n == 1:
        try:
            f = open("f1.txt", "z")
            print("success")
        except ValueError:
            print("Value Error")
    elif n == 2:
        try:
            f = open("f1.txt")
            print("success")
        except FileNotFoundError:
            print("File Not Found Error")
    elif n == 3:
        try:
            f = open("f1.txt","r","w")
            print("success")
        except TypeError:
            print("Type Error")
    elif n == 4:
        try:
            f = open("f1.txt","w+")
            f.write("Hello")
            f1 = open("f2","r")
            print("success")
        except IOError:
            print("Input Output Error")
    elif n == 5:
        try:
            f = ope("f1.txt","r")
            print("success")
        except NameError:
            print("Name Error")
    elif n==6:
        break
    else:
        print("Invalid input")
