'''
File that stores constants and functions for the game
'''
from os import name, system
from colorama import Style, Back

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
    STAGES = ("Selection", "Placing", "Placed", "Testing", "Testing Failed", "Testing Succeeded","Menu")

class Functions:
    '''
    Class that stores essential functions and variables
    '''
    __stage = Constants.STAGES[0]
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
        char = list(set([*result[0]]))[0]
        
        for i in range(len(result)):
            result[i] = (str(result[i]).center(5) if center else str(result[i])) \
                .replace(' ', space_color + ' ' + Style.RESET_ALL) \
                .replace(char, char_color + char + Style.RESET_ALL)
        
        return result


        