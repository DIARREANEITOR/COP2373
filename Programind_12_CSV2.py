import numpy as np
import csv
import random


def collect_and_fill_data():
    # 1. Ask for number of students
    count = int(input("How many students will you enter? "))
    students = []
    header = ['First Name', 'Last Name', 'Exam 1', 'Exam 2', 'Exam 3']

    # 2. Manual data entry
    for i in range(count):
        print(f"\nStudent {i + 1}:")
        first = input("First Name: ")
        last = input("Last Name: ")
        e1 = float(input("Exam 1: "))
        e2 = float(input("Exam 2: "))
        e3 = float(input("Exam 3: "))
        students.append([first, last, e1, e2, e3])

    # 3. Auto-fill if less than 10
    if len(students) < 10:
        remaining = 10 - len(students)
        print(f"\nAdding {remaining} more students automatically to reach 10...")
        for i in range(remaining):
            first = f"Student_{i + 1}"
            last = "Lastname"
            e1, e2, e3 = np.random.randint(50, 101, size=3)
            students.append([first, last, float(e1), float(e2), float(e3)])

    # 4. Save to CSV
    with open('grades.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(students)

    return np.array([row[2:] for row in students], dtype=float)


def run_analysis(grades_np):
    # Print structure
    print("\nDATASET PREVIEW:")
    print(grades_np[:5])

    # Stats per exam
    print("\nPER EXAM STATISTICS:")
    exams = ["Exam 1", "Exam 2", "Exam 3"]
    for i, name in enumerate(exams):
        col = grades_np[:, i]
        print(
            f"{name} -> Mean: {np.mean(col):.2f} | Median: {np.median(col)} | Std: {np.std(col):.2f} | Min: {np.min(col)} | Max: {np.max(col)}")

    # Overall stats
    print("\nOVERALL STATISTICS:")
    print(f"Mean: {np.mean(grades_np):.2f}")
    print(f"Median: {np.median(grades_np)}")
    print(f"Standard Deviation: {np.std(grades_np):.2f}")
    print(f"Min: {np.min(grades_np)} | Max: {np.max(grades_np)}")

    # Pass/Fail counts
    print("\nPASS/FAIL COUNTS (Pass >= 60):")
    for i, name in enumerate(exams):
        passed = np.sum(grades_np[:, i] >= 60)
        failed = np.sum(grades_np[:, i] < 60)
        print(f"{name}: {passed} Passed, {failed} Failed")

    # Overall pass percentage
    pass_pct = (np.sum(grades_np >= 60) / grades_np.size) * 100
    print(f"\nOverall Pass Percentage: {pass_pct:.2f}%")


if __name__ == "__main__":
    data = collect_and_fill_data()
    run_analysis(data)