'''File storing all the functions for each instruction for the CPU'''
from typing import TYPE_CHECKING # Import type checking to get types and functions

if TYPE_CHECKING: # Check if importing types to prevent looped importing errors
    from cpu import CPU # Import types for the CPU for access to its types

def ldai(cpu:CPU): # Load A immediate (Loads A register with the next value in memory)
    pass