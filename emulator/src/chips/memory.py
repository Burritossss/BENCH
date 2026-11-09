from library.datatypes import * # Import all the custom datatypes

class SRAM:
    '''
    Memory chip of the system. This mimicks SRAM and is used
    for the total memory in the machine
    '''
    def __init__(self, size:int=0xFFFF) -> None:
        # Create the memory by storing the size 
        # and then creating a list of all the bytes for the chip
        self.size = size
        self.data = [UInt8(0) for _ in range(size)]

    def read(self, address:int|UInt16):
        '''Returns a specific byte from memory'''
        # Check to see if the address is either an int or
        # a UInt16. If UInt, pull the value of the UInt,
        # otherwise pull it normally
        value = address.value if isinstance(address, UInt16) else address
        # Return the byte at the address and using a bitwise
        # and to keep the requested address it within size
        return self.data[value & self.size]

    def write(self, address:int|UInt16, value:int|UInt8):
        '''Write to a specific byte of memory'''
        # Check to see if the address is either an int or
        # a UInt16. If UInt, pull the value of the UInt,
        # otherwise pull it normally
        address_value = address.value if isinstance(address, UInt16) else address
        # Do what we did with the address just instead of UInt16, its a 
        # UInt8
        value_value = value.value if isinstance(value, UInt8) else value # another great variable name......
        # Set the value of the address to the arguments value
        self.data[address_value & self.size].value = value_value 
    