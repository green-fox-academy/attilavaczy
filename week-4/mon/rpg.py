class Barbarian:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

    def char(self):
        print(self.name)

    def health(self, hp):
        self.hp -= hp

    def dest(self, damage):
        self.damage += damage

    def drink_potion(self):
        self.hp = self.hp + 10

    def print_status(self):
        if self.hp < 0:
            print('Dead')
        elif self.hp > 0:
            print(self.name)
            print(self.hp)

    def strike(self, other):
        other.hp -= self.damage

class Cerlic(Barbarian):
    def heal(self, ally):
        ally.hp += 10


player = Barbarian('Skandar_Graun', 100, 80)

player2 = Barbarian('Hitler', 90, 1)

player3 = Cerlic('Melkor'), 1000, 80)

player.print_status()
player2.strike(player)
player.print_status()
