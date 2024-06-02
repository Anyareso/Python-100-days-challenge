# Calculator

# Add
def add(n1, n2):
    return n1 + n2

# Subtract
def subtract(n1,n2):
    return n1 -  n2

# Multiply
def multiply(n1, n2):
    return n1 * n2

# Divide
def divide(n1, n2):
    return n1 / n2

operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide
}

num1 = int(input("What's the first number?: "))
num2 = int(input("What's the second number?: "))

for operands in operations:
    print(operands)
