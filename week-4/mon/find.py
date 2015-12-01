students = [
    {'name': 'tibi' , 'age': 8},
    {'name': 'Adorjan' , 'age': 9},
    {'name': 'Agoston' , 'age': 6},
    {'name': 'Aurel' , 'age': 7},
    {'name': 'dezso' , 'age': 12},
]


students_at_least_than_8 = []

for n in students:
    if n['age'] >= 8:
        students_at_least_than_8.append(n['name'])
print(students_at_least_than_8)


student_ages_starting_with_A = []

for student in students:
    if student['name'][0] == 'A':
        student_ages_starting_with_A.append(student['age'])


print(student_ages_starting_with_A)
