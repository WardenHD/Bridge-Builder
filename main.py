from pynput import keyboard
from colorama import just_fix_windows_console, Cursor, Back, Fore, Style
from time import sleep
from re import findall

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

    if len(Functions.Saves.get_all()) == 0: Functions.Saves.add()

    while not Functions.Flags.close:

        if not Functions.Flags.restart:
            Functions.clear()
            
            titlebar.print()
            
            if Functions.get_stage() == Constants.STAGES[6]:
                print()
                for i, p in enumerate(Functions.Saves.get_all()):
                    if Functions.get_highlighted_profile() == i:
                        print(f"{Fore.BLUE}Profile {p[0]}: Wins - {p[1]}{Style.RESET_ALL}".center(Constants.WIDTH + len(Fore.BLUE + Style.RESET_ALL)))
                    else: print(f"Profile {p[0]}: Wins - {p[1]}".center(Constants.WIDTH))
                print()
            elif Functions.get_stage() == Constants.STAGES[5]:
                for line in Constants.ABOUT.splitlines(): print(line.center(65, " "))
            else:
                for i in Constants.TITLE_LOGO[0]:
                    print(Fore.BLUE + i.center(60) + Style.RESET_ALL)
                for i in Constants.TITLE_LOGO[1]:
                    print(Fore.MAGENTA + i.center(60) + Style.RESET_ALL)

            separator = Constants.WIDTH * '-'
            print(separator + '\n\n\n\n' + separator, '\n') 
            actionbar.print() 
        else:
            Functions.Flags.restart = False
            inv.gen_blocks()
            map.move_block(0, 0)
            map.gen_padding()
            map.construct()
            Functions.set_stage(Constants.STAGES[0])

        correct_stage = (Functions.get_stage() != Constants.STAGES[4] and Functions.get_stage() != 
            Constants.STAGES[6] and Functions.get_stage() != Constants.STAGES[5])

        while not Functions.Flags.close and not Functions.Flags.restart and correct_stage:        
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
                
                # Highlight the block with magenta or red if blocks intercept
                block = Functions.highlight_block(block, Back.MAGENTA if not Functions.Flags.blocks_intercept else Back.RED, Back.CYAN) 
                if Functions.Flags.blocks_intercept: Functions.Flags.blocks_intercept = False
                
                for i in range(len(block)): 
                    escape_codes = findall(r"\x1b\[.m|\x1b\[..m", block[i])
                    block[i] = [i for i in block[i] if not i == Back.CYAN and not i.isdigit() and i not in '[m']

                    c = 0
                    is_second_code = False
                    for j in range(len(block[i])):
                        if block[i][j] == ' ': continue
                        if block[i][j] == '\x1b' and len(escape_codes) != 0:
                            Functions.cursor_pos(map.get_blockpos_x() + c, map.get_blockpos_y() + i)
                            print(escape_codes[0])
                            del escape_codes[0]
                            if is_second_code: c += 1
                            is_second_code = False if is_second_code else True
                            continue
                        else:   
                            Functions.cursor_pos(map.get_blockpos_x() + c, map.get_blockpos_y() + i)
                            print(block[i][j])
                    
                sleep(0.05)

                if Functions.Flags.block_placed:
                    map.place_block(selectedblock_list)
                    if not Functions.Flags.blocks_intercept:
                        inv.remove_block(selectedblock_inv)
                        inv.resetselected()
                        Functions.set_stage(Constants.STAGES[0])
                    
                    Functions.Flags.block_placed = False

            if Functions.Flags.testing:
                id = Functions.get_selected_profile()
                success = map.do_testing()
                Functions.Saves.set(id, Functions.Saves.get(id)[1] + 1 if success else 0)

                Functions.set_stage(Constants.STAGES[3] if success else Constants.STAGES[2])
                Functions.Flags.testing = False

            sleep(0.1)

        sleep(0.35)

    Functions.clear()
    Functions.Saves.close()