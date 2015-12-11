warrior.join.KillerField()


class Warrior:
    def __init__(self):
        self.companions = []
        self.hp = 100

    def join(self, companion):
        self.companions.append(companion)

    def strike(self, opponent):
        opponent.inflict_damage(40)


    def inflict_damage(self, damage):
        self.hp -= damage
        for companion in self.companions:
            companion.notify('damage', self)

    def kill(self, hp):
        self.hp -= hp

class KillerField:
    def notify(self, type, warrior):
        if type == 'damage':
            warrior.kill(40)
