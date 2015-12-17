from random import randint
from rpg_naked import *

class Character():
    def __init__(self, name = None, potion = None, health = 0, dexterity = 0, luck = 0):
        self.name = name
        self.health = health
        self.dexterity = dexterity
        self.luck = luck
        self.inventory = ['Leather armour', 'Sword']
        self.potion = potion

    def get_status(self):
        return '{} {} {} {}'.format(self.name, self.health, self.dexterity, self.luck)

    def set_status(self):
        self.health = randint(1, 6) + randint(1, 6) + 12
        self.dexterity = randint(1, 6) + 6
        self.luck = randint(1, 6) + 6

    def add_potion(self, number):
        potions = ['Potion of Health', 'Potion of Dexterity', 'Potion of Luck']
        self.potion = potions[number - 1]

    def set_inventory(self):
        self.inventory.append(self.potion)
        print(self.inventory)

    def display_potions(self):
        print('This is your potion: ' , self.potion)
