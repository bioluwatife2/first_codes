# Project Scrore Sheet

# Get users name
student_name = str(input("What's your name?: "))
student_name = student_name.title()

# Perform a condition to check if users name is less than 5 characters
if len(student_name) < 5:
    print('User Name is too short')

# Get users grade score
grade_score = int(input("What is your grade score?: "))

# Perform a condition to check the grade points
if grade_score <= 100 and grade_score>=85:
    grade_point = 'A'
elif grade_score <= 84 and grade_score >=70:
   grade_point = 'B'
elif grade_score <= 69 and grade_score>=50:
    grade_point = 'C'
elif grade_score <= 49 and grade_score>=40:
    grade_point = 'D'
else:
    grade_point = 'F'
# Example 100 - 85 = A, 85-75 = B, 75-60 = C, 60-50 = D, 50 - 0 =  F

# Remarks
if grade_point == 'A':
    remarks = 'Excellent!'
elif grade_point == 'B':
    remarks = 'Very Good!'
elif grade_point == 'C':
    remarks = 'Good'
elif grade_point == 'D':
    remarks = 'Pass'
else:
    remarks = 'Fail!'

# Print user's name and grade score with corresponding grade point
print('Your Score sheet')
print('Name: {} | Grade Score: {} | Grade Point: {}'.format(student_name, grade_score, grade_point))
print(f'Remarks: ', remarks)