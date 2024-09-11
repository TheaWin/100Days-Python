import art

def add(n1, n2):
    return n1 + n2

def subtract(n1,n2):
    return n1 - n2

def multiply(n1,n2):
    return n1 * n2

def divide (n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def calculator():
    print(art.logo)
    should_continue = True
    result = 0
    first_number = float(input("What's the first number?: "))
    while should_continue:
        operator = input("+\n-\n*\n/\nPick an operation: ")
        second_number = float(input("What's the next number?: "))

        if operator == "+":
            result = add(first_number,second_number)
        elif operator == "-":
            result = subtract(first_number,second_number)
        elif operator == "*":
            result = multiply(first_number,second_number)
        elif operator == "/":
            result = divide(first_number,second_number)
        else:
            print("Invalid operator or number")

        print(f"{first_number} {operator} {second_number} = {result}")
        to_continue = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ").lower()

        if to_continue == "y":
            first_number = result
        else:
            should_continue = False
            print("\n" * 20)
            calculator()

calculator()

# This is the calculator using the dictionary for operations
# def calculator_with_dictionary():
#     print(art.logo)
#     should_continue = True
#     first_number = float(input("What's the first number?: "))
#     while should_continue:
#         for symbol in operations:
#             print(symbol)
#         operator = input("Pick an operation: ")
#         second_number = float(input("What's the next number?: "))
#         result = operations[operator](first_number,second_number)
#         print(f"{first_number} {operator} {second_number} = {result}")
#
#         to_continue = input(
#             f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ").lower()
#
#         if to_continue == "y":
#             first_number = result
#         else:
#             should_continue = False
#             print("\n" * 20)
#             calculator()
