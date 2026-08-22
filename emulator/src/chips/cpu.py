'''CPU chip definition'''
# Import pin library
from library.pin import *
from library.dataTypes import *

class CPU:
    '''CPU is the Central Processing Unit. It does all the data processing and running programs'''
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
    