from rpg_character import *

player = Character()

class MenuItem():
    def __init__(self, number, name, function):
        self.number = number
        self.name = name
        self.function = function

    def __repr__(self):
        return '{} {}'.format(self.number, self.name)

load_items = [
    MenuItem(1, 'Load Game', None),
    MenuItem(2, 'Slot 1', None),
    MenuItem(3, 'Slot 2', None),
    MenuItem(4, 'Slot 3', None),
    MenuItem(5, 'Slot 4', None),
    MenuItem(6, 'Slot 5', None)
]

def load_game():
    load_menu = Menu(load_items, 'Load:')
    load_menu.show_list()

def new_game():
    new_items = [
        MenuItem(1, 'Reenter name', None),
        MenuItem(2, 'Continue', new_continue_menu),
        MenuItem(3, 'Save', None),
        MenuItem(4, 'Quit', None)
    ]
    new_menu = Menu(new_items, 'New Game:')
    player.name = input('Enter your name: ')
    print(player.name)
    new_menu.show_list()
    new_menu.number_select(int(input('Choose: ')))

def new_continue_menu():
    new_continue_items = [
        MenuItem(1, 'Reroll stats', new_continue_menu),
        MenuItem(2, 'Continue', potion_menu),
        MenuItem(3, 'Save', None),
        MenuItem(4, 'Quit', None)
    ]
    new_continue_menu_instance = Menu(new_continue_items, 'Roll menu:')
    print('Roll stats: ')
    player.set_status()
    print(player.get_status())
    new_continue_menu_instance.show_list()
    new_continue_menu_instance.number_select(int(input('Choose: ')))



def potion_menu():
    potion_items = [
        MenuItem(1, 'Potion of Health', reselect_potion_menu),
        MenuItem(2, 'Potion of Dexterity', reselect_potion_menu),
        MenuItem(3, 'Potion of Luck', reselect_potion_menu)
    ]
    potion_menu = Menu(potion_items, 'Potions:')
    potion_menu.show_list()
    potion_menu.number_select(int(input('Choose: ')))

def reselect_potion_menu():
    reselect_potion_items = [
    MenuItem(1, 'Reselect potion', potion_menu),
    MenuItem(2, 'Continue', begin_menu),
    MenuItem(3, 'Quit', None)
    ]
    reselect_potion_menu = Menu(reselect_potion_items, 'Reselect potions:')
    reselect_potion_menu.show_list()
    reselect_potion_menu.number_select(int(input('Choose: ')))

def begin_menu():
    print(player.get_status())
    begin_menu_items = [
    MenuItem(1, 'Begin', None),
    MenuItem(2, 'Save', None),
    MenuItem(3, 'Quit', None)
    ]
    begin_menu = Menu(begin_menu_items, 'Start the game:')
    begin_menu.show_list()
    begin_menu.number_select(int(input('Choose: ')))

menu_items = [
    MenuItem(1, 'New Game', new_game),
    MenuItem(2, 'Load Game', load_game),
    MenuItem(3, 'Exit Game', None)
]


class Menu:
    def __init__(self, itemlist, name = None):
        self.itemlist = itemlist
        self.name = name

    def show_list(self):
        if self.name != None:
            print('\n' + self.name + '\n')
        for item in self.itemlist:
            print(item)


    def number_select(self, number):
        for item in self.itemlist:
            if number == item.number:
                return item.function()
