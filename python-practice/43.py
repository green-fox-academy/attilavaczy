students = [
        {'name': 'Rezso', 'age': 9.5, 'candies': 2},
        {'name': 'Gerzson', 'age': 10, 'candies': 1},
        {'name': 'Aurel', 'age': 7, 'candies': 3},
        {'name': 'Zsombor', 'age': 12, 'candies': 5},
        {'name': 'Olaf', 'age': 12, 'candies': 7},
        {'name': 'Teodor', 'age': 3, 'candies': 2}
]

#a fornal nem kell kulon definialni a valtozot
def get_student_count(student):
    student_count = 0
    for younglings in students:
        if younglings['candies'] > 4:
            student_count += 1
    return student_count

print(get_student_count(students))
