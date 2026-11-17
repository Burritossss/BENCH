'''Abstraction layer for writign UI's in BENCH easier'''
import curses
from typing import Any
from types import FunctionType
from emulator.exceptions import *

class Window:
    '''A window object with a title, position, and size'''
    def __init__(self, 
                 x:int, 
                 y:int, 
                 width:int, 
                 height:int,
                 name:str="Window"):
        self.name = name # Name for the window
        # Dynamics are dynamic items that are easy to update
        self.dynamics:dict[int,tuple[Any, int, int]] = {} # Format: <id>:(<value>, <x>, <y>)
        self.buttons:dict[int,tuple[str, int, int, FunctionType, bool]] = {} # Format: <id>:(<button_string>, <x>, <y>, <function>, <status>)
        self.window = curses.newwin(height, width, y, x)
        self.window.border()
        self.window.addstr(1, ((self.window.getmaxyx()[1] - len(self.name)) // 2), self.name)
        self.window.refresh() # Refresh the window

    def refresh(self):
        '''Manually refresh the window'''
        self.window.refresh()

    def add_dynamic(self, x:int, y:int, id:int, value:Any):
        '''Creates a dynamic value object.'''
        if id in self.dynamics:
            raise AlreadyExistsError(f"Dynamic with ID, {id}, already exists!")
        self.dynamics[id] = (value, x, y)
        self.window.addstr(y, x, str(value))
        self.window.refresh()

    def update_dynamic(self, id:int, value:Any):
        '''Updates a dynamic's value based on it's ID'''
        if id not in self.dynamics:
            raise KeyError(f'ID {id} does not exist!')
        _, x, y = self.dynamics[id] # Unpack the tuple
        self.dynamics[id] = (value, x, y) # Reassemble the tuple
        self.window.addstr(y, x, str(value)) # Add the string to the window
        self.window.refresh()

    def add_button(self, x:int, y:int, id:int, name:str, function:FunctionType, status:bool=False):
        '''Creates a dynamic button object'''
        if id in self.buttons:
            raise AlreadyExistsError(f'Button with ID, {id}, already exists!')
        self.buttons[id] = (name, x, y, function, status)
        self.window.addstr(y, x, name, curses.A_REVERSE if status else curses.A_NORMAL)
        self.window.refresh()