'''
File that stores classes needed for game map
'''
from random import randint
from pynput import keyboard
from colorama import Back, Style

from defs import Constants, Functions

class Map:
    '''
    Class that represents the game map
    '''
    def __init__(self):
        '''
        Initializes the map
        '''
        self.__lines = ['' for i in range(Constants.MAP_HEIGHT)]
        self.__top_padding = randint(2, 4)
        self.fillmap(self.__top_padding)

        self.__blockpos_x = Constants.MAP_LAND_LENGTH + 0
        self.__blockpos_y = self.__top_padding + 0

    def get_top_padding(self) -> int:
        '''
        Returns the top padding of the map
        '''
        return self.__top_padding

    def fillmap(self, top_padding: int):
        '''
        Generates the map
        :param top_padding: the space between grass and top
        '''
        # generating upper layer
        self.__lines[top_padding] = self.genlayer('~', ' ', char_color=Back.GREEN, space_color=Back.CYAN)
        
        # generate other layers
        for i in range(Constants.MAP_HEIGHT):
            if i < top_padding: self.__lines[i] = Back.CYAN + (Constants.WIDTH * ' ') + Style.RESET_ALL # top
            elif i == Constants.MAP_HEIGHT - 1: self.__lines[i] = self.genlayer('|', '^', char_color=Back.LIGHTBLACK_EX, space_color=Back.BLUE) # bottom
            elif i > top_padding: self.__lines[i] = self.genlayer('|', ' ', char_color=Back.LIGHTBLACK_EX, space_color=Back.CYAN) # middle

    def genlayer(self, char: str, spacechar: str, char_color: str = '', space_color: str = '') -> str:
        '''
        Generates a single layer of the map land
        :param char: character to use for land
        :param spacechar: character to use for spaces
        :param char_color: color to use for land character 
        :param space_color: color to use for spaces
        '''
        land = char_color + (Constants.MAP_LAND_LENGTH * char) + Style.RESET_ALL
        space = space_color + ((Constants.WIDTH - Constants.MAP_LAND_LENGTH * 2) * spacechar) + Style.RESET_ALL

        return land + space + land
    
    def print(self) -> None:
        '''
        Prints the map
        '''
        print(*self.__lines, sep='\n')

    # Block moving

    def move_block(self, x: int, y: int) -> None:
        '''
        Moves the block to the specified position in map
        :param x: x position
        :param y: y position        
        '''
        self.__blockpos_x = Constants.MAP_LAND_LENGTH + x
        self.__blockpos_y = 1 + self.__top_padding + y

    def get_blockpos_x(self) -> int:
        '''
        Returns the x position of the block
        '''
        return self.__blockpos_x
    
    def get_blockpos_y(self) -> int:
        '''
        Returns the y position of the block
        '''
        return self.__blockpos_y
    
    # Keylistener functions

    def on_press(self, key) -> None:
        '''
        Listens for keyboard input and moves the block accordingly with arrows. Method for keylistener
        :param key: key pressed
        '''
        if not Functions.get_stage() == Constants.STAGES[1]: return

        if key == keyboard.Key.left and key not in Functions.keys_pressed:
            self.move_block((self.__blockpos_x - 1) % Constants.WIDTH - Constants.MAP_LAND_LENGTH * 2, self.__blockpos_y)            
        elif key == keyboard.Key.right and key not in Functions.keys_pressed:
            self.move_block((self.__blockpos_x + 1) % Constants.WIDTH - Constants.MAP_LAND_LENGTH * 2, self.__blockpos_y)
        elif key == keyboard.Key.up and key not in Functions.keys_pressed:
            self.move_block(self.__blockpos_x, (self.__blockpos_y + 1) % Constants.MAP_HEIGHT - 1)
        elif key == keyboard.Key.down and key not in Functions.keys_pressed:
            self.move_block(self.__blockpos_x, (self.__blockpos_y - 1) % Constants.MAP_HEIGHT - 1)
        elif key == keyboard.Key.enter and key not in Functions.keys_pressed:
            Functions.set_stage(Constants.STAGES[0])
        # elif key == keyboard.KeyCode.from_char('x'):
        #     Stages.set_stage(Constants.STAGES[0])
        #     self.__block_selected = None
        #     self.move_block(0, 0)

        Functions.keys_pressed.add(key)

    def on_release(self, key) -> None:
        '''
        Removes the key from the set when released. Method for keylistener
        :param key: key released
        '''
        try: Functions.keys_pressed.remove(key)
        except KeyError: pass

    def __str__(self) -> str:
        '''
        Returns the map string representation
        :return: the list of map lines
        '''
        return str(self.__lines)
    
    # string representation
    __repr__ = __str__
    