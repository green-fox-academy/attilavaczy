class BankAccount:
    def __init__(self, name, startBalance = 0, location = "Budapest"):
        self.balance = startBalance
        self.name = name
        self.location = location

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        self.balance -= amount
        return self.balance
