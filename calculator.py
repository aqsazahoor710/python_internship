"""
Simple Calculator Program
Supports addition, subtraction, multiplication, and division
"""

def add(a, b=0):
    """
    Returns the sum of two numbers.
    Default value of b is 0.
    """
    return a + b


def subtract(a, b=0):
    """
    Returns the difference of two numbers.
    Default value of b is 0.
    """
    return a - b


def multiply(a, b=1):
    """
    Returns the product of two numbers.
    Default value of b is 1.
    """
    return a * b


def divide(a, b=1):
    """
    Returns the division of two numbers.
    Handles division by zero.
    Default value of b is 1.
    """
    if b == 0:
        return "Error: Division by zero is not allowed"
    return a / b


def get_numbers():
    """
    Takes two numbers as input from the user.
    """
    x = float(input("Enter first number: "))
    y = float(input("Enter second number: "))
    return x, y


def calculator():
    """
    Main calculator logic based on user choice.
    """
    print("\nCalculator Menu")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Enter your choice (1-4): ")
    a, b = get_numbers()

    if choice == "1":
        print("Result:", add(a, b))
    elif choice == "2":
        print("Result:", subtract(a, b))
    elif choice == "3":
        print("Result:", multiply(a, b))
    elif choice == "4":
        print("Result:", divide(a, b))
    else:
        print("Invalid choice")


# ---------------- TESTING FUNCTIONS ----------------

def test_functions():
    """
    Tests each function independently.
    """
    print("\nTesting Functions")
    print("Add:", add(5, 3))
    print("Subtract:", subtract(10, 4))
    print("Multiply:", multiply(6, 2))
    print("Divide:", divide(8, 2))
    print("Divide by zero:", divide(5, 0))


# Run tests
test_functions()

# Run calculator
calculator()
