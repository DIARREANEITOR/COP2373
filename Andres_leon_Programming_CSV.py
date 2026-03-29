import csv


def write_grades():
    count = int(input("Enter the number of students: "))
    header = ['First Name', 'Last Name', 'Exam 1', 'Exam 2', 'Exam 3']

    with open('grades.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(header)

        for _ in range(count):
            first = input("First Name: ")
            last = input("Last Name: ")
            e1 = int(input("Exam 1: "))
            e2 = int(input("Exam 2: "))
            e3 = int(input("Exam 3: "))
            writer.writerow([first, last, e1, e2, e3])


def read_grades():
    try:
        with open('grades.csv', mode='r') as file:
            reader = csv.reader(file)
            # Simple column spacing
            fmt = "{:<15} {:<15} {:<10} {:<10} {:<10}"

            for row in reader:
                print(fmt.format(*row))
    except FileNotFoundError:
        print("The file grades.csv does not exist.")


if __name__ == "__main__":
    write_grades()
    print("\nData recorded. Displaying table:\n")
    read_grades()