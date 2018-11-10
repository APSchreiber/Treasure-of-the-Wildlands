# Treasure of MDC
# ToMDC.py

# Author: Andrew Schreiber
# Created: 11/09/18
# Modified: 11/09/18

'''
Treasure of MDC Game
'''

print "Loading..."
import os, sys, traceback, datetime, random
from subprocess import call 
from time import sleep 

#####################################################################

game_script = {
    "welcome": "Welcome to the Treasure of MDC!"
    }

actions = ["Pick it up", "Eat it", "Leave it be"]

results = ["grow forty feet tall!", "sleep for a week", "lose your sensibilities"]

rooms = [
    {
        "name": "Rockwoods Reservation",
        "description": "a magical forest wonderland",
        "items": ["magic flute", "deadly fern", "rabbit foot"]
    },
    {
        "name": "Amidon",
        "description": "a deep and dark jungle",
        "items": ["mushroom", "spear", "jungle potion"]
    },
    {
        "name": "Powder Valley",
        "description": "an enchanted snow kingdom, nestled below the gigantic mountains",
        "items": ["hawk's beak", "snow shoe", "ice medallion"]
    },
    {
        "name": "Howell Island",
        "description": "a remote island off the banks of the King Charles River",
        "items": ["hornpipe", "rusty bucket", "fish head"]
    }
]

#####################################################################

# navigate
def navigate(rooms, player):

    print "\nWelcome, " + player + ". Let us explore this glorious land!" 
   
    # get room names
    names = []
    for rm in rooms:
        names.append(rm["name"])

    # give user options
    print "\n" + "Here is a map of the territory: "
    for n in names:
        ind = names.index(n) + 1
        print "\t" + str(ind) + ".) " + n
    print
    go_to_room = raw_input("Where would you like to go? ")

    # going to that room
    selected_room = names[int(go_to_room) - 1]
    print "\nWell, OK then " + player + ", let's go to " + selected_room + "!"
    sleep(3)

    # populate room
    room = rooms[int(go_to_room) - 1]
    description = room["description"]
    print "You find yourself in " + description + "."
    sleep(3)

    # get a random number
    max_items = len(room["items"])
    rand_item = room["items"][random.randint(1, max_items) - 1]
    print "\nOn the ground before you, you see " + rand_item + "."

    print
    for a in actions:
        ind = actions.index(a) + 1
        print "\t" + str(ind) + ".) " + a
    next_choice = actions[int(raw_input("\nWhat would you like to do? ")) - 1]

    max_results = len(results)
    rand_result = results[random.randint(1, max_results) - 1]
    print "\n" + "It looks like the " + rand_item + " caught your eye. Your choice to " + next_choice.lower() + " caused you to " + rand_result +"!"
    



#####################################################################

#####################################################################

try:

    # welcome routine
    sleep(2)
    print game_script['welcome'] + "\n"

    player = raw_input("What is your name? ")

    navigate(rooms, player)
        
    print "\n\nThe End!"
    
except:

    tb = sys.exc_info()[2]
    tbinfo = traceback.format_tb(tb)[0]

    print "\nError: " + tbinfo
    
