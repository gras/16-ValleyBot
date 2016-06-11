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
frontArmSwitch = 1500
frontArmUp = 1200 #Arm at 90 degrees up
frontArmMidPom = 700 #Arm at 30 degrees up
frontArmGrabBot = 550 #grabs BotGuy well
frontArmMidCube = 450 #Arm at 30 degrees up
frontArmMidDown = 325 #added during comp for crease
frontArmSwing = 200
frontArmDown = 100 #Arm forward on ground

#Front Claw
frontClawOpen = 2000 #Claw open
frontClawMid = 1400 # claw cube grab
frontClawCube = 1150 
frontArmUpRamp = 850
frontClawClose = 830 # Claw closed

#Back Claw
backClawOpen = 00
backClawOpenComp = 350
backClawMid = 1250
backClawMidSolar = 1500
backClawCompGrab = 1550
backClawClose = 2000 

#Back Arm
backArmDown = 250
backArmBinGrab = 560 #when the backArm pulls bin
backArmCompGrab = 580
backArmMid = 730
backArmUp = 1200
backArmSwitch = 1700

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
    frontArmMidDown = 1000 #added during comp for crease
    frontArmSwing = 750
    frontArmUpRamp = 1350
    
    frontClawOpen = 1400 # Claw open
    frontClawMid = 600 
    frontClawCube = 500
    frontClawClose = 200 # Claw closed     
    
    backClawOpen = 500
    backClawOpenComp = 350
    backClawMid = 700
    backClawMidSolar = 1300
    backClawCompGrab = 1550
    
    backClawClose = 1450
    backClawSmallSolar = 1122
    
    backArmDown = 440
    backArmBinGrab = 750
    backArmCompGrab = 780
    backArmMid = 1000
    backArmUp = 1400
    backArmPushSolar = 600
    
    frontArmSwitch = 2047 #1950
    backArmSwitch = 2047
    
        