# 1. Print numbers from 1 to 100 using for loop
print(" Numbers from 1 to 100:")
for i in range(1, 101):
    print(i, end=" ")
print("\n")


# 2. Countdown timer using while loop
print(" Countdown Timer:")
count = 5
while count > 0:
    print(count)
    count -= 1
print(" Time's up!\n")


# 3. Using break and continue
print("Break & Continue Example:")
for i in range(1, 11):
    if i == 7:
        print(" Loop stopped at 7")
        break
    if i % 2 == 0:
        continue  # Skip even numbers
    print(i)
print()


# 4. Iterate over string characters
word = "Python"
print(" Characters in string:")
for char in word:
    print(char)
print()


# 5. Multiplication table
num = 5
print(f"✖ Multiplication Table of {num}:")
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
print()


# 6. range() with steps
print("Numbers from 0 to 20 with step 2:")
for i in range(0, 21, 2):
    print(i, end=" ")
print("\n")


# 7. Loop combined with condition
print("Numbers divisible by 3 between 1 and 30:")
for i in range(1, 31):
    if i % 3 == 0:
        print(i, end=" ")
