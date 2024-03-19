class A:
    def __init__(self, a):
        self.a = a

    def __gt__(self, other):
        if self.a > other.a:
            return True
        else:
            return False

    def __eq__(self, other):
        if self.a == other.a:
            return "Its equal"
        else:
            return "Not equal"

    def __add__(self, other):
        return self.a - other.a


ob1 = A(2)
ob2 = A(2)

if ob1 > ob2:
    print("Ob1 is greater")
else:
    print("Ob2 is greater")

temp = ob1 == ob2

print(temp)
# output Its equal

print(ob1 + ob2)
# output 0
