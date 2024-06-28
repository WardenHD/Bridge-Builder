'''
File that has methods to manage game's title
'''
from colorama import Back, Style

from defs import Constants, Functions

class Title:
    '''
    Class that adds title features
    '''
    def __init__(self, title: str) -> None:
        '''
        Constructor
        :param title: title on the top
        ''' 
        self.__title = title
    
    def print(self) -> None:
        '''
        Prints the title
        '''
        wins_str = 'Wins: ' + str(Functions.Saves.get(Functions.get_selected_profile())[1]) + '  '
        profile_str = 'Profile ' + str(Functions.get_selected_profile()) + '  '
        footer = wins_str if Functions.get_stage() == Constants.STAGES[2] or Functions.get_stage() == Constants.STAGES[3] else profile_str
        spaces = (Constants.WIDTH - len(self.__title) - len(Functions.get_stage()) - 4 - len(footer)) * ' '

        print(f'{Back.RED} {self.__title} - {Functions.get_stage() + spaces + footer}{Style.RESET_ALL}')

    def __str__(self) -> str:
        '''
        Returns the title as a string
        '''
        return self.__title
    
    # string representation
    __repr__ = __str__