import logging

# 5 & 6. Configure logging and save logs to file
logging.basicConfig(
    filename="error.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def divide_numbers(a, b):
    """
    Function to divide two numbers
    Demonstrates runtime errors
    """
    try:
        # 8. Simulate runtime errors
        result = a / b
        return result

    # 3. Handle multiple exceptions
    except ZeroDivisionError as e:
        logging.error("Division by zero error", exc_info=True)
        print(" Error: You cannot divide by zero.")
    
    except TypeError as e:
        logging.error("Invalid data type error", exc_info=True)
        print(" Error: Please enter numeric values only.")

    # 4. else block
    else:
        print(" Division successful.")

    # 4. finally block
    finally:
        print(" Operation completed.\n")


def read_file(filename):
    """
    Reads a file and handles file-related errors
    """
    try:
        with open(filename, "r") as file:
            print(file.read())

    except FileNotFoundError as e:
        # 7. Custom error message
        logging.error("File not found", exc_info=True)
        print(f" Custom Error: The file '{filename}' does not exist.")

    finally:
        print(" File read attempt finished.\n")


# Main program
if __name__ == "__main__":
    print("---- Error Handling Demo ----\n")

    # Valid operation
    divide_numbers(10, 2)

    # Runtime error: ZeroDivisionError
    divide_numbers(10, 0)

    # Runtime error: TypeError
    divide_numbers(10, "a")

    # File handling error
    read_file("data.txt")

    print("Check 'error.log' file for detailed error logs.")
