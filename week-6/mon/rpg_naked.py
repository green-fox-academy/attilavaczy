
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
    load_menu = Menu(load_items)
    load_menu.show_list()


def new_game():
    new_items = [
        MenuItem(1, 'Reenter name', None),
        MenuItem(2, 'Continue', None),
        MenuItem(3, 'Save', None),
        MenuItem(4, 'Quit', None)
    ]
    new_menu = Menu(new_items)
    new_menu.number_select(input('Enter your name: '))
    new_menu.show_list()
    new_menu.number_select(int(input('Choose: ')))

menu_items = [
    MenuItem(1, 'New Game', new_game),
    MenuItem(2, 'Load Game', load_game),
    MenuItem(3, 'Exit Game', None)
]


class Menu:
    def __init__(self, itemlist):
        self.itemlist = itemlist

    def show_list(self):
        print('\nMenu:\n')
        for item in self.itemlist:
            print(item)


    def number_select(self, number):
        for item in self.itemlist:
            if number == item.number:
                return item.function()
