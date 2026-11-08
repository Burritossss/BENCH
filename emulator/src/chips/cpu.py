'''CPU chip definition'''
# Import pin library
from library.pin import * # Import pin objects to allow accessing pins
from library.datatypes import * # Import all datatypes to prevent illegal overflowing
# Import instruction set

class CPU:
    '''
    CPU class. Responsible for executing program instructions,
    managing internal data movement across registers and buses, 
    and driving the core fetch-decode-execute cycle.
    '''
    def __init__(self):
        # Pin definitions
        self.addressBus = PinBus(16)
        self.dataBus = PinBus(8)
        self.clockPin = Pin()
        self.rWPin = Pin()

        # Register's for keeping track of data.
        self.a = UInt8(0)   # General purpose register A
        self.x = UInt8(0)   # General purpose register X
        self.y = UInt8(0)   # General purpose register Y
        self.ir = UInt8(0)  # Instruction register
        self.pc = UInt16(0) # Program Counter Register

        # Internal "scratch" registers
        self.mar = UInt16(0) # Memory Address Register
        self.mdr = UInt8(0) # Memory Data Register