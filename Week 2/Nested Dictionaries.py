'''Basic Creation: Create a dictionary of students. Each student (key) should have another dictionary as a value containing their age and grade.
Accessing Nested Elements: Fetch the age of a specific student.
Updating Nested Dictionary: Update the grade of a student.
Looping through Nested Dictionaries: Print out each student's name along with their age and grade.
'''
def line():
    print('______________________________________________________________________________')
students = {
    'jonny': {'age': 19, 'grade': 'A'},
    'ricky': {'age': 25, 'grade': 'B'},
    'cowboy': {'age': 24, 'grade': 'C'},
    'yana': {'age': 16, 'grade': 'A'}
}
print(students)

line()
a= students['jonny']
print(a)

line()

b = students['ricky']['grade'] = 'A+'
print(b)
print(students)
line()

for student,studentdetails in students.items():
    print(f"Student Name: {student}")
    print(f"Age: {studentdetails['age']}")
    print(f"Grade: {studentdetails['grade']}")
