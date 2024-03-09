from Operator import Operator

# Create objects
ov1 = Operator()
ov2 = Operator()

# Get elements for the first list
ov1.get_elements(int(input("Enter the size of the first list: ")))
ov1.display()

# Get elements for the second list
ov2.get_elements(int(input("Enter the size of the second list: ")))
ov2.display()

# Display results
ov1._add_(ov2)
ov1._sub_(ov2)
ov1._mul_(ov2)
ov1._floordiv_(ov2)
ov1._pow_(ov2)