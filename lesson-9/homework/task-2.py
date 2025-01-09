import csv

def read_grades(file_name):
    grades = []
    with open(file_name, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            row["Grade"] = int(row["Grade"])
            grades.append(row)
    return grades

def calculate_average_grades(grades):
    subject_totals = {}
    subject_counts = {}
    for entry in grades:
        subject = entry["Subject"]
        grade = entry["Grade"]
        if subject not in subject_totals:
            subject_totals[subject] = 0
            subject_counts[subject] = 0
        subject_totals[subject] += grade
        subject_counts[subject] += 1
    averages = {subject: subject_totals[subject] / subject_counts[subject] for subject in subject_totals}
    return averages

def write_average_grades(file_name, averages):
    with open(file_name, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Subject", "Average Grade"])
        for subject, average in averages.items():
            writer.writerow([subject, round(average, 2)])

if __name__ == "__main__":
    input_file = "grades.csv"
    output_file = "average_grades.csv"

    grades = []
    print("Enter student grades (Name, Subject, Grade). Type 'done' to finish:")
    while True:
        entry = input("Enter data: ").strip()
        if entry.lower() == 'done':
            break
        try:
            name, subject, grade = map(str.strip, entry.split(","))
            grade = int(grade)
            grades.append({"Name": name, "Subject": subject, "Grade": grade})
        except ValueError:
            print("Invalid input format. Please use 'Name, Subject, Grade'.")

    with open(input_file, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=["Name", "Subject", "Grade"])
        writer.writeheader()
        writer.writerows(grades)

    grades = read_grades(input_file)
    averages = calculate_average_grades(grades)
    write_average_grades(output_file, averages)
    print(f"Average grades written to {output_file}")
