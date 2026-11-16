'''Abstraction layer for making windows in BENCH easier'''
import curses
from typing import Any
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
        self.window = curses.newwin(height, width, y, x)
        self.window.border()
        self.window.addstr(1, ((self.window.getmaxyx()[1] - len(self.name)) // 2), self.name)
        self.window.refresh() # Refresh the window

    def refresh(self):
        '''Manually refresh the window'''
        self.window.refresh()

    def add_dynamic(self, x:int, y:int, id:int, value:Any):
        '''Add's a dynamic value to the window with a starting value and an ID.'''
        if id in self.dynamics:
            raise AlreadyExistsError(f"ID {id} already exists!")
        self.dynamics[id] = (value, x, y)
        self.window.addstr(y, x, str(value))
        self.window.refresh()

    def update_dynamic(self, id:int, value:Any):
        '''Updates a dynamic's value based on it's ID'''
        if id not in self.dynamics:
            raise KeyError(f'ID {id} does not exist!')
        # Unpack the tuple (because they are immutable......)
        _, x, y = self.dynamics[id]
        self.dynamics[id] = (value, x, y)

        self.window.addstr(y, x, str(value))
        self.window.refresh()