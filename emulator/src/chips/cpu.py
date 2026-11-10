from library.datatypes import * # Import all datatypes to prevent illegal overflowing
from instructions import INSTRUCTION_TABLE # Import instruction set
from typing import TYPE_CHECKING

# Import system bus type checking
if TYPE_CHECKING:
    from systembus import SystemBus

class CPU:
    '''
    CPU class. Responsible for executing program instructions,
    managing internal data movement across registers and buses, 
    and driving the core fetch-decode-execute cycle.
    '''
    def __init__(self, bus:SystemBus):
        self.bus = bus # Keep track of the system bus object

        # Register's for keeping track of data.
        self.a: UInt8 = UInt8(0)   # General purpose register A
        self.x: UInt8 = UInt8(0)   # General purpose register X
        self.y: UInt8 = UInt8(0)   # General purpose register Y
        self.ir: UInt8 = UInt8(0)  # Instruction register
        self.pc: UInt16 = UInt16(0) # Program Counter Register

        # == Reset the program counter == 
        # Read the lower and upper address from the place in memory the PC start address should be
        lower = bus.read_address(0xFFFE)
        upper = bus.read_address(0xFFFF)
        address = lower | (upper << 8)

        # Set the PC to the start address
        self.pc = UInt16(address)

    def fetch_decode_execute(self):
        '''Fetch-Decode-Execute loop of the CPU'''
        self.ir = UInt8(self.bus.read_address(self.pc)) # Read the byte at the address the PC is reading at
        self.pc += 1
        # Get the instruction's function from the instruction table
        instruction = INSTRUCTION_TABLE.get(self.ir.value)
        # and check if the instruction actually exists
        if instruction:
            instruction(self) # Run the instruction and pass the CPU
        else:
            # Crash!!
            raise NotImplementedError(f"Instruction not implemented {self.ir.value:02X}")
        