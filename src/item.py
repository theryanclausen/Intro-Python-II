class Item:
    '''Base class'''
    def __init__(self, name, description):
        self.name = name
        self.description = description
    def inspect(self):
        print(f"{self.name} is {self.description}")