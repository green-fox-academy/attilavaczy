class Weapon:
    def strike(self, opponent):
        opponent.hp -= self.damage()

    def damage(self):
        pass

class NUKE(Weapon):
    def damage(self):
        return 10

class BFG9000(Weapon):
    def damage(self):
        return 1000

class QuadDamage(Weapon):
    def __init__(self, weapon):
        self.weapon = weapon

    def damage(self):
        return self.weapon.damage() * 4

    def self_damage(self):
        return self.weapon.self.damage() / 4


class Doomguy:
    def __init__(self, weapon):
        self.hp = 100
        self.weapon = weapon

    def strike(self, enemy):
        self.weapon.strike(enemy)

    def __repr__(self):
        return 'hp = {}'.format(self.hp)

doomguy = Doomguy(BFG9000())
enemy = Doomguy(NUKE())

doomguy.strike(enemy)
print(doomguy)
print(enemy)

enemy.strike(doomguy)
print(doomguy)
print(enemy)

doomguy = Doomguy (QuadDamage(BFG9000()))
doomguy.strike(enemy)
print('---')
print(enemy.hp)
