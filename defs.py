'''
File that stores constants and functions for the game
'''
from os import name, system
from colorama import Style, Back
from pynput import keyboard

from flags import Flags

class Constants:
    '''
    Class that stores constants for the game
    '''

    # Block variables
    # Block variants list - tuple of 3 lines
    BLOCKS: list[tuple] = [
        ('*****', '', ''), 
        ('@@@', '', ''),
        ('&&&&&', '&    ', '&    '),  
        ('###  ', '  ###', ''), 
        ('  >>>', '>>>  ', ''),
        ('<<<<<', '    <', '    <'), 
        ('~~~~~', '  ~  ', '  ~  '), 
        (':', ':', ':'), 
        (' ; ; ', ';;;;;', ';   ;'), 
        ('  $$$', '  $  ', '$$$  ')
    ]

    BLOCK_LINES = 3
    BLOCK_COLORS = (Back.RED, Back.BLACK, Back.WHITE)

    # Screen size
    WIDTH = 65
    HEIGHT = 25
    TITLE_BAR = 'BRIDGE BUILDER'

    # Map constants
    MAP_HEIGHT = 10
    MAP_LAND_LENGTH = 5

    # Inventory capacity
    INVENTORY_CAPACITY = 5

    # Actions for actionbar
    ACTIONS = ("Select(Enter)", "Move(Left, Right)", "Info(I)", "Restart(R)", "Test(T)", "Exit(Esc)", 
               "Place(Enter)", "Move(Arrows)", "Profiles(P)", "Start(Enter)")

    # Game stages
    STAGES = ("Selection", "Placing", "Testing", "You lose", "Testing Suceeded", "Menu")

    # Logo
    TITLE_LOGO = (
        (
            ' ______  ______  __  _____   ______  ______',
            '/\\  == \\/\\  == \\/\\ \\/\\  __-./\\  ___\\/\\  ___\\',
            '\\ \\  __<\\ \\  __<\\ \\ \\ \\ \\/\\ \\ \\ \\__ \\ \\  __\\',
            '   \\ \\_____\\ \\_\\ \\_\\ \\_\\ \\____-\\ \\_____\\ \\_____\\',
            '    \\/_____/\\/_/ /_/\\/_/\\/____/ \\/_____/\\/_____/'
        ), 
        (
            ' ______  __  __  __  __      _____   ______  ______',
            '/\\  == \\/\\ \\/\\ \\/\\ \\/\\ \\    /\\  __-./\\  ___\\/\\  == \\',
            '\\ \\  __<\\ \\ \\_\\ \\ \\ \\ \\ \\___\\ \\ \\/\\ \\ \\  __\\\\ \\  __<',
            '   \\ \\_____\\ \\_____\\ \\_\\ \\_____\\ \\____-\\ \\_____\\ \\_\\ \\_\\',
            '    \\/_____/\\/_____/\\/_/\\/_____/\\/____/ \\/_____/\\/_/ /_/'
        )
    )

class Functions:
    '''
    Class that stores essential functions and variables
    '''
    __stage = Constants.STAGES[0]
    
    Flags = Flags()
    keys_pressed = set()

    @staticmethod
    def clear() -> None:
        '''
        Clears the console
        '''
        if name == 'nt': system('cls')
        else: system('clear')

    @staticmethod
    def cursor_pos(x: int, y: int) -> None:
        '''
        Moves the cursor to the specified position by using ANSI escape codes
        :param x: x position (begin from 0)
        :param y: y position (begin from 0)
        '''
        print(f'\x1B[{y + 2};{x + 1}f', end='')

    @staticmethod
    def get_stage() -> str:
        '''
        Getter for the current game stage
        '''
        return Functions.__stage
    
    @staticmethod
    def set_stage(value: str) -> None:
        '''
        Setter for the current game stage
        '''
        if value in Constants.STAGES: Functions.__stage = value
        else: raise ValueError("Invalid game stage")

    @staticmethod
    def highlight_block(block: list[str], char_color: str = '', space_color = '', center: bool = False) -> list[str]:
        '''
        Returns a list of strings representing a highlighted block
        :param block: index of the block in block list
        :param char_color: color of the character
        :param space_color: color of the space
        :param center: whether to center the block with width 5
        :return: list of 3 highlighted block lines
        '''
        result = list(block)
        
        for i in range(len(result)):
            if center: result[i] = list(result[i].center(5))
            else: result[i] = list(result[i])

            for j in range(len(result[i])):
                result[i][j] = space_color + ' ' if result[i][j] == ' ' else char_color + result[i][j] + Style.RESET_ALL
            
            result[i] = ''.join(result[i])
        
        return result

    # Handlers for generic keylistener

    def genkeylistener_on_press(key: int) -> bool:
        '''
        Function that is called when a key is pressed. Method for keylistener
        :param key: keycode
        :return: whether to stop the listener
        ''' 
        if key == keyboard.Key.esc and key not in Functions.keys_pressed: 
            if Functions.__stage == Constants.STAGES[5]: Functions.Flags.close = True
        elif key == keyboard.Key.enter and key not in Functions.keys_pressed:
            if Functions.__stage == Constants.STAGES[5]: Functions.Flags.menu = False
        Functions.keys_pressed.add(key)

    def genkeylistener_on_release(key: int) -> bool:
        '''
        Function that is called when a key is released. Method for keylistener
        :param key: keycode
        :return: whether to stop the listener
        '''
        try: Functions.keys_pressed.remove(key)
        except KeyError: pass
        