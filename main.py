from pynput import keyboard
from colorama import just_fix_windows_console, Cursor, Back, Fore, Style
from time import sleep

from inventory import Inventory
from defs import Functions, Constants
from map import Map
from title import Title
from actionbar import Actionbar

class Main:
    just_fix_windows_console()

    inv = Inventory()
    map = Map()
    titlebar = Title(Constants.TITLE_BAR)
    actionbar = Actionbar()

    selectedblock_inv = None
    selectedblock_list = None

    inv_keylistener = keyboard.Listener(inv.on_press, inv.on_release)
    map_keylistener = keyboard.Listener(map.on_press, map.on_release)
    gen_keylistener = keyboard.Listener(Functions.genkeylistener_on_press, Functions.genkeylistener_on_release)
    inv_keylistener.start()
    map_keylistener.start()
    gen_keylistener.start()

    Functions.Flags.menu = True

    while not Functions.Flags.close:
        if not Functions.Flags.restart:
            Functions.set_stage(Constants.STAGES[5])
            Functions.clear()
            
            titlebar.print()

            for i in Constants.TITLE_LOGO[0]:
                print(Fore.BLUE + i.center(60) + Style.RESET_ALL)
            for i in Constants.TITLE_LOGO[1]:
                print(Fore.MAGENTA + i.center(60) + Style.RESET_ALL)

            separator = Constants.WIDTH * '-'
            print(separator + '\n\n\n\n' + separator, '\n') 
            actionbar.print()

            while Functions.Flags.menu and not Functions.Flags.close: sleep(0.1)
            print("e")
            Functions.set_stage(Constants.STAGES[0])
        else:
            Functions.Flags.restart = False
            inv.gen_blocks()

            map.gen_padding()
            map.construct()
         
        Functions.Flags.menu = False

        while not Functions.Flags.menu and not Functions.Flags.close:        
            print(Cursor.POS(1, 1))
            Functions.clear()

            titlebar.print()
            map.print()
            inv.print()
            print()
            actionbar.print()

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

                if Functions.Flags.block_placed:
                    inv.remove_block(selectedblock_inv)
                    inv.resetselected()
                    map.place_block(selectedblock_list)
                    Functions.set_stage(Constants.STAGES[0])
                    Functions.Flags.block_placed = False

            sleep(0.1)

    Functions.clear()