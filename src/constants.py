#16-ValleyBot constants.py
'''
Created on Mar 13, 2016

@author: Dead Robot Society
'''
import wallaby as w  #  need to fix *********************************

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
armUp = 1200 #Arm at 90 degrees up
armMid = 520 #Arm at 30 degrees up
armDown = 200 #Arm forward on ground
clawOpen = 1670 #Claw open
clawMid =1100 # claw cube grab
clawClosed = 500 # Claw closed
cubeMid = 1000 
cubeUp = 775
cubeDown = 1600

isClone = w.digital(CLONE_SWITCH)
isPrime = not isClone    

#define clone values here
if isClone:
    # servo positions
    armUp = 2000 # Arm at 90 degrees up
    armDown = 600 # Arm foward on ground
    clawOpen = 2000 # Claw open
    clawClosed = 800 # Claw closed
    cubeMid = 1450
    cubeUp = 775
    cubeDown = 1600
