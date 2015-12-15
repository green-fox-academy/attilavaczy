from rpg_naked import *
import os
def cls():
    os.system('cls' if os.name=='nt' else 'clear')
cls()

menu = Menu(menu_items)
menu.show_list()
menu.number_select(int(input('Choose: ')))
