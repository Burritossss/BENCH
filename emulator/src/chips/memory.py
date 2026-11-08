from library.datatypes import UInt8 # Import Unsigned 8 Integers

class SRAM:
    '''
    Memory chip of the system. This mimicks SRAM and is used
    for both RAM and ROM
    '''
    def __init__(self, size:int=0xFFFF) -> None:
        # Create the memory by storing the size 
        # and then creating a list of all the bytes for the chip
        self.data = [UInt8(0) for _ in range(size)]