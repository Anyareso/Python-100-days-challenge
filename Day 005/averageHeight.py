# Input a python list of students

# Program calculates the average student height from of a list of heights
# The average height can be calculated by adding all the heights together and dividing by the total number of heights
student_heights = input("Enter the student heights in metres.").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
    
total_height = 0
for height in student_heights:
    total_height += height 
print(f"Total height = {total_height}")

no_of_students = 0
for student in student_heights:
    no_of_students += 1
print(f"Number of students: {no_of_students}")

average_height = round(total_height / no_of_students)
print(f"average height: {average_height}")