'''
File that stores functions for key listeners
'''
from pynput import keyboard

class KeyFunctions:
    '''
    Class that stores functions needed for key listeners
    '''
    def __init__(self):
        '''
        Initializes the class
        '''
        self.__keys_pressed = set()
        self.__listener = keyboard.Listener(on_press=self.__on_press, on_release=self.__on_release)
        self.__listener.start()
        
    def __on_press(self, key: int) -> bool:
        '''
        Function that is called when a key is pressed
        :param key: keycode
        '''
        if key == keyboard.Key.esc:
            # Stop listener
            return False
        
        self.__keys_pressed.add(key)

    def __on_release(self, key: int) -> bool:
        '''
        Function that is called when a key is released
        :param key: keycode
        '''
        try: self.__keys_pressed.remove(key)
        except KeyError: pass
            
    def keyspressed(self) -> set:
        '''
        Returns a set of keys that are currently pressed
        '''
        return self.__keys_pressed