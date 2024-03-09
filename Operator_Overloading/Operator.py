class Operator:
    def _init_(self):
        self.list = []

    def get_elements(self, size):
        self.list = [float(input(f"Enter element {i + 1}: ")) for i in range(size)]

    def display(self):
        print("List:", self.list)

    def _add_(self, other):
        new_list = [a + b for a, b in zip(self.list, other.list)]
        print("Sum:", new_list)

    def _sub_(self, other):
        new_list = [a - b for a, b in zip(self.list, other.list)]
        print("Difference:", new_list)

    def _mul_(self, other):
        new_list = [a * b for a, b in zip(self.list, other.list)]
        print("Product:", new_list)

    def _floordiv_(self, other):
        new_list = [a // b for a, b in zip(self.list, other.list)]
        print("Integer Quotient:", new_list)

    def _pow_(self, other):
        new_list = [a ** b for a, b in zip(self.list, other.list)]
        print("Power:", new_list)