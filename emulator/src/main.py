'''
The BENCH emulator.

A high level, easy to modify and play with, moddable custom 8-bit emulator.
'''

from chips.cpu import CPU # Import CPU class
from chips.memory import SRAM # Import SRAM class
from chips.systembus import SystemBus # Import System Bus class
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
    sys.exit(1)

def main(stdscr:curses.window):
    stdscr.clear()
    # Emulator initialization
    try:
        bus = SystemBus() # Initialize the BUS
        memory = SRAM(0xFFFF) # Initialize the Memory
        bus.map_device(0, 0xFFFF, memory) # Map the memory onto the bus
        cpu = CPU(bus) # Initialize the CPU
    except Exception as e:
        stdscr.addstr(1,1,f'There was an error loading. {e}')
        stdscr.addstr(6,1,"Press any key to continue")
        stdscr.refresh()
        stdscr.getch()
        sys.exit(1)
    
    # ======== Window setup ========
    window_size = stdscr.getmaxyx()
    window_width = window_size[1]
    window_height = window_size[0]
    # Emulator Statistics window
    emulator_stats_width = window_width // 6 # Width of the Emulator Statistics window
    emulator_stats_height = window_height // 2 - 1 # Height of the Emulator Statistics window
    emulator_stats = curses.newwin(emulator_stats_height, emulator_stats_width, 1, 1) # Create the window

    emulator_stats.addstr(1, ((emulator_stats.getmaxyx()[1] - len('Status')) // 2), 'Status') # Add the title to the window
    
    emulator_stats.border() # Create the border
    emulator_stats.refresh() # Refresh the window
    emulator_stats.getch()

    # Emulator Settings
    emulator_settings_width = window_width // 6
    emulator_settings_height = window_height // 2
    emulator_settings = curses.newwin(emulator_settings_height, emulator_settings_width, window_height - emulator_settings_height, 1)

    emulator_settings.addstr(1, ((emulator_settings.getmaxyx()[1] - len('Settings')) // 2), 'Settings')
    emulator_settings.border()
    emulator_settings.refresh()
    emulator_settings.getch()

    # Main Window
    main_window_width = window_width - (window_width // 6) - 1
    main_window_height = window_height - 4
    main_window = curses.newwin(main_window_height, main_window_width, 2, (window_width // 6) + 1)

    main_window.addstr(1, ((main_window.getmaxyx()[1] - len('Main Window')) // 2), 'Main Window')
    main_window.border()
    main_window.refresh()
    main_window.getch()



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