'''
The BENCH emulator.

A high level, easy to modify and play with, moddable custom 8-bit emulator.
'''

from chips.cpu import CPU # Import CPU class
from chips.memory import SRAM # Import SRAM class
from chips.systembus import SystemBus # Import System Bus class

def main():
    # Initialize the system bus
    bus = SystemBus()

    # Initialize the virtual memory chip and make it a size of 65535
    memory = SRAM(0xFFFF)

    # Define a program and write the program to ROM space in memory
    program:list[int] = []
    memory.write_program(program, (0x00, 0x20)) # Write the program and set the start address to 0x2000

    bus.map_device(0, 0xFFFF, memory) # Map memory to the bus
    cpu = CPU(bus) # Create the CPU object
    # Loop
    while True:
        cpu.fetch_decode_execute() # Tick the cpu once
        print(f"A: {cpu.a}; X: {cpu.x}; Y: {cpu.y}")
        input() # Hold the program hostage until the user presses enter

if __name__ == "__main__":
    main() # Run the main program