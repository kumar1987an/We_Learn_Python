""" 
Write a Python program to assign grades to students at the end of the year. The program must do the following:

    Ask for a student number.
    Ask for the student’s tutorial mark.
    Ask for the student’s test mark.
    Calculate whether the student’s average so far is high enough for the student to be permitted to write the examination. If the average (mean) of the tutorial and test marks is lower than 40%, the student should automatically get an F grade, and the program should print the grade and exit without performing the following steps.
    Ask for the student’s examination mark.
    Calculate the student’s final mark. The tutorial and test marks should count for 25% of the final mark each, and the final examination should count for the remaining 50%.
    Calculate and print the student's grade, according to the below table

|----------------------|-------------|
| Weighted final Score | Final Grade |
|----------------------|-------------|
| 80 <= mark <= 100    | A           |
| 70 <= mark < 80      | B           |
| 60 <= mark < 70      | C           |
| 50 <= mark < 60      | D           |
| mark < 50            | E           |
|----------------------|-------------|
"""

student_number = input("Please enter a student number: ")
tutorial_mark = float(input("Please enter the student's tutorial mark: "))
test_mark = float(input("Please enter the student's test mark: "))


def student_grade(student_number, tutorial_mark, test_mark):
    if (tutorial_mark + test_mark) / 2 < 40:
        grade = "F"

    else:
        exam_mark = float(input("Please enter the student's final examination mark: "))
        mark = (tutorial_mark + test_mark + 2 * exam_mark) / 4
        print(f"aggregated mark is {mark}")

        if 80 <= mark <= 100:
            grade = "A"
        elif 70 <= mark < 80:
            grade = "B"
        elif 60 <= mark < 70:
            grade = "C"
        elif 50 <= mark < 60:
            grade = "D"
        else:
            grade = "E"

    return f"Student's Roll number {student_number} grade is {grade}."

print(student_grade(student_number, tutorial_mark, test_mark))
