'''
File that stores an Inventory class
'''

from colorama import Fore, Style
from defs import Constants, Functions
from pynput import keyboard
from random import randint

class Inventory:
    '''
    This class is used to manage the inventory of the player.
    '''

    def __init__(self) -> None:
        '''
        Initializes the inventory with 5 random blocks.
        '''
        self.__inventory: list[list[str]] = self.gen_blocks()
        self.__selected = 0
        self.__keys_pressed = set()

    def insertblock(self, index: int) -> None:
        '''
        Inserts a random block at a specific index in the inventory.
        :param index: index from 0
        '''
        if index < 0 or index > Constants.INVENTORY_CAPACITY - 1: raise IndexError("Index out of range")
        self.__inventory[index] = Constants.BLOCKS[randint(0, 9)]

    def getblock(self, index: int) -> list[str]:
        '''
        Returns the block at a specific index in the inventory.
        :param index: index from 0
        :return: block in list of 3 lines
        '''
        if index < 0 or index > Constants.INVENTORY_CAPACITY - 1: raise IndexError("Index out of range")
        return self.__inventory[index]
    
    def removeblock(self, index: int) -> None:
        '''
        Removes the block at a specific index in the inventory.
        :param index: index from 0
        '''
        if index < 0 or index > Constants.INVENTORY_CAPACITY - 1: raise IndexError("Index out of range")
        del self.__inventory[index]

    def selectblock(self, index: int) -> list[str]:
        '''
        Selects a block from the inventory and highlights it
        :param index: index from 0
        :return: block in list of 3 lines
        '''
        if index < 0 or index > Constants.INVENTORY_CAPACITY - 1: raise IndexError("Index out of range")

        self.__inventory[index] = [Fore.GREEN + i + Style.RESET_ALL for i in self.__inventory[index]]

        for i, b in enumerate(self.__inventory):
            if i != index: self.__inventory[i] = [l.replace(Fore.GREEN, '').replace(Style.RESET_ALL, '') for l in b]

        return self.__inventory[index]

    def gen_blocks(self) -> list[list[str]]: 
        '''
        Generates 5 random blocks and puts them in inventory
        :return: new inventory
        '''
        result = [list(Constants.BLOCKS[randint(0, 9)]) for i in range(Constants.INVENTORY_CAPACITY)]

        return result
    
    def print(self) -> None:
        '''
        Prints the current inventory
        '''
        separator = Constants.WIDTH * '-'
        print(separator)

        for i in range(3):
            print(''.join('    ' + self.__inventory[j][i] + '    ' for j in range(5)))
            
        print(separator)

    def getselected(self) -> int:
        '''
        Returns the currently selected block
        :return: selected block index
        '''
        return self.__selected
    
    # Functions for keylistener

    def on_press(self, key: int) -> bool:
        '''
        Function that is called when a key is pressed. Method for keylistener
        :param key: keycode
        ''' 
        if key == keyboard.Key.left and key not in self.__keys_pressed:
            self.__selected = (self.__selected - 1) % Constants.INVENTORY_CAPACITY
            self.selectblock(self.__selected)
            Functions.clear()
            self.print()
        elif key == keyboard.Key.right and key not in self.__keys_pressed:
            self.__selected = (self.__selected + 1) % Constants.INVENTORY_CAPACITY
            Functions.clear()
            self.selectblock(self.__selected)
            self.print()

        self.__keys_pressed.add(key)

    def on_release(self, key: int) -> bool:
        '''
        Function that is called when a key is released. Method for keylistener
        :param key: keycode
        '''
        try: self.__keys_pressed.remove(key)
        except KeyError: pass

    def __str__(self) -> str:
        '''
        Returns a string representation of the inventory.
        :return: string representation
        '''
        return "Inventory"
    
    # list string representation
    __repr__ = __str__