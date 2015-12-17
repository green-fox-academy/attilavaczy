from random import randint
from rpg_naked import *

class Character():
    def __init__(self, name = None, health = 0, dexterity = 0, luck = 0, inventory = ['Leather armour', 'Sword']):
        self.name = name
        self.health = health
        self.dexterity = dexterity
        self.luck = luck
        self.inventory = inventory

    def get_status(self):
        return '{} {} {} {}'.format(self.name, self.health, self.dexterity, self.luck)

    def set_status(self):
        self.health = randint(1, 6) + randint(1, 6) + 12
        self.dexterity = randint(1, 6) + 6
        self.luck = randint(1, 6) + 6
