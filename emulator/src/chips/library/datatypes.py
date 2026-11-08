'''More data types for making chips easier'''
from __future__ import annotations

class UInt8:
    '''An unsigned integer limited to numbers between 0 and 255'''
    def __init__(self, value:int):
        self._value = value & 0xFF

    @property
    def value(self) -> int:    
        return self._value
    
    @value.setter
    def value(self, value:int) -> None:
        self._value = value & 0xFF

    def __add__(self, other:int|UInt8) -> UInt8:
        # Grab the value of other depending on what type it is
        value = other.value if isinstance(other, UInt8) else other
        return UInt8(self._value + value)

    def __radd__(self, other:int|UInt8) -> UInt8:
        return self.__add__(other) # Return the addition

    def __iadd__(self, other:int|UInt8) -> UInt8:
        # Grab the value of other depending on what type it is
        value = other.value if isinstance(other, UInt8) else other
        self._value = (self.value + value) & 0xFF # Add the value of other to the value and keep it within 0xFF
        return self

class UInt16:
    '''An unsigned integer limited to numbers between 0 and 65535'''
    def __init__(self, value:int):
        self._value = value & 0xFFFF

    @property
    def value(self) -> int:    
        return self._value
    
    @value.setter
    def value(self, value:int) -> None:
        self._value = value & 0xFFFF

    def __add__(self, other:int|UInt8|UInt16) -> UInt16:
        # Grab the value of other depending on what type it is
        value = other.value if isinstance(other, UInt16|UInt8) else other
        return UInt16(self._value + value)

    def __radd__(self, other:int|UInt8|UInt16) -> UInt16:
        return self.__add__(other) # Return the addition

    def __iadd__(self, other:int|UInt8|UInt16) -> UInt16:
        # Grab the value of other depending on what type it is
        value = other.value if isinstance(other, UInt16|UInt8) else other
        self._value = (self.value + value) & 0xFFFF # Add the value of other to the value and keep it within 0xFFFF
        return self