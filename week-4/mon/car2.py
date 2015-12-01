class Car:
    def __init__(self, color, type, km):
        self.color = color
        self.type = type
        self.km = km

    def ride(self, km):
        self.km += km

    def getmiles(self):
        return self.km * 0.6213

tesla = Car('pink', 'Tesla S', 1200)

tesla.ride(300)

tesla.has_eye_brows = True

lada = Car('red', 'Lada', 1200)

print(tesla.has_eye_brows)
tesla.ride(220)
print(tesla.getmiles())
