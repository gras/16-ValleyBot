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
frontArm = 0
frontClaw = 1
backArm = 2
backClaw = 3

# ANALOG ports
LINE_FOLLOWER = 0

# DIGITAL ports
CLONE_SWITCH = 9
RIGHT_BUTTON = 13

# PRIME servo positions
frontArmUp = 1200 #Arm at 90 degrees up
frontArmMid = 520 #Arm at 30 degrees up
frontArmDown = 200 #Arm forward on ground
frontClawOpen = 1670 #Claw open
frontClawMid = 800 # claw cube grab
frontClawClose = 200 # Claw closed
backClawOpen = 350
backClawMid = 850
backClawClose = 1350
backArmDown = 250
backArmMid = 600
backArmUp = 1200

# PRIME analog sensor values
frontLineFollowerGrey = 1000



isClone = w.digital(CLONE_SWITCH)
isPrime = not isClone    


if isPrime:
    print "running Prime"
else:
    print "running Clone"
    # servo positions
    frontArmUp = 2000 # Arm at 90 degrees up
    frontArmDown = 600 # Arm foward on ground
    frontClawOpen = 2000 # Claw open
    frontClawClose = 800 # Claw closed

        