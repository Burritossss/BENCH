'''More data types for making chips easier'''

class UInt8:
    '''An unsigned integer limited to numbers between 0 and 255'''
    def __init__(self, value:int):
        self._value = value & 0xFF

    @property
    def value(self):    
        return self._value
    
    @value.setter
    def value(self, value:int):
        self._value = value & 0xFF

class UInt16:
    '''An unsigned integer limited to numbers between 0 and 255'''
    def __init__(self, value:int):
        self._value = value & 0xFFFF

    @property
    def value(self):    
        return self._value
    
    @value.setter
    def value(self, value:int):
        self._value = value & 0xFFFF