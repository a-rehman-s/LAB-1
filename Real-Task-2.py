def calculate_gpa():
    grade_scale = {
        'A': 4.0,
        'B': 3.0,
        'C': 2.0,
        'D': 1.0,
        'F': 0.0
    }
    total_gpa = 0

    for i in range(5):
        while True:
            grade = input(f"Enter grade for course {i+1} (e.g., A, B, C, D, F): ")
            if grade.upper() in grade_scale:
                total_gpa += grade_scale[grade.upper()]
                break
            else:
                print("Invalid grade. Please enter a valid grade.")

    average_gpa = total_gpa / 5

    print(f"Average GPA: {average_gpa:.2f}")

calculate_gpa()