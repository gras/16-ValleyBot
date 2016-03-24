#16-ValleyBot constants.py

'''
Created on Mar 13, 2016

@author: Dead Robot Society
'''
import wallaby as w  

# TIME
startTime = -1

# Motor ports
LMOTOR = 0
RMOTOR = 3

# SERVO ports
ARM = 0
CLAW = 1
CUBE_HOLDER = 2

# ANALOG ports
LINE_FOLLOWER = 0

# DIGITAL ports
CLONE_SWITCH = 9
RIGHT_BUTTON = 13

# PRIME servo positions
armUp = 1200 #Arm at 90 degrees up
armMid = 520 #Arm at 30 degrees up
armDown = 200 #Arm forward on ground
clawOpen = 1670 #Claw open
clawMid = 800 # claw cube grab
clawClose = 200 # Claw closed
cubeMid = 1000 
cubeUp = 775
cubeDown = 1600

isClone = w.digital(CLONE_SWITCH)
isPrime = not isClone    


if isPrime:
    print "running Prime"
else:
    print "running Clone"
    # servo positions
    armUp = 2000 # Arm at 90 degrees up
    armDown = 600 # Arm foward on ground
    clawOpen = 2000 # Claw open
    clawClose = 800 # Claw closed
    cubeMid = 1450
    cubeUp = 775
    cubeDown = 1600

        