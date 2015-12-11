class Warrior:
    def __init__(self):
        self.companions = []
        self.hp = 100

    def join(self, companion):
        self.companions.append(companion)

    def strike(self, opponent):
        opponent.inflict_damage(50)


    def inflict_damage(self, damage):
        self.hp -= damage
        for companion in self.companions:
            companion.notify('damage', self)

    def heal(self, hp):
        self.hp += hp

    def kill(self, hp):
        self.hp -= hp

    def boredtodeath(self, hp):
        self.hp -= hp

class Healer:
    def notify(self, type, warrior):
        if type == 'damage':
            warrior.heal(10)

class Killer:
    def notify(self, type, warrior):
        if type == 'damage':
            warrior.kill(40)

class Kardashians:
    def notify(self, type, warrior):
        if type == 'heal':
            warrior.boredtodeath(100)


rabbit = Warrior()
wolf = Warrior()
shaman = Healer()
hitler = Killer()
kimmy = Kardashians()

rabbit.join(shaman)

wolf.strike(rabbit)
print(rabbit.hp)

wolf.join(hitler)
rabbit.strike(wolf)
print(wolf.hp)

rabbit.join(kimmy)
rabbit.strike(wolf)
print(wolf.hp)
