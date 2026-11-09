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
        self.a = UInt8(0)   # General purpose register A
        self.x = UInt8(0)   # General purpose register X
        self.y = UInt8(0)   # General purpose register Y
        self.ir = UInt8(0)  # Instruction register
        self.pc = UInt16(0) # Program Counter Register

        # Internal "scratch" registers
        self.mar = UInt16(0) # Memory Address Register
        self.mdr = UInt8(0) # Memory Data Register

    def fetch_decode_execute(self):
        '''Fetch-Decode-Execute loop of the CPU'''
        self.ir = self.bus.read_address(self.pc) # Read the byte at the address the PC is reading at
        self.pc += 1
        # Get the instruction's function from the instruction table
        instruction = INSTRUCTION_TABLE.get(self.ir)   
        # and check if the instruction actually exists
        if instruction:
            instruction(self) # Run the instruction and pass the CPU
        else:
            # Crash!!
            raise NotImplementedError(f"Instruction not implemented {self.ir:02X}")
        