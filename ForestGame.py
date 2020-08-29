# Author: Adam Grimshaw
# Date: December 24, 2019
# Description: A campy text game just for the heck of it. Enjoy!
# Variables_______________________________________________________

# Tiles
# Tile name, North, East, South, West, Tile Description, Item name, Item description, Can item be used here?, Description of item being used.

A0 = ['A0', False, False, False, False]

A1 = ['A1', False, False, False, False]

A2 = ['A2', False, True, True, False, 'You stand on the bank of a river. The moonlight reflects off the silent ripples. The forest extends to the SOUTH and EAST.', None, None, None, True]

A3 = ['A3', False, True, True, True, 'You stand at the edge of the forest. The distinct howl of wolves makes you think that proceeding any further NORTH would be a mistake. The forest extends SOUTH, EAST, and WEST.', None, None, None, True]

A4 = ['A4', False, True, True, True, 'You stand at the edge of the forest. You hear wolves howling to the NORTH. The forest extends SOUTH, EAST, and WEST.', None, None, None, True]

A5 = ['A5', False, False, False, True, 'You stand at the base of cliff. There appears to be no way up. A clearing lies NORTH, but looks dangerous. You can only proceed WEST.', None, None, None, True]

A6 = ['A6', False, False, False, False]

A7 = ['A7', False, False, False, False]

A8 = ['A8', False, False, False, False]

A9 = ['A9', False, True, True, False, 'The cave leads EAST and SOUTH.', None, None, True, None]

A10 = ['A10', False, False, False, True, 'You come to a dead end. On the ground lay a human skull with a large fracture.', 'KEY', 'You find a KEY amongst the rocks on the ground.', True, None]

A11 = ['A11', False, False, False, False]

A12 = ['A12', False, False, False, False]

A13 = ['A13', False, False, True, False, 'You come to a dead end.', 'CHAINSAW', 'You find a CHAINSAW laying on the floor. It is full of gas,', True, None]

B0 = ['B0', False, False, False, False]

B1 = ['B1', False, False, False, False]

B2 = ['B2', True, True, True, False, 'You stand on the bank of a river. The woods extend to the NORTH, EAST, and SOUTH.', None, None, None, True]

B3 = ['B3', True, True, True, True, 'You stand in the woods. The forest extends to the NORTH, SOUTH, EAST, and WEST.', None, None, None, True]

B4 = ['B4', True, False, True, True, 'A pile of junk lies at the base of a stone cliff. The forest extends to the NORTH, SOUTH, and WEST.', 'TIRE', 'You sort through the junk and find a TIRE.', None, True]

B5 = ['B5', False, False, False, False]

B6 = ['B6', False, False, False, False]

B7 = ['B7', False, False, False, False]

B8 = ['B8', False, True, True, False, 'The cave continues SOUTH and EAST.', None, None, True, None]

B9 = ['B9', True, True, False, True, 'The cave extends NORTH, EAST, and WEST.', None, None, True, None]

B10 = ['B10', False, True, False, True, 'The cave extends EAST, and WEST.', None, None, True, None]

B11 = ['B11', False, False, True, True, 'The cave continues SOUTH and WEST.', None, None, True, None]

B12 = ['B12', False, True, True, False, 'You stand in the room behind the door. It smells like death. Bones litter the floor. You hope they are not human. You decide to not look too closely. The room extends EAST.', None, None, True, None]

B13 = ['B13', True, False, False, True, 'You walk carefully. The room extends to the NORTH and WEST.', None, None, True, None]

C0 = ['C0', False, False, False, False]

C1 = ['C1', False, False, False, False]

C2 = ['C2', False, False, False, False, 'You fall into a pit. You struggle to climb out, but fail to get a hold of anything solid. The soil crumbles in your hand. You are stuck down here.', None, None, None, True]

C3 = ['C3', True, True, True, True, 'You stand in the woods. The forest extends to the NORTH, SOUTH, EAST, and WEST.', None, None, None, True]

C4 = ['C4', True, True, True, True, 'You stand in the woods. The forest extends to the NORTH, SOUTH, EAST, and WEST.', None, None, None, True]

C5 = ['C5', False, True, False, True, 'Tall walls of stone rise up on your NORTH and SOUTH. To your EAST lies the opening of a large cave. The forest lies WEST.', None, None, None, True]

C6 = ['C6', False, True, False, True, 'You stand in the entrance to the cave. The forest lies WEST. The cave continues to the EAST.', None, None, True, None]

C7 = ['C7', False, True, False, True, 'A large pile of volcanic rock litters the floor. You have to choose yoru steps carefully. You can proceed EAST or WEST.', None, None, True, None]

C8 = ['C8', True, False, False, True, 'You come to a curve. You can go NORTH or WEST.', None, None, True, None]

C9 = ['C9', False, True, False, False, 'The cave comes to a dead end.', None, None, True, None]

C10 = ['C10', False, False, True, True, 'The cave extends WEST and SOUTH.', None, None, True, None]

C11 = ['C11', True, False, True, False, 'You have to crawl through a low tunnel. The cave continues to the NORTH and SOUTH.', None, None, True, None]

C12 = ['C12', False, True, True, False, 'You enter a chamber with a large door at the NORTH, built of heavy timbers. It is locked. The cave continues EAST and SOUTH. ', None, None, True, None]

C13 = ['C13', False, False, True, True, 'The cave continues SOUTH and WEST.', None, None, True, None]

D0 = ['D0', False, False, False, False]

D1 = ['D1', False, True, True, False, 'You stand on a river bank. The forest extends to the EAST and SOUTH.', None, None, None, True]

D2 = ['D2', False, False, True, True, 'You come to an abandoned shack, fenced in on the NORTH and EAST sides.', 'SURGICAL TUBING', 'You rummage the sordid debris in the shack. You find a length of SURGICAL TUBING.', True, None]

D3 = ['D3', True, True, True, False, 'You stand in the woods. The forest extends to the NORTH, SOUTH, and EAST. An old, weathered fence obstructs your path to the WEST.', None, None, None, True]

D4 = ['D4', True, False, True, True, 'You stand at the base of a stone cliff. There is no way up. The forest extends to the NORTH, SOUTH, and WEST.', None, None, None, True]

D5 = ['D5', False, True, False, False, 'You come to the edge of the cliff and look out across the forest. It seems peaceful from this vantage point. You can only go back the way you came.', None, None, True, None]

D6 = ['D6', False, False, True, True, 'The grass shelf extends to the WEST and SOUTH. Stone cliffs close you in on all other sides.', 'OWL', 'A majestic OWL is perched on the limb a large, dead branch. He looks at you, his eyes piercing your soul.', True, None]

D7 = ['D7', False, True, False, False, 'You come to a dead end.', 'CHARCOAL', 'Bits of CHARCOAL litter the ground.', True, None]

D8 = ['D8', False, False, True, True, 'The cave extends to the WEST and SOUTH.', None, None, True, None]

D9 = ['D9', False, True, True, False, 'A large booming noise echos through the cave. You are not eager to spend more time in here than necessary.The cave continues to the EAST and SOUTH.', None, None, True, None]

D10 = ['D10', True, False, False, True, 'The cave continues to the NORTH and WEST.', None, None, True, None]

D11 = ['D11', True, True, False, False, 'There is a carving on the wall. You cannot make out the words. The cave extends to the NORTH and EAST.', None, None, True, None]

D12 = ['D12', True, False, True, True, 'The cave continues to the NORTH, SOUTH, and WEST.', None, None, True, None]

D13 = ['D13', True, False, False, False, 'You reach a dead end.', None, None, True, None]

E0 = ['E0', False, False, False, False]

E1 = ['E1', True, True, True, False, 'The stand at the edge of a river. The forest extends to the NORTH, EAST, and SOUTH.', None, None, None, True]

E2 = ['E2', True, True, True, True, 'The moon shines through the trees casting sinister shadows on the forest floor. The forest extends in all directions.', None, None, None, True]

E3 = ['E3', True, True, True, True, 'You stand in the woods. The forest extends to the NORTH, SOUTH, EAST, and WEST.', None, None, None, True]

E4 = ['E4', True, True, True, True, 'You hear an OWL. You see a stone formation to the EAST.', None, None, None, True]

E5 = ['E5', False, False, True, True, 'You stand at the base of a cliff. Looking up to the EAST, you see a large metal hook screwed into the rock above you. The forest extends to the SOUTH and WEST.', None, None, None, True]

E6 = ['E6', True, True, True, True, 'You stand on a grassy shelf of cliff. The forest lies below you to the WEST. The grassy shelf extends to the NORTH, EAST, and SOUTH.', None, None, True, None]

E7 = ['E7', False, False, True, True, 'You look up at a stone wall. There is no way up. The grassy shelf extends SOUTH and WEST.', None, None, True, None]

E8 = ['E8', True, True, False, False, 'You enter a chamber that smells of charcoal.', 'HATCHET', 'On the ground you find a HATCHET.', True, None]

E9 = ['E9', True, False, True, True, 'The cave forks NORTH, WEST, and SOUTH.', None, None, True, None]

E10 = ['E10', False, True, True, False, 'The cave extends SOUTH and EAST.', None, None, True, None]

E11 = ['E11', False, False, False, True, 'You come to a dead end. You can either go back, or sit here and wait around to die.', None, None, True, None]

E12 = ['E12', True, False, True, False, 'The cave continues to the NORTH and SOUTH.', None, None, True, None]

E13 = ['E13', False, False, False, False]

F0 = ['F0', False, True, True, False, 'A river blocks your path to the NORTH. A large tree bends over it, its branches nearly touching the water. The forest extends SOUTH and EAST.', 'ROPE', 'You peer into a large hollow of the tree and find a ROPE.', None, True]

F1 = ['F1', True, True, True, True, 'You see a river to the NORTH.', None, None, None, True]

F2 = ['F2', True, True, True, True, 'You stand in the woods. The forest extends to the NORTH, SOUTH, EAST, and WEST.', None, None, None, True]

F3 = ['F3', True, True, True, True, 'The trees creak and sway in the wind. The forest extends in all directions.', None, None, None, True]

F4 = ['F4', True, True, True, True, 'You stand in the woods. The forest extends to the NORTH, SOUTH, EAST, and WEST.', None, None, None, True]

F5 = ['F5', True, False, True, True, 'You stand at the base of a cliff. There is no way up. The forest extends to the NORTH, SOUTH, and WEST.', None, None, None, True]

F6 = ['F6', True, True, False, False, 'A steep cliff lay to the WEST and SOUTH. You stand at the edge and look down at the forest. The moon reflects off the lake in the distance.', None, None, None, True]

F7 = ['F7', True, True, True, True, 'You stand on a grassy shelf on the side of a cliff. The shelf extends in all directions.', None, None, True, None]

F8 = ['F8', False, False, False, True, 'You grassy ledge comes to a halt stone walls surround you in every direction. There is no way to climb up. You can only go back.', 'CHAIN', 'Coiled up at the foot of a boulder is a large CHAIN with sturdy hooks at both ends.', True, None]

F9 = ['F9', True, False, True, False, 'You hear a shriek in the distance, but it could just be your imagination. The cave extends to the NORTH and SOUTH.', None, None, True, None]

F10 = ['F10', True, True, False, False, 'The cave extends to the NORTH and EAST.', None, None, True, None]

F11 = ['F11', False, False, True, True, 'You enter a chamber with a large mineral deposit. The cave continues to the EAST and SOUTH.', None, None, True, None]

F12 = ['F12', True, False, True, False, 'A feel a drop of water on your face. A shallow puddle has formed on the floor. You walk more carefully. The cave extends to the NORTH and SOUTH.', None, None, True, None]

F13 = ['F13', False, False, False, False]

G0 = ['G0', True, True, False, False, 'The woods to the WEST have grown into a vast thicket, making walking that way impossible. A large lake lies to the SOUTH.', None, None, None, True]

G1 = ['G1', True, True, False, True, 'You stand on the edge of a lake. The forest extends to the NORTH, EAST, and WEST.', None, None, None, True]

G2 = ['G2', True, True, True, True, 'You stand in the woods. You see a lake nearby. The forest extends to the NORTH, SOUTH, EAST, and WEST.', None, None, None, True]

G3 = ['G3', True, True, True, True, 'You come across a dead animal. A deer perhaps? Its mangled corpse stains the ground with blood. The forest extends to the NORTH, SOUTH, EAST, and WEST.', None, None, None, True]

G4 = ['G4', True, True, True, True, 'The forest extends in all directions. To the SOUTH you see the glow of a campfire.', None, None, None, True]

G5 = ['G5', True, True, True, True, 'You stand in the woods. The forest extends to the NORTH, SOUTH, EAST, and WEST.', None, None, None, True]

G6 = ['G6', False, False, True, True, 'You find yourself at the base of a cliff. There seems to be no way up. The forest extends to the WEST, and SOUTH.', None, None, None, True]

G7 = ['G7', True, False, False, False, 'You stand at the edge of the cliff and look down at the forest. The moon reflects off the lake in the distance.', None, None, True, None]

G8 = ['G8', False, True, True, False, 'You stand in the cave entrance. The air is cool and smells musty. At least you are protected from the howling wind in here. The forest lies SOUTH. The cave proceeds EAST.', None, None, True, None]

G9 = ['G9', True, True, False, True, 'The cave forks. Paths lead NORTH, EAST, and WEST.', None, None, True, None]

G10 = ['G10', False, True, False, True, 'The cave extends to the EAST and WEST.', None, None, True, None]

G11 = ['G11', True, True, False, True, 'The cave forks. Paths lead NORTH, EAST, and WEST.', None, None, True, None]

G12 = ['G12', True, False, False, True, 'You reach a bend. You can proceed NORTH or WEST.', None, None, True, None]

G13 = ['G13', False, False, False, False]

H0 = ['H0', False, False, False, False]

H1 = ['H1', False, True, True, False, 'The wood creaks as you step onto the boat dock. The sound of the sloshing water gives you a sinking feeling in your gut. A BOAT is tied to the SOUTH side of the dock.', None, None, True, None]

H2 = ['H2', True, True, True, True, 'You stand on the shore of a lake. A small boatdock extends onto the water to the WEST.', None, None, None, True]

H3 = ['H3', True, True, True, True, 'You stand in the woods. The forest extends to the NORTH, SOUTH, EAST, and WEST.', None, None, None, True]

H4 = ['H4', True, True, True, True, 'You enter a clearing where an old man sits at a campfire. He looks hungry. He hands you a mug of coffee and tells you to sit down. He rambles on about the end of the world. You try to ask him about getting help, but you cannot get a word in edgewise. Finally you stand up to leave.', None, None, None, True]

H5 = ['H5', True, False, True, True, 'A dense briar patch prevents you from going EAST. The forest extends in all directions.', None, None, None, True]

H6 = ['H6', True, True, True, False, 'A dense briar patch prevents you from going WEST. The forest extends in all directions.', None, None, None, True]

H7 = ['H7', False, True, True, True, 'You stand at the base of a cliff. There seems to be no way up. The forest extends to the EAST, WEST, and SOUTH.', None, None, None, True]

H8 = ['H8', True, False, True, True, 'You find yourself at the base of a cliff. The black, gaping mouth of a cave lay NORTH. The forest extends to the WEST and SOUTH.', None, None, None, True]

H9 = ['H9', False, False, False, False]

H10 = ['H10', False, False, False, False]

H11 = ['H11', False, False, False, False]

H12 = ['H12', False, False, False, False]

H13 = ['H13', False, False, False, False]

I0 = ['I0', False, False, False, False]

I1 = ['I1', True, False, False, False, 'You step into the boat. You attempt to start the engine, but to no avail. You check the tank; it is full of GAS but the engine will not turn over.', None, None, True, None]

I2 = ['I2', True, True, True, False, 'You stand on the shore of a lake. You hear the haunting call of a loon. The shorline extends to the NORTH and SOUTH. The forest lies to the EAST.', None, None, None, True]

I3 = ['I3', True, True, True, True, 'You stand in the woods. The forest extends to the NORTH, SOUTH, EAST, and WEST.', None, None, None, True]

I4 = ['I4', True, True, True, True, 'A cold wind whips through the trees. To the NORTH you see the warm glow of a fire.', None, None, None, True]

I5 = ['I5', True, True, True, True, 'The tire tracks lead to a small clearing and then disappear. A large, weathered sign reads: WELCOME TO CAMP GOLDENROD. Fun activities for the whole family. ROW BOATS available for rent. See the Forest Ranger office for CLIMBING GEAR.', 'MAP', '', None, True]

I6 = ['I6', True, True, True, True, 'You stand in the woods. The forest extends to the NORTH, SOUTH, EAST, and WEST.', None, None, None, True]

I7 = ['I7', True, True, True, True, 'The woods seem particularly dark in this area. You hear the hoot of a majestic OWL. The forest extends to the NORTH, SOUTH, EAST, and WEST.', None, None, None, True]

I8 = ['I8', True, True, True, True, 'You stand in a dark enclosure. The trees and underbrush have grown thick here. The forest extends to the NORTH, SOUTH, EAST, and WEST.', None, None, None, True]

I9 = ['I9', False, False, True, True, 'You find yourself at the base of a cliff. There seems to be no way up. The forest extends to the WEST and SOUTH.', None, None, None, True]

I10 = ['I10', False, False, False, False]

I11 = ['I11', False, False, False, False]

I12 = ['I12', False, False, False, False]

I13 = ['I13', False, False, False, False]

J0 = ['J0', False, False, False, False]

J1 = ['J1', False, False, False, False]

J2 = ['J2', True, True, False, False, 'You stand on the shore of a lake. The shorline extends to the NORTH. The forest lies to the EAST.', None, None, None, True]

J3 = ['J3', True, True, False, True, 'The forest is cold and dark. Your car lies EAST. The forest extends to the NORTH and WEST.', None, None, None, True]

J4 = ['J4', True, True, False, True, 'You look at your car. Better find a way to fix it so you can get out of this creepy place. The forest extends to the NORTH, EAST, and WEST.', None, None, None, True]

J5 = ['J2', True, True, False, True, 'Tire tracks lead into the woods and go NORTH. Your car lies WEST. The road lies SOUTH. The forest extends to the EAST.', None, None, None, True]

J6 = ['J6', True, True, False, True, 'You stand in the woods. The forest extends to the NORTH, EAST, and WEST. The road lies to the SOUTH.', None, None, None, True]

J7 = ['J7', True, True, False, True, 'A cold wind sweeps through the forest. You shiver and move on. The forest extends to the NORTH, EAST, and WEST.', None, None, None, True]

J8 = ['J8', True, True, False, True, 'The road lay to the SOUTH. The forest extends to the NORTH, EAST, and WEST.', None, None, None, True]

J9 = ['J9', True, False, False, True, 'The road closes you in on the SOUTH and EAST. This must be the curve in the road where you swerved to miss that ' + '"' + 'THING' + '".', None, None, None, True]

J10 = ['J10', False, False, False, False]

J11 = ['J11', False, False, False, False]

J12 = ['J12', False, False, False, False]

J13 = ['J13', False, False, False, False]

RA = [A0, A1, A2, A3, A4, A5, A6, A7, A8, A9, A10, A11, A12, A13]

RB = [B0, B1, B2, B3, B4, B5, B6, B7, B8, B9, B10, B11, B12, B13]

RC = [C0, C1, C2, C3, C4, C5, C6, C7, C8, C9, C10, C11, C12, C13]

RD = [D0, D1, D2, D3, D4, D5, D6, D7, D8, D9, D10, D11, D12, D13]

RE = [E0, E1, E2, E3, E4, E5, E6, E7, E8, E9, E10, E11, E12, E13]

RF = [F0, F1, F2, F3, F4, F5, F6, F7, F8, F9, F10, F11, F12, F13]

RG = [G0, G1, G2, G3, G4, G5, G6, G7, G8, G9, G10, G11, G12, G13]

RH = [H0, H1, H2, H3, H4, H5, H6, H7, H8, H9, H10, H11, H12, H13]

RI = [I0, I1, I2, I3, I4, I5, I6, I7, I8, I9, I10, I11, I12, I13]

RJ = [J0, J1, J2, J3, J4, J5, J6, J7, J8, J9, J10, J11, J12, J13]

allRows = [RA, RB, RC, RD, RE, RF, RG, RH, RI, RJ]

M0 = ['', '', '', '', '', '', '', '', '', '', '', '', '', '']
MA = ['', '', '', '', '', '', '', '', '', '', '', '', '', '']
M1 = ['', '', '', '', '', '', '', '', '', '', '', '', '', '']
MB = ['', '', '', '', '', '', '', '', '', '', '', '', '', '']
M2 = ['', '', '', '', '', '', '', '', '', '', '', '', '', '']
MC = ['', '', '', '', '', '', '', '', '', '', '', '', '', '']
M3 = ['', '', '', '', '', '', '', '', '', '', '', '', '', '']
MD = ['', '', '', '', '', '', '', '', '', '', '', '', '', '']
M4 = ['', '', '', '', '', '', '', '', '', '', '', '', '', '']
ME = ['', '', '', '', '', '', '', '', '', '', '', '', '', '']
M5 = ['', '', '', '', '', '', '', '', '', '', '', '', '', '']
MF = ['', '', '', '', '', '', '', '', '', '', '', '', '', '']
M6 = ['', '', '', '', '', '', '', '', '', '', '', '', '', '']
MG = ['', '', '', '', '', '', '', '', '', '', '', '', '', '']
M7 = ['', '', '', '', '', '', '', '', '', '', '', '', '', '']
MH = ['', '', '', '', '', '', '', '', '', '', '', '', '', '']
M8 = ['', '', '', '', '', '', '', '', '', '', '', '', '', '']
MI = ['', '', '', '', '', '', '', '', '', '', '', '', '', '']
M9 = ['', '', '', '', '', '', '', '', '', '', '', '', '', '']
MJ = ['', '', '', '', '', '', '', '', '', '', '', '', '', '']
M10 = ['', '', '', '', '', '', '', '', '', '', '', '', '', '']

mapArray = [M0, MA, M1, MB, M2, MC, M3, MD, M4, ME, M5, MF, M6, MG, M7, MH, M8, MI, M9, MJ, M10]

# Other variables

import random

introText = 'Driving home your car swerves off the road and gets stuck in a giant puddle of mud. Your rear left tire is now flat, and you are out of gas. You are miles from the nearest town and have not seen a pair of headlights in hours. You see tire tracks leading into the woods. Perhaps you can find someone or something in there to help you.'

instructions = 'HOW TO PLAY: Commands must be given in ALL CAPS. Valid commands include: GO NORTH, GO SOUTH, GO EAST, GO WEST, GET (ITEM), USE ITEM, INVENTORY, and HELP.'

inventory = ['KEYS', 'POCKET KNIFE', 'MRE']

endGame = False

chainAttached = False
tireFixed = False
carReleased = False
carFueled = False
gotTeaKettle = False

bloodCode = False
cheat = False

xPosition = 4
yPosition = 9

xBigfoot = 3
yBigfoot = 2


playerLocation = allRows[yPosition][xPosition]
bigfootLocation = allRows[yBigfoot][xBigfoot]

# Functions____________________________________________

def requestInput():
    validInput = False
    global xPosition
    global yPosition
    global endGame
    currentRoom = allRows[yPosition][xPosition]

#    print('Player is at tile ' + currentRoom[0])
    userInput = input('How will you proceed? ')

    while(validInput == False):

        if(userInput == 'GO NORTH' and currentRoom[1] == True):
            validInput = True
            yPosition = yPosition - 1
            currentRoom = allRows[yPosition][xPosition]
            loadTile(currentRoom)

        if(userInput == 'GO EAST' and currentRoom[2] == True):
            validInput = True
            xPosition = xPosition + 1
            currentRoom = allRows[yPosition][xPosition]
            loadTile(currentRoom)

        if(userInput == 'GO SOUTH' and currentRoom[3] == True):
            validInput = True
            yPosition = yPosition + 1
            currentRoom = allRows[yPosition][xPosition]
            loadTile(currentRoom)

        if(userInput == 'GO WEST' and currentRoom[4] == True):
            validInput = True
            xPosition = xPosition - 1
            currentRoom = allRows[yPosition][xPosition]
            loadTile(currentRoom)

        if(userInput == 'GET ' + str(currentRoom[6])):
            print('You take the ' + str(currentRoom[6]) + '.')
            inventory.append(currentRoom[6])
            currentRoom[6] = None
            validInput = True
            requestInput()

        if(userInput == 'USE ITEM'):
            whichItem = input('Which item would you like to use? ')
            for item in inventory:
                if(item == whichItem):
                    checkUsage(item, currentRoom)
            validInput = True
            if(endGame == True):
                gameOver()
            else:
                requestInput()

        if(userInput == 'INVENTORY'):
            print('You are carrying the following:')
            for item in inventory:
                print(item)
            validInput = True
            requestInput()

        if(userInput == 'HELP'):
            print(instructions)
            validInput = True
            requestInput()

        if(userInput == 'LETS CHEAT'):
            global cheat
            print('Cheating enabled.')
            cheat = True
            validInput = True
            requestInput()

        if(userInput == 'DONE CHEATING'):
            print('Cheating disabled.')
            cheat = False
            validInput = True
            requestInput()            

        else:
            if(endGame == True):
                validInput = True
            else:
                print('You cannot go that way.')
                validInput = False
                requestInput()

def checkUsage(prop, room):
    if(prop == 'MAP'):
        createMap()
    if(prop == 'MRE' and room[0] == allRows[7][4][0]):
        inventory.remove('MRE')
        print('You give the old man the MRE. A tear trickles down his cheek.' + '"' + 'Well...thank you.' + '"' 'He mutters. ' + '"' + 'You should take this with you. It might come in handy.' + '"' + ' He hands you a TEA KETTLE.')
        inventory.append('TEA KETTLE')
        global gotTeaKettle
        gotTeaKettle = True
        allRows[7][4][5] = 'The old man warms himself at the fire. He is no longer interested in talking.'
    if(prop == 'ROPE' and room[0] == allRows[4][5][0]):
        inventory.remove('ROPE')
        print('You make a loop at one end of the rope and throw it at the hook. It takes several tries, but eventually you loop it around the hook. You give it a good tug. The ROPE feels sturdy.')
        allRows[4][5][2] = True        
    if(prop == 'KEY' and room[0] == allRows[2][12][0]):
        inventory.remove('KEY')
        print('You place the KEY into the lock and turn it. The lock falls to the floor. You undo the chain and push open the door.')
        allRows[2][12][1] = True
    if(prop == 'CHAIN' and room[0] == allRows[9][4][0]):
       inventory.remove('CHAIN')
       global chainAttached
       chainAttached = True
       print('You attach the chain to the undercarriage of the car. You climb up a large, crooked tree that leans away from the car. You wrap the other end of the chain around the tree and secure it tightly.')
    if(prop == 'CHAINSAW' and room[0] == allRows[9][4][0] and chainAttached == True):
        inventory.remove('CHAINSAW')
        print('You rev up the CHAINSAW and take it to the base of the tree. It starts to give and you move out of the way. As the tree comes down it pulls your car out of the mud.')
        global carReleased
        carReleased = True
    if(prop == 'TIRE' and room[0] == allRows[9][4][0] and carReleased == True):
        inventory.remove('TIRE')
        global tireFixed
        tireFixed = True
        print('Amazingly, the tire fits your car perfectly.')
    if(prop == 'GAS CAN' and room[0] == allRows[9][4][0]):
        inventory.remove('GAS CAN')
        print('You use the GAS CAN to fill the gas tank of the car.')
        global carFueled
        carFueled = True
    if(prop == 'SURGICAL TUBING' and room[0] == allRows[8][1][0] and gotTeaKettle == True):
        inventory.remove('TEA KETTLE')
        inventory.append('GAS CAN')
        print('You siphon GAS from the boat engine. TEA KETTLE has been promoted to GAS CAN.')
    if(prop == 'KEYS' and room[0] == allRows[9][4][0] and carReleased == True and tireFixed == True and carFueled == True):
        print('You put the key in the ignition and pray that it works. The car starts right up. Before you know it you are twenty miles down the highway, happy to leave that forest behind you forever.')
        global endGame
        endGame = True
    if(prop == 'POCKET KNIFE' and room[8] == None):
        carving = input('You pull out your POCKET KNIFE to carve the bark of a tree. What will you carve? ')
        room[8] = carving
        room[5] = room[5] + ' There is a carving on a tree. It reads: ' + carving
        print('You carve: ' +'"' + carving + '"' ' into the bark of the tree.')
    if(prop == 'HATCHET' and room[0] == allRows[6][3][0]):
        print('You hack away at the mangled corpse. You get pretty dirty in the process. You wonder why you are doing this.')
        global bloodCode
        bloodCode = True
    if(prop == 'CHARCOAL' and room[9] == None):
        carving = input('You pull out the piece of CHARCOAL. What will you write? ')
        room[9] = carving
        room[5] = room[5] + ' You look closely. The following is written in charcoal: ' + carving
        print('You write: ' +'"' + carving + '"' '.')
        
def loadTile(room):
    print()
    global endGame
    determineDistance()
    if(endGame == True):
        gameOver()
    else:
        if(random.randint(0,1)):
            determineMovement()
        print(room[5])
        if(room[6]):
            print(room[7])
        requestInput()

def moveBigfoot(direction):
    global xBigfoot
    global yBigfoot
    global bigfootLocation
    global bloodCode
    global xPosition
    global yPosition

    if(bloodCode == True):
        if(xBigfoot >= xPosition):
            xBigfoot = xBigfoot - 1
        if(xBigfoot <= xPosition):
            xBigfoot = xBigfoot + 1
        if(yBigfoot >= yPosition):
            yBigfoot = yBigfoot - 1
        if(xBigfoot <= xPosition):
            yBigfoot = yBigfoot + 1
        bigfootLocation = allRows[yBigfoot][xBigfoot]

    if(bloodCode == False):
        if(direction == 1):
            yBigfoot = yBigfoot - 1
        if(direction == 2):
            xBigfoot = xBigfoot + 1
        if(direction == 3):
            yBigfoot = yBigfoot + 1
        if(direction == 4):
            xBigfoot = xBigfoot - 1
        bigfootLocation = allRows[yBigfoot][xBigfoot]

#    print('BIGFOOT is at tile ' + bigfootLocation[0])

def determineMovement():
    global xBigfoot
    global yBigfoot
    movementDirection = random.randint(1,4)
    if(allRows[yBigfoot][xBigfoot][movementDirection]):
        moveBigfoot(movementDirection)

def determineDistance():
    global xBigfoot
    global yBigfoot
    global xPosition
    global yPosition
    global endGame

    if(xBigfoot >= xPosition):
        currentDistanceX = xBigfoot - xPosition
    else:
        currentDistanceX = xPosition - xBigfoot

    if(yBigfoot >= yPosition):
        currentDistanceY = yBigfoot - yPosition
    else:
        currentDistanceY = yPosition - yBigfoot

    if(currentDistanceY + currentDistanceX == 2):
        print('You hear deep breathing and feel the ground quake under your feet.')

    if(currentDistanceY + currentDistanceX == 1):
        print('You sense movement nearby. You see a large shadow move quickly through the trees.')

    if(currentDistanceY + currentDistanceX == 0):
        print('Before you know what is happening, a large, hairy arm strikes you in the chest. You fly into the nearest solid object and your body crumbles to the ground. The last thing you hear is the sound of heavy footsteps running away.')
        global endGame
        endGame = True

def createMap():
    global xPosition
    global yPosition
    global xBigfoot
    global yBigfoot
    global cheat
    ticker = 0
    counter = 0
    stringArray = ['', '|', '', '|', '', '|', '', '|', '', '|', '', '|', '', '|', '', '|', '', '|', '', '|', '']

    while(counter < 10):
        while(ticker < 14):
            if(allRows[counter][ticker][1]):
                mapArray[counter * 2][ticker] = '    '
            else:
                mapArray[counter * 2][ticker] = ' ---'
            if(allRows[counter][ticker][2]):
                mapArray[counter * 2 + 1][ticker] = '    '
            else:
                mapArray[counter * 2+ 1][ticker] = '   |'
            if(counter == yPosition and ticker == xPosition):
                mapArray[counter * 2+ 1][ticker] = ' X |'
            if(counter == yPosition and ticker == xPosition and allRows[counter][ticker][2]):
                mapArray[counter * 2+ 1][ticker] = ' X  '
            if(cheat == True):
                if(counter == yBigfoot and ticker == xBigfoot):
                    mapArray[counter * 2+ 1][ticker] = ' B |'
                if(counter == yBigfoot and ticker == xBigfoot and allRows[counter][ticker][2]):
                    mapArray[counter * 2+ 1][ticker] = ' B  '
            stringArray[counter * 2] = stringArray[counter * 2] + mapArray[counter * 2][ticker]
            stringArray[counter * 2 + 1] = stringArray[counter * 2 + 1] + mapArray[counter * 2 + 1][ticker]
            ticker = ticker + 1

        print(stringArray[counter * 2])
        print(stringArray[counter * 2 + 1])

        counter = counter + 1
        ticker = 0

def startGame():
    print('|-------------------------|')
    print('|                         |')
    print('|        WELCOME TO       |')
    print('|                         |')
    print('|       DEATH  WOODS      |            _____  ')
    print('|                         |           /     \ ')
    print('|_________________________|           X 0    |')
    print('|                         |          m      / ')
    print('|                         |        III __/    ')
    print('|                         |       /___/       ')
    print()
    print(introText)
    print()
    print(instructions)
    global xPosition
    global yPosition
    currentRoom = allRows[yPosition][xPosition]
    loadTile(currentRoom)

def gameOver():
    print('GAME OVER')


# Execute Game______________________________________

startGame()


