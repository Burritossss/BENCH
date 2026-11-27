'''File storing all the functions for each instruction for the CPU'''
from __future__ import annotations
from typing import TYPE_CHECKING # Import type checking to get types and functions
from types import FunctionType # Import function type for better type checking
from .library.helperfuncs import * # Import helperfuncs for easier writing of instructions
from .library.datatypes import * # Import dataclasses

if TYPE_CHECKING: # Check if importing types to prevent looped importing errors
    from cpu import CPU # Import types for the CPU for access to its types

def nop(cpu:CPU): # No Operation. Just passes
    pass

def ldai(cpu:CPU): # Load A immediate (Loads A register with the next value in memory)
    cpu.a = UInt8(cpu.fetch_from_bus(cpu.pc)) # Sets the A register immediately
    Registers.increment_pc(cpu) # Increments the PC

def ldaa(cpu:CPU): # Load A absolute (Loads A register with a value in an address defined by two bytes in memory)
    address = Memory.pull_address(cpu)
    cpu.a = UInt8(cpu.fetch_from_bus(address))

def staa(cpu:CPU): # Store A absolute (Stores A register at an address defined by two bytes in memory)
    address = Memory.pull_address(cpu)
    cpu.write_to_bus(address, cpu.a) # Write the A register to the address

def ldxi(cpu:CPU): # Load X immediate (Loads X register with the next value in memory)
    cpu.x = UInt8(cpu.fetch_from_bus(cpu.pc)) # Sets the X register immediately
    Registers.increment_pc(cpu) # Increment the PC

def ldxa(cpu:CPU): # Load X absolute (Loads the X register with a value in an address defined by two bytes in memory)
    address = Memory.pull_address(cpu)
    cpu.x = UInt8(cpu.fetch_from_bus(address))

def stxa(cpu:CPU): # Store X absolute (Stores X register at an address defined by two bytes in memory)
    address = Memory.pull_address(cpu)
    cpu.write_to_bus(address, cpu.a)

def ldyi(cpu:CPU): # Load Y immediate (Loads Y register with the next value in memory)
    cpu.y = UInt8(cpu.fetch_from_bus(cpu.pc)) # Sets the Y register immediately
    Registers.increment_pc(cpu) # Increment the PC

def ldya(cpu:CPU): # Load Y absolute (Loads the Y register with a value in an address defined by two bytes in memory)
    address = Memory.pull_address(cpu)
    cpu.y = UInt8(cpu.fetch_from_bus(address))

def stya(cpu:CPU): # Store Y absolute (Stores Y register at an address defined by two bytes in memory)
    address = Memory.pull_address(cpu)
    cpu.write_to_bus(address, cpu.y)


'''
A dictionary of each instructions function and it's operand

The format is <opcode>:<function without parenthesis>
'''
INSTRUCTION_TABLE:dict[int,FunctionType] = {
    0x00:nop, 
    0x01:ldai, 0x02:ldaa, 0x03:staa, 
    0x11:ldxi, 0x12:ldxa, 0x03:stxa,
}