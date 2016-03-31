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
FRONT_TOPHAT = 0
REAR_TOPHAT = 1


# DIGITAL ports
CLONE_SWITCH = 9
RIGHT_BUTTON = 13

# PRIME servo positions
frontArmUp = 1200 #Arm at 90 degrees up
frontArmMidCube = 520 #Arm at 30 degrees up
frontArmMidPom = 700 #Arm at 30 degrees up
frontArmDown = 100 #Arm forward on ground
frontClawOpen = 1670 #Claw open
frontClawMid = 800 # claw cube grab
frontClawClose = 200 # Claw closed
backClawOpen = 0
backClawMid = 550
backClawClose = 1250
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
    frontArmUp = 1900 # Arm at 90 degrees up
    frontArmDown = 630 # Arm forward on ground
    frontArmMidCube = 1200
    frontArmMidPom = 1300
    frontClawOpen = 2000 # Claw open
    frontClawMid = 1500
    frontClawClose = 800 # Claw closed
    backArmUp = 1400
    backArmDown = 440
    backArmMid = 1000
    backClawClose = 1600
    backClawOpen = 500
    backClawMid = 1100
        