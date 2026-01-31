# 1. Create text file & 2. Write user data into file
try:
    with open("userdata.txt", "w") as file:
        name = input("Enter your name: ")
        age = input("Enter your age: ")
        file.write(f"Name: {name}\n")
        file.write(f"Age: {age}\n")
    print("Data written successfully.")

except Exception as e:
    print("Error while writing file:", e)


# 3. Read file contents
try:
    with open("userdata.txt", "r") as file:
        content = file.read()
        print("\nFile Content:")
        print(content)

except FileNotFoundError:
    print("File not found.")



# 4. Append data to file
try:
    with open("userdata.txt", "a") as file:
        city = input("Enter your city: ")
        file.write(f"City: {city}\n")
    print("Data appended successfully.")

except Exception as e:
    print("Error while appending file:", e)



# 6. Create CSV file & 7. Write multiple rows
import csv

try:
    with open("students.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Name", "Marks"])
        writer.writerow([1, "Ali", 85])
        writer.writerow([2, "Sara", 90])
        writer.writerow([3, "Ahmed", 78])
    print("CSV file created and data written.")

except Exception as e:
    print("CSV write error:", e)


# 8. Read CSV data
try:
    with open("students.csv", "r") as file:
        reader = csv.reader(file)
        print("\nCSV Data:")
        for row in reader:
            print(row)

except FileNotFoundError:
    print("CSV file not found.")
