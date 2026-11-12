from __future__ import annotations
from typing import Any # Import any type
from .library.datatypes import * # Import datatypes

class SystemBus:
    '''Routes read/write requests to hardware devices based on address'''
    def __init__(self):
        # Create the list of for the System Bus
        self.regions: list[tuple[int, int, Any]] = []

    def map_device(self, start:int|UInt16, end:int|UInt16, device:Any):
        '''Maps a device onto the System Bus'''
        # Check if start and end is using UInt16.
        # If so, use the UInt16's value,
        # otherwise use the integer
        start_value = start.value if isinstance(start, UInt16) else start
        end_value = end.value if isinstance(end, UInt16) else end

        # Append the format for the system bus regions
        self.regions.append((start_value, end_value, device))

    def read_address(self, address:int|UInt16) -> int:
        '''
        Reads an address linked in the system bus.

        If an address isn't linked, a warning will be printed and will return 0
        '''
        # Check if the address is a UInt or normal int.
        # If it is a UInt, pull the value of the UInt, otherwise pull the integer
        address_value = address.value if isinstance(address, UInt16) else address
        # Loop through each device linked in the system bus
        for start, end, device in self.regions:
            if start <= address_value <= end: # Check if the requested address is in range
                return device.read(address_value - start) # Return the devices read function
        # If there's nothing at the address, print a warning and return 0
        print(f"Bus Warning: Unmapped read at 0x{address_value:04X}")
        return 0

    def write_address(self, address:int|UInt16, value:int|UInt8) -> None:
        '''Write's to an address linked to the system bus '''
        # Check if arguments is a UInt or int.
        # If it is a UInt, pull the value of the UInt, otherwise pull integer
        address_value = address.value if isinstance(address, UInt16) else address
        value_value = value.value if isinstance(value, UInt8) else value # greatest variable name... value_value

        # Loop through each device linked in the system bus
        for start, end, device in self.regions:
            if start <= address_value <= end: # Check if the requested address is in range
                device.write(address_value - start, value_value) # Write to the device at the address requested
                return
        # If there's nothing at the address, print a warning
        print(f"Bus Warning: Unmapped write at 0x{address_value:04X}")
        return