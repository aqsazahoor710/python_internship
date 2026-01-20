def get_grade(marks):
    """Return grade based on marks"""

    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 40:
        return "D"
    else:
        return "F"


def evaluate_student(marks):
    """Evaluate student result using nested conditions"""

    # Handle invalid marks
    if marks < 0 or marks > 100:
        print("❌ Invalid marks! Please enter marks between 0 and 100.")
        return

    grade = get_grade(marks)
    print(f"📊 Marks: {marks}")
    print(f"🏷 Grade: {grade}")

    # Nested business rules
    if marks >= 40:
        print("✅ Status: Pass")

        if marks >= 90:
            print("🎉 Excellent performance! Distinction awarded.")
        elif marks >= 75 and marks < 90:
            print("👏 Very good performance.")
        else:
            print("👍 Good, but you can improve more.")
    else:
        print("❌ Status: Fail")

        if marks < 20:
            print("⚠ Serious improvement required.")
        else:
            print("📘 Try harder next time.")


# ---- MAIN PROGRAM ----
try:
    user_marks = int(input("Enter your marks (0-100): "))
    evaluate_student(user_marks)
except ValueError:
    print("❌ Please enter numeric values only.")
