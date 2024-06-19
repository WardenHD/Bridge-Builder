from pynput import keyboard
from colorama import just_fix_windows_console, Cursor, Back
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
    selectedblock_inv = None
    selectedblock_list = None

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

        if Functions.get_stage() == Constants.STAGES[1]:  
            selectedblock_inv = inv.getselected_inv() 
            selectedblock_list = inv.getselected_list()     
            block = list(filter(None, Constants.BLOCKS[selectedblock_list]))

            map.set_selected_block(selectedblock_list)
            
            # Highlight the block with magenta
            block = Functions.highlight_block(block, Back.MAGENTA, Back.CYAN)

            for i in range(len(block)): 
                Functions.cursor_pos(map.get_blockpos_x(), map.get_blockpos_y() + i)
                print(block[i])
        elif Functions.get_stage() == Constants.STAGES[2]:
            inv.remove_block(selectedblock_inv)
            inv.resetselected()
            map.place_block(selectedblock_list)
            Functions.set_stage(Constants.STAGES[0])

        sleep(0.1)