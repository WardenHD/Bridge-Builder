'''
File that stores constants for the game
'''
from os import name, system
from colorama import Back, Style

class Constants:
    '''
    Class that stores constants for the game
    '''

    # Block variants list - tuple of 3 lines
    BLOCKS: list[tuple] = [
        ('     ', '*****', '     '), 
        ('     ', ' @@@ ', '     '),
        ('&&&&&', '&    ', '&    '),  
        ('###  ', '  ###', '     '), 
        ('  >>>', '>>>  ', '     '),
        ('<<<< ', '<    ', '<    '), 
        ('~~~~ ', '   ~ ', '   ~ '), 
        ('  :  ', '  :  ', '  :  '), 
        (' ; ; ', ';;;;;', ';   ;'), 
        ('  $$$', '  $  ', '$$$  ')
    ]

    # Block lines
    BLOCK_LINES = 3

    # Screen size
    WIDTH = 65
    HEIGHT = 25
    TITLE = 'BRIDGE BUILDER'

    # Map constants
    MAP_HEIGHT = 10
    MAP_LAND_LENGTH = 5

    # Inventory capacity
    INVENTORY_CAPACITY = 5

    # Actions for actionbar
    ACTIONS = ("Select(Enter)", "Move(Left, Right)", "Info(I)", "Restart(R)", "Test(T)", "Exit(Esc)", 
               "Place(Enter)", "Move(Up, Left, Right, Down)", "Profiles(P)")

    # Game stages
    STAGES = ("Selection", "Placing", "Testing", "Menu")

class Functions:
    '''
    Class that stores essential functions and variables
    '''
    __stage = Constants.STAGES[0]
    keys_pressed = set()

    def clear() -> None:
        '''
        Clears the console
        '''
        if name == 'nt': system('cls')
        else: system('clear')

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