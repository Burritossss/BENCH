'''File storing all the functions for each instruction for the CPU'''
from typing import TYPE_CHECKING # Import type checking to get types and functions
from types import FunctionType # Import function type for better type checking
from library.helperfuncs import * # Import helperfuncs for easier writing of instructions
from library.datatypes import * # Import dataclasses

if TYPE_CHECKING: # Check if importing types to prevent looped importing errors
    from cpu import CPU # Import types for the CPU for access to its types

def nop(cpu:CPU): # No Operation. Just passes
    Registers.increment_pc(cpu) # Increment the PC

def ldai(cpu:CPU): # Load A immediate (Loads A register with the next value in memory)
    cpu.a = UInt8(cpu.bus.read_address(cpu.pc)) # Sets the A register immediately
    Registers.increment_pc(cpu) # Increments the PC

def ldaa(cpu:CPU): # Load A absolute (Loads A register with a value in an address defined by two bytes in memory)
    address = Memory.pull_address(cpu)
    cpu.a = UInt8(cpu.bus.read_address(address))

'''
A dictionary of each instructions function and it's operand

The format is <opcode>:<function without parenthesis>
'''
INSTRUCTION_TABLE:dict[int,FunctionType] = {
    0x00:nop, 
    0x01:ldai, 0x02:ldaa,    
}