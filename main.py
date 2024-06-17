from pynput import keyboard

# print('Press s or n to continue:')

# with keyboard.Events() as events:
#     # Block for as much as possible
#     event = events.get(1e6)
#     if event.key == keyboard.KeyCode.from_char('s'):
#         print("YES")

import os
from colorama import just_fix_windows_console

from inventory import Inventory
from keyhandler import KeyFunctions

class Main:
    just_fix_windows_console() 

    inv = Inventory()
    inv_keylistener = keyboard.Listener(inv.on_press, inv.on_release)
    inv_keylistener.start()
    inv.print()
    inv_keylistener.join()

# os.system('cls')
# # draw interface
# Colorprint.formatprint(" Bridge Builder                                                  ", bg = Colorprint.Background.MAGENTA)
# for i in range(8): Colorprint.formatprint(WIDTH * " ", bg = Colorprint.Background.CYAN)
# colortable.ColorTable
# # draw inventory for blocks