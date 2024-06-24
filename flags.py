'''
File that manages the flags needed for working of the game
'''

class Flags:
    '''
    Class that manages the flags needed for working of the game
    '''

    def __init__(self):
        '''
        Initializes the flags
        '''
        self.restart = False
        self.block_placed = False
        self.close = False
        self.menu = False

    @property
    def restart(self) -> bool:
        '''
        Getter for the restart flag
        '''
        return self.__restart

    @restart.setter
    def restart(self, value: bool) -> None:
        '''
        Setter for the restart flag
        '''
        if type(value) != bool: raise TypeError("Value must be a boolean")
        self.__restart = value

    @property
    def block_placed(self) -> bool:
        '''
        Getter for the block placed flag
        '''
        return self.__block_placed

    @block_placed.setter
    def block_placed(self, value: bool) -> None:
        '''
        Setter for the block placed flag
        '''
        if type(value) != bool: raise TypeError("Value must be a boolean")
        self.__block_placed = value

    @property
    def close(self) -> bool:
        '''
        Getter for the close flag
        '''
        return self.__close

    @close.setter
    def close(self, value: bool) -> None:
        '''
        Setter for the close flag
        '''
        if type(value) != bool: raise TypeError("Value must be a boolean")
        self.__close = value

    @property
    def menu(self) -> bool:
        '''
        Getter for the close flag
        '''
        return self.__menu

    @menu.setter
    def menu(self, value: bool) -> None:
        '''
        Setter for the menu flag
        '''
        if type(value) != bool: raise TypeError("Value must be a boolean")
        self.__menu = value
    

    