class Operator:
    def __init__(self):
        self.list = []

    def get_elements(self, size):
        self.list = [float(input(f"Enter element {i + 1}: ")) for i in range(size)]

    def display(self):
        print("List:", self.list)

    def __add__(self, other):
        new_list = [a + b for a, b in zip(self.list, other.list)]
        result = Operator()
        result.list = new_list
        return result

    def __sub__(self, other):
        new_list = [a - b for a, b in zip(self.list, other.list)]
        result = Operator()
        result.list = new_list
        return result

    def __mul__(self, other):
        new_list = [a * b for a, b in zip(self.list, other.list)]
        result = Operator()
        result.list = new_list
        return result

    def __floordiv__(self, other):
        new_list = [a // b for a, b in zip(self.list, other.list)]
        result = Operator()
        result.list = new_list
        return result

    def __pow__(self, other):
        new_list = [a ** b for a, b in zip(self.list, other.list)]
        result = Operator()
        result.list = new_list
        return result
