"""
Demonstration of Python Collections:
List, Tuple, Set
"""

# Store student names in a list
students = ["Ali", "Ayesha", "Sara", "Ali", "Bilal"]
print("Original student list:", students)

# Add elements to list
students.append("Zain")
print("After adding a student:", students)

# Remove elements from list
students.remove("Sara")
print("After removing a student:", students)

# Sort list
students.sort()
print("Sorted student list:", students)

# Use tuple for fixed data (immutable)
student_info = ("Ali", 20, "Computer Science")
print("\nStudent Info (Tuple):", student_info)

# Convert list to set to remove duplicates
unique_students = set(students)
print("\nUnique students (Set):", unique_students)

# Perform set operations
new_students = {"Hassan", "Ali", "Zara"}

print("\nSet Operations:")
print("Union:", unique_students.union(new_students))
print("Intersection:", unique_students.intersection(new_students))
print("Difference:", unique_students.difference(new_students))

# Iterate over collections
print("\nIterating over List:")
for s in students:
    print(s)

print("\nIterating over Tuple:")
for info in student_info:
    print(info)

print("\nIterating over Set:")
for u in unique_students:
    print(u)

# Mutable vs Immutable comparison
print("\nMutable vs Immutable:")

# List is mutable
students[0] = "Ahmed"
print("Modified List:", students)

# Tuple is immutable (this will cause error if uncommented)
# student_info[0] = "Ahmed"

print("Tuple cannot be modified (Immutable)")
