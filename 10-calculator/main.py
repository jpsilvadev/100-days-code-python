from art import logo
import os


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {"+": add, "-": subtract, "*": multiply, "/": divide}


print(logo)
num1 = float(input("What's the first number?: "))
while True:
    for k in operations:
        print(k)
    op = input("Pick an operation: ")
    num2 = float(input("What's the next number?: "))

    result = operations[op](num1, num2)
    print(f"{num1} {op} {num2} = {result}")

    keep_result = input(
        f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: "
    ).lower()
    if keep_result != "y":
        os.system("cls" if os.name == "nt" else "clear")
        print(logo)
        num1 = float(input("What's the first number?: "))
    num1 = result
