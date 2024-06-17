from pynput import keyboard
from colorama import just_fix_windows_console, Cursor
from time import sleep

from inventory import Inventory
from defs import Functions, Constants
from map import Map
from title import Title

class Main:
    just_fix_windows_console()

    inv = Inventory()
    map = Map()
    title = Title(Constants.TITLE)

    inv_keylistener = keyboard.Listener(inv.on_press, inv.on_release)
    map_keylistener = keyboard.Listener(map.on_press, map.on_release)
    inv_keylistener.start()
    map_keylistener.start()

    while True:
        print(Cursor.POS(1, 1))
        Functions.clear()

        title.print()
        map.print()
        inv.print()

        # if Functions.get_stage() == Constants.STAGES[1]:
        #     print(Functions.cursor_pos(map.get_blockpos_x(), map.get_blockpos_y()))

        sleep(0.1)