'''
File that adds class for game actionbar
'''
from colorama import *

from defs import Constants, Functions

class Actionbar:
    '''
    Class for game actionbar
    '''
    def __init__(self) -> None:
        '''
        Constructor
        '''
        self.__actions = []

    def __determine_actions(self) -> None:
        '''
        Method to determine actions based on game stage
        '''
        stage = Functions.get_stage()
        self.__actions.clear()

        if stage == Constants.STAGES[0]: 
            self.__actions.append(Constants.ACTIONS[1])
            self.__actions.append(Constants.ACTIONS[0])
            self.__actions.append(Constants.ACTIONS[3])
        elif stage == Constants.STAGES[1]: 
            self.__actions.append(Constants.ACTIONS[6])
            self.__actions.append(Constants.ACTIONS[7])
            self.__actions.append(Constants.ACTIONS[3])
        elif stage == Constants.STAGES[2]:
            pass
        elif stage == Constants.STAGES[3]:
            self.__actions.append(Constants.ACTIONS[9])
            self.__actions.append(Constants.ACTIONS[8])
            self.__actions.append(Constants.ACTIONS[3])
        elif stage == Constants.STAGES[4]:
            pass
        elif stage == Constants.STAGES[5]:
            self.__actions.append(Constants.ACTIONS[9])
            self.__actions.append(Constants.ACTIONS[8])
            self.__actions.append(Constants.ACTIONS[2])

        self.__actions.append(Constants.ACTIONS[5])


    def print(self) -> None: 
        '''
        Prints the actionbar
        '''
        self.__determine_actions()
        print("Actions:", '  '.join(map(str, self.__actions)))

    def __str__(self) -> str:
        '''
        String representation of actions of the actionbar
        '''
        return str(self.__actions)
    
    # string representation
    __repr__ = __str__