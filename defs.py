'''
File that stores constants and functions for the game
'''
from os import name, system
from colorama import Style
from pynput import keyboard
import webbrowser

from flags import Flags
from saves import Saves

class Constants:
    '''
    Class that stores constants for the game
    '''
    GITHUB_LINK = "https://github.com/WardenHD/Bridge-Builder"
    LICENSE_LINK = "https://github.com/WardenHD/Bridge-Builder/blob/main/LICENSE"

    # Block variables
    # Block variants list - tuple of 3 lines
    BLOCKS: list[tuple] = [
        ('*****', '', ''), 
        ('@@@', '', ''),
        ('&&&&&', '&    ', '&    '),  
        ('###  ', '  ###', ''), 
        ('  >>>', '>>>  ', ''),
        ('<<<<<', '    <', '    <'), 
        ('?????', '  ?  ', '  ?  '), 
        (':', ':', ':'), 
        (' ; ; ', ';;;;;', ';   ;'), 
        ('  $$$', '  $  ', '$$$  ')
    ]

    BLOCK_LINES = 3
    BLOCK_CHARS = ''.join(set(''.join([i for sub in BLOCKS for i in sub])))

    # Screen size
    WIDTH = 65
    HEIGHT = 25
    TITLE_BAR = 'BRIDGE BUILDER'

    # Map constants
    MAP_HEIGHT = 10
    MAP_LAND_LENGTH = 5

    # Inventory capacity
    INVENTORY_CAPACITY = 5

    # Game stages
    STAGES = ("Selection", "Placing", "Testing Failed", "Testing Suceeded", "Menu", "About", "Profiles")

    # Actions for actionbar  
    ACTIONS = {
        STAGES[0]: ("Select(Arrows, Enter)", "Test(T)", "Restart(R)", "Menu(Esc)"),
        STAGES[1]: ("Place(Enter)", "Move(Arrows)", "Reset Pos(R)", "Cancel(Esc)"),
        STAGES[2]: ("Menu(Enter)", "Exit(Esc)"),
        STAGES[3]: ("New Game(Enter)", "Menu(Esc)"),
        STAGES[4]: ("Start(Enter)", "Profiles(P)", "About(A)", "Exit(Esc)"),
        STAGES[5]: ("Github Page(G)", "License(L)", "Menu(Esc)"),
        STAGES[6]: ("Select(Arrows, Enter)", "New(N)", "Delete(D)", "Menu(Esc)")
    }

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

    ABOUT = '''
Bridge Builder is a game where you should build a bridge.
To win, the first line of the bridge mustn't have spaces and
other lines nust have at least 3 different types of blocks.

Notes:
The map is flat, but generated with different elevation.
The blocks that are placed cannot be removed.
If you lose, the score will be 0.\n
'''

class Functions:
    '''
    Class that stores essential functions and variables
    '''
    __stage = Constants.STAGES[4]
    __selected_profile_id = 1
    __highlighted_profile_id = 0
    
    Flags = Flags()
    Saves = Saves()
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
                result[i][j] = space_color + ' ' + Style.RESET_ALL if result[i][j] == ' ' else char_color + result[i][j] + Style.RESET_ALL
            
            result[i] = ''.join(result[i])
        
        return result
    
    @staticmethod
    def get_selected_profile() -> int:
        '''
        Getter for the selected profile id
        '''
        return Functions.__selected_profile_id
    
    @staticmethod
    def get_highlighted_profile() -> int:
        '''
        Getter for the highlighted profile in terms of list of all profiles
        '''
        return Functions.__highlighted_profile_id

    # Handlers for generic keylistener

    def genkeylistener_on_press(key: int) -> bool:
        '''
        Function that is called when a key is pressed. Method for keylistener
        :param key: keycode
        :return: whether to stop the listener
        '''
        if Functions.__stage == Constants.STAGES[4]: 
            if key == keyboard.Key.esc and key not in Functions.keys_pressed: 
                Functions.Flags.close = True
            elif key == keyboard.Key.enter and key not in Functions.keys_pressed:
                Functions.set_stage(Constants.STAGES[0])
            elif key == keyboard.KeyCode.from_char('p') and key not in Functions.keys_pressed:
                Functions.set_stage(Constants.STAGES[6])
            elif key == keyboard.KeyCode.from_char('a') and key not in Functions.keys_pressed:
                Functions.set_stage(Constants.STAGES[5])
        elif Functions.__stage == Constants.STAGES[6]:
            if key == keyboard.Key.esc and key not in Functions.keys_pressed:
                Functions.set_stage(Constants.STAGES[4])
            elif key == keyboard.KeyCode.from_char('n') and key not in Functions.keys_pressed: 
                Functions.Saves.add()
            elif key == keyboard.KeyCode.from_char('d') and key not in Functions.keys_pressed: 
                Functions.Saves.delete(Functions.Saves.get_all()[Functions.__highlighted_profile_id][0])
            elif key == keyboard.Key.up and key not in Functions.keys_pressed:
                Functions.__highlighted_profile_id = (Functions.__highlighted_profile_id - 1) % len(Functions.Saves.get_all())
            elif key == keyboard.Key.down and key not in Functions.keys_pressed:
                Functions.__highlighted_profile_id = (Functions.__highlighted_profile_id + 1) % len(Functions.Saves.get_all())
            elif key == keyboard.Key.enter and key not in Functions.keys_pressed:
                Functions.__selected_profile_id = Functions.Saves.get_all()[Functions.__highlighted_profile_id][0]
                Functions.set_stage(Constants.STAGES[4])
        elif Functions.__stage == Constants.STAGES[2]: 
            if key == keyboard.Key.enter and key not in Functions.keys_pressed:
                Functions.set_stage(Constants.STAGES[4])
            if key == keyboard.Key.esc and key not in Functions.keys_pressed:
                Functions.Flags.close = True
        elif Functions.__stage == Constants.STAGES[3]: 
            if key == keyboard.Key.enter and key not in Functions.keys_pressed:
                Functions.Flags.restart = True
                Functions.set_stage(Constants.STAGES[4])
            if key == keyboard.Key.esc and key not in Functions.keys_pressed:
                Functions.set_stage(Constants.STAGES[4])
        elif Functions.__stage == Constants.STAGES[5]: 
            if key == keyboard.KeyCode.from_char('g') and key not in Functions.keys_pressed:
                webbrowser.open_new_tab(Constants.GITHUB_LINK)
            elif key == keyboard.KeyCode.from_char('l') and key not in Functions.keys_pressed:
                webbrowser.open_new_tab(Constants.LICENSE_LINK)
            elif key == keyboard.Key.esc and key not in Functions.keys_pressed:
                Functions.set_stage(Constants.STAGES[4])

        Functions.keys_pressed.add(key)

    def genkeylistener_on_release(key: int) -> bool:
        '''
        Function that is called when a key is released. Method for keylistener
        :param key: keycode
        :return: whether to stop the listener
        '''
        try: Functions.keys_pressed.remove(key)
        except KeyError: pass