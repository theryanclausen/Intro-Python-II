# Implement a class to hold room information. This should have name and
# description attributes.
from item import Item 



class Room(Item):
    def __init__(self, name, description):
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.list = []
        super().__init__(name, description)
    def enter(self):
        print(f'You enter the {self.name}. {self.description}') 
    def unpack(self):
        return ', '.join(self.list)
    def check(self):
        print(f'Searching the {self.name}, you find {self.unpack()}')
    def add(self, item):
        self.list.append(item)
    def remove(self, item):
        self.list.remove(item)


