# hello_world.py
# This script prints your name, internship role, and today's date.
# It also accepts user input for name and role.

# 1. Import the datetime module to get today's date
from datetime import date

# 2. Store values in variables
# Using input() to allow user to enter their name and role
name = input("Enter your name: ")         # Prompt user for their name
role = input("Enter your internship role: ")  # Prompt user for internship role

# 3. Get today's date
today = date.today()  # Returns date in YYYY-MM-DD format

# 4. Print the details
print("\n--- Internship Details ---")
print("Name:", name)           # Prints the user's name
print("Role:", role)           # Prints the internship role
print("Today's Date:", today)  # Prints today's date

# 5. End of script
print("\nThank you for running this program!")
