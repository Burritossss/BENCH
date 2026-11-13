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
    pass

def debugmode():
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
    debugmode() # Run the main program