#16-ValleyBot constants.py

'''
Created on Mar 13, 2016

@author: Dead Robot Society
'''
import wallaby as w  

# Start light threshold
startLightThresh = 2000

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
STARTLIGHT = 2


# DIGITAL ports
CLONE_SWITCH = 9
RIGHT_BUTTON = 13

# PRIME servo positions
frontArmUp = 1200 #Arm at 90 degrees up
frontArmMidCube = 450 #Arm at 30 degrees up
frontArmGrabBot = 550 #grabs BotGuy well
frontArmMidPom = 700 #Arm at 30 degrees up
frontArmDown = 100 #Arm forward on ground
frontClawOpen = 2000 #Claw open
frontClawMid = 1400 # claw cube grab
frontClawCube = 1150 
frontClawClose = 830 # Claw closed
backClawOpen = 00
backClawOpenComp = 350
backClawMid = 1250
backClawMidSolar = 1500
backClawClose = 2000 
backClawCompGrab = 1550
backArmDown = 250
backArmBinGrab = 560 #when the backArm pulls bin
backArmCompGrab = 580
backArmMid = 730
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
    frontArmMidCube = 1100 #Arm at 30 degrees up
    frontArmGrabBot =  1200 #grabs BotGuy well
    frontArmMidPom = 1300
    frontArmDown = 630 # Arm forward on ground
    
    frontClawOpen = 1400 # Claw open
    frontClawMid = 600 #1500
    frontClawCube = 500
    frontClawClose = 200 # Claw closed     
    
    backClawOpen = 100
    backClawOpenComp = 350
    backClawMid = 700
    backClawMidSolar = 1300
    backClawClose = 1275
    backClawCompGrab = 1550
    
    backArmDown = 440
    backArmBinGrab = 750
    backArmCompGrab = 780
    backArmMid = 1000
    backArmUp = 1400
    
        