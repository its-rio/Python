#wap to check students grades, your program should fullfill the following conditions,
#Grade A - Outstanding
#Grade B - Excellent
#Grade C - Very Good 
#Grade D - Good
#Grade E - Satisfactionary
#Others - Unrecognized
#A person should also ask for student name, classand section.

student_name = input("Enter student's name: ")
student_class = input("Enter student's class: ")
student_section = input("Enter student's section: ")

marks_obtained = float(input("Enter marks obtained: "))
total_marks = float(input("Enter total marks: "))

def get_grade(percentage):
    if percentage >= 90:
        return "A - Outstanding"
    elif percentage >= 80:
        return "B - Excellent"
    elif percentage >= 70:
        return "C - Very Good"
    elif percentage >= 60:
        return "D - Good"
    elif percentage >= 50:
        return "E - Satisfactory"
    else:
        return "Unrecognized"

percentage = (marks_obtained / total_marks) * 100

grade = get_grade(percentage)

print(f"\nStudent Name:", student_name)
print(f"Class:", student_class)
print(f"Section:", student_section)
print(f"Percentage:", percentage,"%")
print(f"Grade: ",grade)



