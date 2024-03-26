class Greeting:
    def Hello(self, name=None, age=None):
        if name is None and age is None:
            print("Hello")
        elif name is not None and age is None:
            print(f"hello, {name}")
        elif name is not None and age is not None:
            print(f"Hello {name} and {age}")
        else:
            print("Invalid arguments")


greet = Greeting()
greet.Hello()
greet.Hello("Dhanush")
greet.Hello("Dhanush", 21)
