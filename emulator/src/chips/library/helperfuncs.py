'''A collection of functions for making it easier to write new instructions'''
from __future__ import annotations
from typing import TYPE_CHECKING # Import type checking to pull only types from CPU
from .datatypes import * # Import data types to force 8 bit and 16 bit limitations
if TYPE_CHECKING: # Check if type checking
    from chips.cpu import CPU
    

class Registers:
    '''Functions that manipulate registers'''
    @staticmethod
    def increment_pc(cpu:CPU) -> None:
        '''Increments the PC by one'''
        cpu.pc += 1

class Memory:
    '''Functions that manage memory'''
    @staticmethod
    def pull_address(cpu:CPU) -> UInt16:
        '''
        Returns an address from the next two values in memory
        
        Increments pc by two
        '''
        lower = cpu.bus.read_address(cpu.pc)
        Registers.increment_pc(cpu)
        upper = cpu.bus.read_address(cpu.pc)
        Registers.increment_pc(cpu)

        address = lower | (upper << 8)
        return UInt16(address)