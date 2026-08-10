class Pin:
    '''A pin is a simple, readable and writable bit'''
    def __init__(self):
        self.value = False

    def write(self, value:bool):
        self.value = value

    def read(self):
        return self.value

