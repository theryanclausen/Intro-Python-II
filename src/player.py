# Write a class to hold player information, e.g. what room they are in
# currently.
from item import Item

class Player(Item):
    def __init__(self, name, description, startLocation, inventory =[] ):
        self.location = startLocation
        self.inventory = inventory
        super().__init__(name, description)
    def change_location(self, new_location):
        self.location = new_location
    def __repr__(self):
        return "Current Location: {}".format(self.location)
    def __str__(self):
        return "Current Location: {}".format(self.location)
    def add(self, item):
        self.inventory.append(item)
    def remove(self, item):
        self.inventory.remove(item)
    def unpack(self):
        i = ''
        for x in self.inventory:
            i += x.name
        return i
    def check_inventory(self):
        return f'{self.name} has {self.unpack()}'