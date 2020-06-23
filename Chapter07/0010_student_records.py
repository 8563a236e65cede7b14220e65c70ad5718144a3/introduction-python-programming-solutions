"""
Program 7.9
Input Information for n number of Students
as Given Below:
    a) Name
    b) Registration Number
    c) Total Marks
"""


def student_details(number_of_students):
    student_name = {}
    for i in range(0, number_of_students):
        name = input("Enter the Name of the Student\n")
        registration_number = input("Enter student's Registration Number\n")
        total_marks = input("Enter student's Total Marks\n")
        student_name[name] = [registration_number, total_marks]

    student_search = input("Enter name of the student you want to search\n")
    if student_search not in student_name.keys():
        print("Student you are searching is not present in class")
    else:
        print("Student you are searching is present in class")
        print(f"Student's Registration Number is {student_name[student_search][0]}")
        print(f"Student's Total Marks is {student_name[student_search][1]}")


def main():
    number_of_students = int(input("Enter the number of students"))
    student_details(number_of_students)


if __name__ == "__main__":
    main()
