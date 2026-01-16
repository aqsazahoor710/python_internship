# datatypes_demo.py
# This script demonstrates Python data types, type casting, error handling,
# string concatenation, arithmetic operations, and dynamic typing.

# 1. Declare variables of different data types
integer_var = 10              # int type
float_var = 3.5               # float type
string_var = "Python"         # string type
boolean_var = True            # boolean type

# 2. Print the type of each variable using type()
print("Type of integer_var:", type(integer_var))
print("Type of float_var:", type(float_var))
print("Type of string_var:", type(string_var))
print("Type of boolean_var:", type(boolean_var))

print("\n--- Arithmetic Operations ---")

# 3. Perform arithmetic operations using numeric variables
addition = integer_var + float_var
subtraction = integer_var - float_var
multiplication = integer_var * float_var
division = integer_var / float_var

print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)
print("Division:", division)

print("\n--- Type Casting with User Input ---")

# 4. Convert string input to integer and float using type casting
try:
    # Taking input as string (default behavior of input())
    user_input = input("Enter a number: ")

    # Converting string input to integer
    int_value = int(user_input)
    print("Converted to integer:", int_value)

    # Converting string input to float
    float_value = float(user_input)
    print("Converted to float:", float_value)

except ValueError:
    # 5. Handle invalid input using basic error handling
    print("Error: Please enter a valid numeric value.")

print("\n--- String Concatenation ---")

# 6. Concatenate strings and numbers properly
age = 20

# Converting number to string before concatenation
message = "My age is " + str(age)
print(message)

print("\n--- Dynamic Typing Demonstration ---")

# 7. Demonstrate dynamic typing
dynamic_var = 100
print("dynamic_var value:", dynamic_var, "| Type:", type(dynamic_var))

# Reassigning variable to a string
dynamic_var = "Now I am a string"
print("dynamic_var value:", dynamic_var, "| Type:", type(dynamic_var))

# Reassigning variable to a float
dynamic_var = 45.75
print("dynamic_var value:", dynamic_var, "| Type:", type(dynamic_var))
