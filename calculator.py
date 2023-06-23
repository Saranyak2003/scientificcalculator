import math


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


def power(x, y):
    return x ** y


def square_root(x):
    return math.sqrt(x)


def logarithm(x, base):
    return math.log(x, base)


def factorial(x):
    return math.factorial(x)


while True:
    print("Select an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exponentiation")
    print("6. Square Root")
    print("7. Logarithm")
    print("8. Factorial")
    print("9. Exit")

    choice = input("Enter your choice (1-9): ")

    if choice == '9':
        print("Goodbye!")
        break

    if choice in ['6', '8']:
        num = float(input("Enter a number: "))

        if choice == '6':
            result = square_root(num)
            print("Square root of", num, "is", result)
        else:
            result = factorial(num)
            print("Factorial of", num, "is", result)

    else:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        if choice == '1':
            result = add(num1, num2)
        elif choice == '2':
            result = subtract(num1, num2)
        elif choice == '3':
            result = multiply(num1, num2)
        elif choice == '4':
            if num2 != 0:
                result = divide(num1, num2)
            else:
                print("Error: Division by zero!")
                continue
        elif choice == '5':
            result = power(num1, num2)
        elif choice == '7':
            base = float(input("Enter the base: "))
            result = logarithm(num1, base)
        else:
            print("Invalid choice!")
            continue

        print("Result:", result)
