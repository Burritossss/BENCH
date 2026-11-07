'''CPU chip definition'''
# Import pin library
from library.pin import *
from library.dataTypes import *
# Import instruction set

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

    # ================================ Micro Instructions ================================

    class MicroInstructions:
        def __init__(self, cpu:'CPU'):
            self.cpu = cpu

        def StoreAinMDR(self): # Stores the A register in the temporary internal data register
            self.cpu.mdr = self.cpu.a

        def LoadAfromMDR(self): # Loads the A register from the temporary internal data register
            self.cpu.a = self.cpu.mdr

        def StoreAinX(self): # Sets the A register to the X register
            self.cpu.a = self.cpu.x

        def StoreAinY(self): # Sets the A register to the Y register
            self.cpu.a = self.cpu.y

        def StoreXinMDR(self): # Stores the X register in the temporary internal data register
            self.cpu.mdr = self.cpu.x

        def LoadXfromMDR(self): # Loads the X register from the temporary internal data register
            self.cpu.x = self.cpu.mdr

        def StoreXinA(self): # Sets the X register to the A register
            self.cpu.x = self.cpu.a

        def StoreXinY(self): # Sets the X register to the Y register
            self.cpu.x = self.cpu.y

        def StoreYinMDR(self): # Stores the X register in the temporary internal data register
            self.cpu.mdr = self.cpu.x

        def LoadYfromMDR(self): # Loads the X register from the temporary internal data register
            self.cpu.x = self.cpu.mdr

        def StoreYinA(self): # Sets the X register to the A register
            self.cpu.x = self.cpu.a

        def StoreYinX(self): # Sets the X register to the Y register
            self.cpu.x = self.cpu.y