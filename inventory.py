'''
File that stores an Inventory class
'''

from colorama import Fore, Style
from pynput import keyboard
from random import randint

from defs import Constants, Functions

class Inventory:
    '''
    This class is used to manage the inventory of the player.
    '''

    def __init__(self) -> None:
        '''
        Initializes the inventory with 5 random blocks.
        '''
        self.__inventory: list[list[str]] = []
        self.__highlighted = 0
        self.__selected = None

        self.gen_blocks()

    def get_block(self, index: int) -> list[str]:
        '''
        Returns the block at a specific index in the inventory.
        :param index: index from 0
        :return: block in list of 3 lines
        '''
        if index < 0 or index > Constants.INVENTORY_CAPACITY - 1: raise IndexError("Index out of range")
        return self.__inventory[index]
    
    def remove_block(self, index: int) -> None:
        '''
        Removes the block and insert new at a specific index in the inventory.
        :param index: index from 0
        '''
        if index < 0 or index > Constants.INVENTORY_CAPACITY - 1: raise IndexError("Index out of range")
        self.__inventory[index] = Constants.BLOCKS[randint(0, 9)]

    def gen_blocks(self) -> None: 
        '''
        Generates random blocks and puts them in clear inventory
        '''
        self.__inventory.clear()

        for i in range(Constants.INVENTORY_CAPACITY):
            self.__inventory.append(Constants.BLOCKS[randint(0, 9)])       
    
    def print(self) -> None:
        '''
        Prints the current inventory
        '''
        # get copy of inventory and highlight the correct block
        copy = list(self.__inventory)
        copy[self.__highlighted] = Functions.highlight_block(copy[self.__highlighted], Fore.GREEN, center=True) 

        for i, b in enumerate(copy):
            if i != self.__highlighted: copy[i] = [l.replace(Fore.GREEN, '').replace(Style.RESET_ALL, '') for l in b]

        separator = Constants.WIDTH * '-'
        print(separator)

        for i in range(3):
            print(''.join('    ' + copy[j][i].center(5) + '    ' for j in range(5)))
            
        print(separator)

    def getselected_list(self) -> int:
        '''
        Returns the currently selected block. -1 if block is not found
        :return: selected block index for blocks list
        '''
        for i in range(len(Constants.BLOCKS)): 
            if Constants.BLOCKS[i][0] == self.get_block(self.__selected)[0]: return i

        return -1
    
    def getselected_inv(self) -> int:
        '''
        Returns the currently selected block in inventory
        :return: selected block index for inventory
        '''
        return self.__selected
     
    def resetselected(self) -> None:
        '''
        Resets the selected block and sets it to 0
        '''
        self.__selected = 0
    
    # Functions for keylistener

    def on_press(self, key: int) -> bool:
        '''
        Function that is called when a key is pressed. Method for keylistener
        :param key: keycode
        ''' 
        if not Functions.get_stage() == Constants.STAGES[0]: return

        if key == keyboard.Key.left and key not in Functions.keys_pressed:
            self.__highlighted = (self.__highlighted - 1) % Constants.INVENTORY_CAPACITY
        elif key == keyboard.Key.right and key not in Functions.keys_pressed:
            self.__highlighted = (self.__highlighted + 1) % Constants.INVENTORY_CAPACITY
        elif key == keyboard.Key.enter and key not in Functions.keys_pressed:
            self.__selected = self.__highlighted
            Functions.set_stage(Constants.STAGES[1])
        elif key == keyboard.Key.esc and key not in Functions.keys_pressed: 
            Functions.set_stage(Constants.STAGES[4])
        elif key == keyboard.KeyCode.from_char('r') and key not in Functions.keys_pressed:
            Functions.Flags.restart = True
            Functions.set_stage(Constants.STAGES[4])
        elif key == keyboard.KeyCode.from_char('t') and key not in Functions.keys_pressed:
            Functions.Flags.testing = True

        Functions.keys_pressed.add(key)

    def on_release(self, key: int) -> bool:
        '''
        Function that is called when a key is released. Method for keylistener
        :param key: keycode
        '''
        try: Functions.keys_pressed.remove(key)
        except KeyError: pass

    def __str__(self) -> str:
        '''
        Returns a string representation of the inventory.
        :return: string representation
        '''
        return "Inventory"
    
    # list string representation
    __repr__ = __str__