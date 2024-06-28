'''
File that adds class for game actionbar
'''
from colorama import *

from defs import Constants, Functions

class Actionbar:
    '''
    Class for game actionbar
    '''
    def print(self) -> None: 
        '''
        Prints the actionbar
        '''
        print(self.__str__())

    def __str__(self) -> str:
        '''
        String representation of actions of the actionbar
        '''
        return "Actions: " + '  '.join(Constants.ACTIONS[Functions.get_stage()])
    
    # string representation
    __repr__ = __str__