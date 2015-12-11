from character import Character
class Wizard(Character):
    def __init__(self, name, hp, damage, manna):
        super().__init__(name, hp, damage)
        self.manna = manna

    def strike(self, opponent):
        self.hp += 3
        super().strike(opponent)

    def reduce_manna(self, opponent):
        self.manna -= 5

    def manna_strike(self, opponent):
        is_enough = self.manna > 5
        self.manna -= 5 if is_enough else 0
        opponent.hp -= self.damage * (3 if is_enough else 1 / 3)
