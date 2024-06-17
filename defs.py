'''
File that stores constants for the game
'''
from os import name, system

class Constants:
    '''
    Class that stores constants for the game
    '''

    # Block variants list - tuple of 3 lines
    BLOCKS: list[tuple] = [
        ('     ', '*****', '     '), 
        ('     ', ' *** ', '     '),
        ('*****', '*    ', '*    '),  
        ('***  ', '  ***', '     '), 
        ('  ***', '***  ', '     '),
        ('**** ', '*    ', '*    '), 
        ('**** ', '   * ', '   * '), 
        ('  *  ', '  *  ', '  *  '), 
        (' * * ', '*****', '*   *'), 
        ('  ***', '  *  ', '***  ')
    ]

    # Block lines
    BLOCK_LINES = 3

    # Screen size
    WIDTH = 65
    HEIGHT = 25

    # Map size
    MAP_HEIGHT = 10
    MAP_LAND_LENGTH = 5

    # Inventory capacity
    INVENTORY_CAPACITY = 5

    # Actions for actionbar
    ACTIONS = ("Select(Enter)", "Move(Left, Right)", "Info(I)", "Restart(R)", "Test(T)", "Exit(Esc)", 
               "Place(Enter)", "Move(Up, Left, Right, Down)", "Profiles(P)")

    # Game stages
    STAGES = ("Selection", "Placing", "Menu")

class Functions:
    '''
    Class that stores essential functions
    '''

    def clear() -> None:
        '''
        Clears the console
        '''
        if name == 'nt': system('cls')
        else: system('clear')
