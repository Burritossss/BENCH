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

# === A register instructions ===

def lda_i(cpu:CPU): # Load A immediate (Loads A register with the next value in memory)
    cpu.a = UInt8(cpu.fetch_from_bus(cpu.pc)) # Sets the A register immediately
    Registers.increment_pc(cpu) # Increments the PC

def lda_a(cpu:CPU): # Load A absolute (Loads A register with a value in an address defined by two bytes in memory)
    address = Memory.pull_address(cpu)
    cpu.a = UInt8(cpu.fetch_from_bus(address))

def sta_a(cpu:CPU): # Store A absolute (Stores A register at an address defined by two bytes in memory)
    address = Memory.pull_address(cpu)
    cpu.write_to_bus(address, cpu.a) # Write the A register to the address

# === X register instructions ===

def ldx_i(cpu:CPU): # Load X immediate (Loads X register with the next value in memory)
    cpu.x = UInt8(cpu.fetch_from_bus(cpu.pc)) # Sets the X register immediately
    Registers.increment_pc(cpu) # Increment the PC

def ldx_a(cpu:CPU): # Load X absolute (Loads the X register with a value in an address defined by two bytes in memory)
    address = Memory.pull_address(cpu)
    cpu.x = UInt8(cpu.fetch_from_bus(address))

def stx_a(cpu:CPU): # Store X absolute (Stores X register at an address defined by two bytes in memory)
    address = Memory.pull_address(cpu)
    cpu.write_to_bus(address, cpu.a)

def inx(cpu:CPU): # Increment X (Increments the X register by one)
    cpu.x += 1
    Registers.increment_pc(cpu)

def dex(cpu:CPU): # Decrement X (Decrements the X register by one)
    cpu.x -= 1
    Registers.increment_pc(cpu)

# === Y register instructions ===

def ldy_i(cpu:CPU): # Load Y immediate (Loads Y register with the next value in memory)
    cpu.y = UInt8(cpu.fetch_from_bus(cpu.pc)) # Sets the Y register immediately
    Registers.increment_pc(cpu) # Increment the PC

def ldy_a(cpu:CPU): # Load Y absolute (Loads the Y register with a value in an address defined by two bytes in memory)
    address = Memory.pull_address(cpu)
    cpu.y = UInt8(cpu.fetch_from_bus(address))

def sty_a(cpu:CPU): # Store Y absolute (Stores Y register at an address defined by two bytes in memory)
    address = Memory.pull_address(cpu)
    cpu.write_to_bus(address, cpu.y)

def iny(cpu:CPU): # Increment Y (Increments the Y register by one)
    cpu.y += 1
    Registers.increment_pc(cpu)

def dey(cpu:CPU): # Decrement Y (Decrements the Y register by one)
    cpu.y -= 1
    Registers.increment_pc(cpu)

'''
A dictionary of each instructions function and it's operand

The format is <opcode>:<function without parenthesis>
'''
INSTRUCTION_TABLE:dict[int,FunctionType] = {
    0x00:nop,
    0x01:lda_i, 0x02:lda_a, 0x03:sta_a,                     # A register manipulation instructions
    0x11:ldx_i, 0x12:ldx_a, 0x13:stx_a, 0x14:inx, 0x15:dex, # X register manipulation instructions
    0x21:ldy_i, 0x22:ldy_a, 0x23:sty_a, 0x24:iny, 0x25:dey, # Y register manipulation instructions
}