class Pin:
    '''A pin is a simple, readable and writable bit'''
    def __init__(self):
        self.value = False

    def write(self, value:bool|int):
        self.value = (value & 1)

    def read(self) -> bool|int:
        return (self.value & 1)

class PinBus:
    '''Variably length group of pins that can be read from and wrote to'''
    def __init__(self, length:int=8):
        if length < 1:
            raise ValueError('Length less that 0 not permitted!')
        self.pins = [Pin() for _ in range(length)]

    def write(self, value:int):
        for i, pin in enumerate(self.pins):
            pin.write((value >> i) & 1)

    def read(self) -> int:
        '''Reads, then returns the full data from the Bus'''
        value = 0
        for i, pin in enumerate(self.pins):
            value |= pin.read() << i
        return value