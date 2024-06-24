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
        self.__top_padding = 0
        self.__selected_block_list = None

        self.gen_padding()
        self.construct()

        self.__blockpos_x = Constants.MAP_LAND_LENGTH + 0
        self.__blockpos_y = self.__top_padding + 0

    def gen_padding(self) -> None:
        '''
        Generates the top padding of the map
        '''
        self.__top_padding = randint(2, 4)

    def construct(self):
        '''
        Constructs the map according to the top padding
        '''
        # generating upper layer
        self.__lines[self.__top_padding] = self.gen_layer('~', ' ', char_color=Back.GREEN, space_color=Back.CYAN)
        
        # generate other layers
        for i in range(Constants.MAP_HEIGHT):
            if i < self.__top_padding: self.__lines[i] = Back.CYAN + (Constants.WIDTH * ' ') + Style.RESET_ALL # top
            elif i == Constants.MAP_HEIGHT - 1: self.__lines[i] = self.gen_layer('|', '^', char_color=Back.LIGHTBLACK_EX, space_color=Back.BLUE) # bottom
            elif i > self.__top_padding: self.__lines[i] = self.gen_layer('|', ' ', char_color=Back.LIGHTBLACK_EX, space_color=Back.CYAN) # middle

    def gen_layer(self, char: str, spacechar: str, char_color: str = '', space_color: str = '') -> str:
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
        # print(*self.__lines, sep='\n')
        for i in self.__lines:
            print(i, len(i))

    # Block functions

    def set_selected_block(self, index: int) -> None:
        '''
        Sets selected block index
        :param index: block index in block list
        '''
        self.__selected_block_list = index

    def place_block(self, index_list: int) -> bool:
        '''
        Places block on x and y position
        :param index_list: index of block in block list
        :return: True if block is placed, False if not
        '''
        block = list(filter(None, Constants.BLOCKS[index_list]))

        for i in range(len(block)):
            line = [*self.__lines[self.__blockpos_y + i]]

            k = 0
            x = self.__blockpos_x - Constants.MAP_LAND_LENGTH
            for j in range(len(line)):
                if line[j] == ' ': 
                    if k >= x and k < x + len(block[i]): 
                        line[j] = block[i][k - x]             
                    k += 1

            self.__lines[self.__blockpos_y + i] = ''.join(line)

    def move_block(self, x: int, y: int) -> None:
        '''
        Moves the block to the specified position in map
        :param x: x position
        :param y: y position        
        '''
        max_width = Constants.WIDTH - Constants.MAP_LAND_LENGTH - len(Constants.BLOCKS[self.__selected_block_list][0])
        max_height = Constants.MAP_HEIGHT - 1 - len(list(filter(None, Constants.BLOCKS[self.__selected_block_list])))

        if x >= Constants.MAP_LAND_LENGTH and x <= max_width: self.__blockpos_x = x
        if y >= self.__top_padding and y <= max_height: self.__blockpos_y = y

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
            self.move_block(self.__blockpos_x - 1, self.__blockpos_y)            
        elif key == keyboard.Key.right and key not in Functions.keys_pressed:
            self.move_block(self.__blockpos_x + 1, self.__blockpos_y)
        elif key == keyboard.Key.up and key not in Functions.keys_pressed:
            self.move_block(self.__blockpos_x, self.__blockpos_y - 1)
        elif key == keyboard.Key.down and key not in Functions.keys_pressed:
            self.move_block(self.__blockpos_x, self.__blockpos_y + 1)
        elif key == keyboard.Key.enter and key not in Functions.keys_pressed:
            Functions.Flags.block_placed = True
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
    