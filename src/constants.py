#16-ValleyBot constants.py
'''
Created on Mar 13, 2016

@author: Dead Robot Society
'''
import wallaby as w

# servo ports
ARM = 0
CLAW = 1
CUBE_HOLDER = 2

# motor ports
LMOTOR = 0
RMOTOR = 3

# digital ports
CLONE_SWITCH = 9
RIGHT_BUTTON = 13

# analog ports
LINE_FOLLOWER = 0

 
# servo positions
UP = 1200 #Arm at 90 degrees up
MID = 520 #Arm at 30 degrees up
DOWN = 200 #Arm forward on ground
OPEN = 1670 #Claw open
CLOSE = 600 # Claw closed
MID_VALUE = 1000 
RAISED = 775
LOWERED = 1600

isClone = w.digital(CLONE_SWITCH)
isPrime = not isClone    

#define clone values here
if isClone:
    # servo positions
    UP = 2000 # Arm at 90 degrees up
    DOWN = 600 # Arm foward on ground
    OPEN = 2000 # Claw open
    CLOSE = 800 # Claw closed
    MID_VALUE = 1450
    RAISED = 775
    LOWERED = 1600
