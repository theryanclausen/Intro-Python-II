from room import Room
from player import Player
from item import Item

belt = Item('championship', "Wrestling's top prize")
chair =Item('chair', "Steel folding chair. Derf's weapon of choice")

# Declare all the rooms 

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", "Dim light filters in from the south. Dusty passages run north and east."),

    'overlook': Room("Grand Overlook", "A steep cliff appears before you, falling into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm."),

    'narrow':   Room("Narrow Passage", "The narrow passage bends here from west to north. The smell of gold permeates the air."),

    'treasure': Room("Treasure Chamber", "You've found the long-lost treasure chamber! Sadly, it has already been completely emptied by earlier adventurers. The only exit is to the south."),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']



#
# Main
#

# Make a new player object that is currently in the 'outside' room.

derf = Player('Derf Flexman', 'a Professional wrestler turned crime fighting vigilante', room['outside'])

derf.add(belt)
room['foyer'].add(chair)
# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
print(f'\nYou are {derf.name}. {derf.inspect()} \n    {derf.location.enter()}\n')
while True:
    print('Enter "com" for list of commands.')
    inp = input("What now? ")
    if inp.__contains__(' '):
        verb_noun = inp.split(' ')
        if verb_noun[0] == 'drop':
            print(f'\n {derf.drop(verb_noun[1])}\n')
            
    if inp == 'q':
        break
    if inp == 'com':
        print('\nCommands: \n"n", "e", "s", "w" to move. \n"look" to search room.\n"m" for more commands \n"q" to quit.\n')
    if inp == 'm':
        print('\nMore Commands: \n"inv" to check inventory')
    if inp == 'look':
        print(f'\n{derf.location.check()}\n')
    if inp == 'inv':
        print(f'\n{derf.check_inventory()}\n')
    if inp == 'n' or inp == 'e' or inp == 's' or inp == 'w':
        next_room = derf.location.get_next_room(inp)
        if next_room == None:
            print("\nYou can't go that way\n")
        else:
            print(f'\n{derf.change_location(next_room)}\n')
