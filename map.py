'''
File that stores classes needed for game map
'''
from random import randint
from defs import Constants

class Map:
    '''
    Class that represents the game map
    '''
    def __init__(self):
        '''
        Initializes the map
        '''
        self.__lines = list()
        self.gen()

    def gen(self):
        '''
        Generates the map
        '''
        # generating upper layer
        top_padding = randint(0, 3)
        self.__lines.insert(top_padding, self.genlayer('~', ' '))
        
        # generate other layers
        for i in range(Constants.MAP_HEIGHT):
            if i <= top_padding: self.__lines.insert(i, Constants.WIDTH * ' ') # top
            elif i == Constants.MAP_HEIGHT - 1: self.__lines.insert(i, self.genlayer('|', '^')) # bottom
            else: self.__lines.insert(i, self.genlayer('|', ' ')) # middle

    def genlayer(self, char: str, spacechar: str) -> str:
        '''
        Generates a single layer of the map land
        :param char: character to use
        :param spacechar: character to use for spaces
        '''
        land = Constants.MAP_LAND_LENGTH * char
        space = (Constants.WIDTH - Constants.MAP_LAND_LENGTH * 2) * spacechar
        return land + space + land
    

    def get(self) -> list:
        '''
        Returns the map
        :return: the list of map lines
        '''
        return self.__lines
    
map = Map()
for l in map.get():
    print(l)