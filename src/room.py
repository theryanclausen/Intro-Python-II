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
        return f'You enter the {self.name}. {self.description}'
    def unpack(self):
        i = ''
        for x in self.list:
            i += x.name
        if i == '':
            i = 'nothing'
        return i
    def check(self):
        return f'Searching the {self.name}, you find {self.unpack()}'
    def add(self, item):
        self.list.append(item)
    def remove(self, item):
        self.list.remove(item)
    def get_next_room(self, direction):
        if direction == 'n':
            return self.n_to
        elif direction == 'e':
            return self.e_to
        elif direction == 'w':
            return self.w_to
        elif direction == 's':
            return self.s_to
        else:
            return None


