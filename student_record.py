import json

# 1. Store student details using dictionary
student = {
    "id": 101,
    "name": "Aqsa",
    "age": 20,
    "course": "Computer Science",
    "marks": 88
}

# 2. Access keys and values
print("Keys:", student.keys())
print("Values:", student.values())

# 3. Update entries
student["marks"] = 92
student["semester"] = "4th"

# 4. Delete an entry
del student["age"]

# 5. Loop through dictionary
print("\nStudent Details:")
for key, value in student.items():
    print(f"{key}: {value}")

# 6. Convert dictionary to JSON
student_json = json.dumps(student, indent=4)

# 7. Save JSON to file
with open("student.json", "w") as file:
    file.write(student_json)

print("\nData saved to student.json")

# 8. Read JSON back into Python
with open("student.json", "r") as file:
    loaded_student = json.load(file)

# 9. Print clean formatted output
print("\nLoaded Student Data:")
for key, value in loaded_student.items():
    print(f"{key.capitalize():<10}: {value}")
