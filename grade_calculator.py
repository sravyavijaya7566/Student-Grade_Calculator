def calculate_grade(marks):
    if marks >= 90:
        return "A", "Excellent! Keep it up! 🌟"
    elif marks >= 80:
        return "B", "Very Good! Keep it up! 👍"
    elif marks >= 70:
        return "C", "Good job! You can do even better! 💪"
    elif marks >= 60:
        return "D", "You passed! Keep learning! 😊"
    else:
        return "F", "Don't give up! Try harder next time! 💖"

while True:
    name = input("Enter student name: ")
    try:
        marks = int(input("Enter marks (0-100): "))
        if 0 <= marks <= 100:
            grade, message = calculate_grade(marks)
            print(f"\n📊 RESULT FOR {name.upper()}:")
            print(f"Marks: {marks}/100")
            print(f"Grade: {grade}")
            print(f"Message: {message}")
            break
        else:
            print("Invalid marks! Please enter a number between 0 and 100.\n")
    except ValueError:
        print("Invalid input! Please enter numeric marks only.\n")
