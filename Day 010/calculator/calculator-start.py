# Calculator
from art import logo
print(logo)
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

def calculator():
    num1 = int(input("What's the first number?: "))
    for operands in operations:
        print(operands)
    should_continue = True

    while should_continue:
        choosen_operand = input("Pick an operation: ")
        num2 = int(input("What's the next number?: "))
        calculation_function = operations[choosen_operand]
        answer = calculation_function(num1, num2)
        print(f"{num1} {choosen_operand} {num2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: . ") == "y":
            num1 = answer
        else:
            should_continue = False
            calculator()

calculator()

# more_calculation = False
# while not more_calculation:
#     to_continue = input(f"Type 'y' to continue calculating with {first_answer}, or type 'n' to exit. ")
#     if to_continue == "y":
#         choosen_operand = input("Pick another operation: ")
#         num3 = int(input("What's the next number?: "))
#         calculation_function = operations[choosen_operand]
#         second_answer = calculation_function(first_answer, num3)
#         print(f"{first_answer} {choosen_operand} {num3} = {second_answer}")
#     else:
#         print("\033c", end='')