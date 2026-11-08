'''A collection of functions for making it easier to write new instructions'''
from typing import TYPE_CHECKING # Import type checking to pull only types from CPU
from datatypes import * # Import data types to force 8 bit and 16 bit limitations
if TYPE_CHECKING: # Check if type checking
    from cpu import CPU

class Registers:
    '''Functions that manipulate registers'''
    @staticmethod
    def increment_pc(cpu:CPU) -> None:
        '''Increments the PC by one'''
        cpu.pc += 1