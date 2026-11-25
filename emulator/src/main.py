'''
The BENCH emulator.

A high level, easy to modify and play with, moddable custom 8-bit emulator.
'''

# Import custom libraries
from chips.cpu import CPU # Import CPU class
from chips.memory import SRAM # Import SRAM class
from chips.systembus import SystemBus # Import System Bus class

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
        
        inp = input().lower()
        match inp: # Check what the user has input
            case "exit": # Check if exit has been typed
                break
            case "prog":
                print("Programming:\n")
                program.clear()
                new_program:list[int] = []
                while True:
                    text_code = input()
                    try:
                        code = int(text_code)
                        new_program.append(code)
                    except:
                        match text_code.lower():
                            case "exit":
                                program = new_program
                                memory.write_program(program, (0x00, 0x20))
                                cpu.reset()
                                break
                            case "list":
                                for progcode in new_program:
                                    print(progcode)
                                print()
                            case _:
                                print("Invalid code")
            case _:
                pass

if __name__ == "__main__":
    debug()