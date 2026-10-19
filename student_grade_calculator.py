# Student Grade Calculator
# This beginner Python program calculates a student's average and letter grade.

def get_score(assignment_number):
    """Ask the user for a valid score from 0 to 100."""
    while True:
        try:
            score = float(input(f"Enter the score for assignment {assignment_number} (0-100): "))
            if 0 <= score <= 100:
                return score
            print("Please enter a score between 0 and 100.")
        except ValueError:
            print("Please enter a number, such as 85 or 92.5.")


def get_letter_grade(average):
    """Return a letter grade based on the average."""
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"


def main():
    print("Welcome to the Student Grade Calculator!")
    scores = []

    # Use a loop to collect scores for three assignments.
    for assignment_number in range(1, 4):
        score = get_score(assignment_number)
        scores.append(score)

    # Calculate the average of the entered scores.
    average = sum(scores) / len(scores)
    letter_grade = get_letter_grade(average)

    print("\n--- Grade Report ---")
    for assignment_number, score in enumerate(scores, start=1):
        print(f"Assignment {assignment_number}: {score:.1f}")
    print(f"Average: {average:.1f}")
    print(f"Letter grade: {letter_grade}")

    if average >= 60:
        print("Status: Passing")
    else:
        print("Status: Needs improvement")


if __name__ == "__main__":
    main()
