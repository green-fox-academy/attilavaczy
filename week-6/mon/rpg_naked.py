

class MenuItem():
    def __init__(self, number, name, function):
        self.number = number
        self.name = name
        self.function = function

    def __repr__(self):
        return '{} {}'.format(self.number, self.name)

menu_items = [
    MenuItem(1, 'New Game', None),
    MenuItem(2, 'Load Game', None),
    MenuItem(3, 'Exit Game', None)
]

load_items = [
    MenuItem(1, 'Load Game', None),
    MenuItem(2, 'Slot 1', None),
    MenuItem(3, 'Slot 2', None),
    MenuItem(4, 'Slot 3', None),
    MenuItem(5, 'Slot 4', None),
    MenuItem(6, 'Slot 5', None)
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
                print(item)
                #return item.action()
