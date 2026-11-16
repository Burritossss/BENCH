'''Abstraction layer for making windows in BENCH easier'''
import curses

class Window:
    '''A window object. It can have a title, position, size, etc.'''
    def __init__(self, 
                 x:int, 
                 y:int, 
                 width:int, 
                 height:int,
                 name:str="Window"):
        self.name = name
        self.window = curses.newwin(height, width, y, x)
        self.window.border()
        self.window.addstr(1, ((self.window.getmaxyx()[1] - len(self.name)) // 2), self.name)

    def refresh(self):
        self.window.refresh()
