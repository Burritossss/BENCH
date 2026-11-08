from __future__ import annotations
from typing import Any # Import any type

class SystemBus:
    '''Routes read/write requests to hardware devices based on address'''
    def __init__(self):
        # Create the list of for the System Bus
        self.regions: list[tuple[int, int, Any]] = []

    def map_device(self, start:int, end:int, device:Any):
        '''Maps a device onto the System Bus'''
        self.regions.append((start, end, device))

    def read_address(self, address:int) -> int:
        '''
        Reads an address linked in the system bus.

        If an address isn't linked, a warning will be printed and will return 0
        '''
        # Loop through each device linked in the system bus
        for start, end, device in self.regions:
            if start <= address <= end: # Check if the requested address is in range
                return device.read(address - start) # Return the devices read function
        # If there's nothing at the address, print a warning and return 0
        print(f"Bus Warning: Unmapped read at 0x{address:04X}")
        return 0

    def write_address(self, address:int, value:int) -> None:
        '''Write's to an address linked to the system bus '''
        # Loop through each device linked in the system bus
        for start, end, device in self.regions:
            if start <= address <= end: # Check if the requested address is in range
                device.write(address - start, value) # Write to the device at the address requested
                return
        # If there's nothing at the address, print a warning
        print(f"Bus Warning: Unmapped write at 0x{address:04X}")
        return