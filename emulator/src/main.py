'''
The BENCH emulator.

A high level, easy to modify and play with, moddable custom 8-bit emulator.
'''

import sys # Import system module
# Prevent curses import issues
try:
    import curses
    from curses import wrapper
except ModuleNotFoundError:
    print('Curses is not found!')
    print('Please ensure Curses is installed.')
    print('Possible fix:')
    if sys.version.startswith("win"): # Check if the OS is window
        print('\tRun: pip install windows-curses')
    else:
        print('\tEnsure curses supports your system and is installed in your python environment')
    input()
    sys.exit(1)
# Import custom libraries
from chips.cpu import CPU # Import CPU class
from chips.memory import SRAM # Import SRAM class
from chips.systembus import SystemBus # Import System Bus class
from emulator.ui import Window

def main(stdscr:curses.window):
    stdscr.clear() # Clear the terminal
    stdscr.scrollok(True) # Allow automatic scrolling
    stdscr.immedok(True) # Turn on immediate refresh
    curses.curs_set(0)
    
    # Pull the size of the window, store it for later window setup
    # and use it now to prevent small terminals from running it
    window_size = stdscr.getmaxyx()
    window_width = window_size[1]
    window_height = window_size[0]

    if window_width < 130 or window_height < 30:
        stdscr.addstr(f'Your terminal is too small!!\nPlease resize your terminal window.\nPress any key to exit.')
        stdscr.getch()
        return

    # Emulator initialization
    try:
        curses.mousemask(curses.ALL_MOUSE_EVENTS | curses.REPORT_MOUSE_POSITION)
        curses.mouseinterval(0)
        stdscr.addstr('Mouse Controls Activated\n')

        bus = SystemBus() # Initialize the BUS
        stdscr.addstr('Initialized Bus\n')
        
        memory = SRAM(0xFFFF) # Initialize the Memory
        stdscr.addstr('Initialized Memory\n')
        
        bus.map_device(0, 0xFFFF, memory) # Map the memory onto the bus
        stdscr.addstr('Memory has been mapped\n')
        
        cpu = CPU(bus) # Initialize the CPU
        stdscr.addstr('Initialized CPU')
    except Exception as e:
        stdscr.clear()
        stdscr.immedok(False)
        stdscr.addstr(1,1,f'There was an error loading. {e}')
        stdscr.addstr(6,1,"Press any key to continue")
        stdscr.refresh()
        stdscr.getch()
        sys.exit(1)
    stdscr.clear()
    stdscr.immedok(False) # Turn off immediate refresh
    stdscr.scrollok(False) # Stop automatic scrolling
    stdscr.nodelay(True) # Turn on no delay mode

    # Emulator variables
    emulation_running = False # Whether the emulation is running
    loaded_rom = '' # Name of the currently loaded rom

    # ======== Window setup ========
    # Emulator Statistics window
    emulator_stats_width = window_width // 6 # Width of the Emulator Statistics window
    emulator_stats_height = window_height // 2 - 1 # Height of the Emulator Statistics window
    emulator_stats = Window(1, 1, emulator_stats_width, emulator_stats_height, 'Statistics') # Create the window
    emulator_stats.add_dynamic(2, 3, 0, f'Running: {'Yes' if emulation_running else 'No'}')

    # Emulator Settings
    emulator_settings_width = window_width // 6
    emulator_settings_height = window_height // 2
    emulator_settings = Window(1, window_height - emulator_settings_height, emulator_settings_width, emulator_settings_height, 'Settings')

    # Main Window
    main_window_width = window_width - (window_width // 6) - 1
    main_window_height = window_height - 4
    main_window = Window((window_width // 6) + 1, 2, main_window_width, main_window_height, 'Main Window')

    # Top toolbar
    toolbar_window_width = window_width - (window_width // 6) - 1
    toolbar_window_height = 1
    toolbar_window = Window((window_width // 6) + 1, 1, toolbar_window_width, toolbar_window_height, '', False)

    toolbar_window.add_button(0, 0, 0, 'Exit', exit)

    while True:
        if emulation_running and loaded_rom:
            cpu.fetch_decode_execute()
        toolbar_window.tick_all_buttons()


def debug():
    # Initialize the system bus
    bus = SystemBus()

    # Initialize the virtual memory chip and make it a size of 65535
    memory = SRAM(0xFFFF)

    # Define a program and write the program to ROM space in memory
    program:list[int] = [
        0x01, 0x20
    ]
    memory.write_program(program, (0x00, 0x20)) # Write the program and set the start address to 0x2000

    bus.map_device(0, 0xFFFF, memory) # Map memory to the bus
    cpu = CPU(bus) # Create the CPU object
    # Loop
    while True:
        cpu.fetch_decode_execute() # Tick the cpu once
        print(f"A: 0x{cpu.a.value:02x}; X: 0x{cpu.x.value:02x}; Y: 0x{cpu.y.value:02x}; PC: 0x{cpu.pc.value:02x}")
        input() # Hold the program hostage until the user presses enter

if __name__ == "__main__":
    wrapper(main) # Run the main program