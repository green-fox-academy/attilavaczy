class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def costs(self, pay):
        self.balance -= pay

    def shitfuck(self, receive):
        self.balance += receive

    def bubu(self):
        print(self.name)

    def transfer(self, other, amount):
        self.costs(amount)
        other.shitfuck(amount)
account = BankAccount("tojas", 4000)

account.costs(400)
account.shitfuck(200)
account.bubu

karoly = BankAccount('karoly *', 7000000)

account.transfer(karoly, 600000)

print(account.balance)
