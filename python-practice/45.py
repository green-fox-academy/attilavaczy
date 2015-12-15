

class Student():
    def __init__(self):
        self.grade = []

    def add_grade(self, grade):
        self.grade.append(grade)

    def get_average(self):
        return sum(self.grade)/len(self.grade)



Jozsika = Student()
Jozsika.add_grade(4)
Jozsika.add_grade(2)
print(Jozsika.get_average())
