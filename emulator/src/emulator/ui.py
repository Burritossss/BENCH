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
                 name:str="Window",
                 border:bool=True):
        self.name = name # Name for the window
        # Dynamics are dynamic items that are easy to update
        self.dynamics:dict[int,tuple[Any, int, int]] = {} # Format: <id>:(<value>, <x>, <y>)
        self.buttons:dict[int,tuple[str, int, int, FunctionType|None]] = {} # Format: <id>:(<text>, <x>, <y>, <function>)
        self.toggles:dict[int,tuple[str, int, int, Any, bool]] = {} # Format: <id>:(<text>, <x>, <y>, <function>, <state>)
        # Initialize the window
        self.window = curses.newwin(height, width, y, x)
        self.window.nodelay(True) # No delay mode on
        self.window.keypad(True) # Turn on the mode that translates multisequence escape sequences into a readable constant
        if border: # Check if we want a border
            self.window.border() # and add a border
        if name: # Check if name is not an empty string
            self.window.addstr(1, ((self.window.getmaxyx()[1] - len(self.name)) // 2), self.name)
        self.window.refresh() # Refresh the window

    def refresh(self):
        '''Manually refresh the window'''
        self.window.refresh()

    def add_dynamic(self, x:int, y:int, id:int, value:Any):
        '''Creates a dynamic value object.'''
        if id in self.dynamics: # Check if the ID already exists
            # If so, throw an already exists error
            raise AlreadyExistsError(f"Dynamic with ID, {id}, already exists!")
        self.dynamics[id] = (value, x, y) # Create the dynamic value
        self.window.addstr(y, x, str(value)) # Create a string on the window
        self.window.refresh() # Refresh the window

    def update_dynamic(self, id:int, value:Any):
        '''Updates a dynamic's value based on it's ID'''
        if id not in self.dynamics: # Check if the ID does not exist
            # If so, throw a Key Error
            raise KeyError(f'ID {id} does not exist!')
        _, x, y = self.dynamics[id] # Unpack the tuple
        self.dynamics[id] = (value, x, y) # Reassemble the tuple
        self.window.addstr(y, x, str(value)) # Add the string to the window
        self.window.refresh()

    def add_button(self, x:int, y:int, id:int, text:str, function:FunctionType|None):
        '''Creates a dynamic button object'''
        if id in self.buttons: # Check if the ID already exists
            # If so, throw an already exists error
            raise AlreadyExistsError(f'Button with ID, {id}, already exists!')
        self.buttons[id] = (text, x, y, function if function else None) # Create the button
        self.window.addstr(y, x, text, curses.A_UNDERLINE) # Create a string on the window
        self.window.refresh() # Refresh the screen

    def tick_all_buttons(self):
        '''Ticks all buttons connected to this window'''
        if self.window.getch() == curses.KEY_MOUSE: # Check if the mouse pointer is being polled
            _, mouse_x, mouse_y, _, b_state = curses.getmouse() # Get the x, y, and state of the mouse
            window_y, window_x = self.window.getbegyx() # Get the top left x y of the window
            for id in self.buttons: # Loop through each button's ID in the window
                text, x, y, function = self.buttons[id] # Pull the data of the button

                # Check if the mouse is touching the button
                if (mouse_y == y + window_y) and (x + window_x <= mouse_x <= x + window_x + len(text)):
                    if b_state & curses.BUTTON1_PRESSED: # Check if the mouse is right clicking
                        self.window.addstr(y, x, text, curses.A_BOLD|curses.A_UNDERLINE) # Replace the text with a bolded version
                        self.window.refresh()
                        if function: # Check if the function for the button exists
                            function() # if so, run it
                        curses.napms(100) # wait 0.1 seconds for the animation
                        self.window.addstr(y, x, text, curses.A_UNDERLINE) # Reset the text
                        self.window.refresh()

    def add_toggle(self):
        '''Creates a dynamic toggle object'''
        if id in self.toggles:
            raise AlreadyExistsError(f'Toggle with ID, {id}, already exists!')