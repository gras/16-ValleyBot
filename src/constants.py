#16-ValleyBot constants.py

'''
Created on Mar 13, 2016

@author: Dead Robot Society
'''
import wallaby as w  

# Start light threshold
startLightThresh = 2000
ETbotGuy = 2900

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
ET = 2

# DIGITAL ports
TOUCH = 0
CLONE_SWITCH = 9
RIGHT_BUTTON = 13

# PRIME servo positions
frontArmDown = 100 #Arm forward on ground
frontArmSwing = 200
frontArmSweep = 275
frontArmMidDown = 350 #added during comp for crease
frontArmMidCube = 450 #Arm at 30 degrees up
frontArmGrabBot = 485 #grabs BotGuy well
frontArmMidPom = 700 #Arm at 30 degrees up
frontArmUpRamp = 900
frontArmUp = 1200 #Arm at 90 degrees up
frontArmSwitch = 1400
frontArmGrabCube = 377
frontArmSolarPanel = 535

#Front Claw
frontClawClose = 830 # Claw closed
frontClawCube = 1150 
frontClawMid = 1400 # claw cube grab
frontClawOpen = 1850 #Claw open

#Back Claw
backClawOpen = 00
backClawOpenComp = 350
backClawDropSolar = 750
backClawSmallSolar = 900
backClawMid = 1250
backClawMidSolar = 1500
backClawCompGrab = 1550
backClawClose = 1300 
backClawStart = 450
backClawSqueeze = 1600

#Back Arm
backArmDown = 250
backArmSweep = 325
backArmPushSolar = 380
backArmBinGrab = 560 #when the backArm pulls bin
backArmCompGrab = 580
backArmMid = 730
backArmWipe= 850 # gets red pom off solars
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
    frontArmDown = 630 # Arm forward on ground
    frontArmSwing = 750
    frontArmSweep = 850
    frontArmMidDown = 1000 #added during comp for crease
    frontArmMidCube = 1100 #Arm at 30 degrees up
    frontArmGrabBot =  1200 #grabs BotGuy well
    frontArmMidPom = 1300
    frontArmUpRamp = 1400
    frontArmUp = 1900 # Arm at 90 degrees up
    
    #Front Claw
    frontClawClose = 200 # Claw closed     
    frontClawCube = 500
    frontClawMid = 600 
    frontClawOpen = 1400 # Claw open
    
    #Back Claw
    backClawOpenComp = 350 
    backClawOpen = 500
    backClawMid = 700
    backClawSmallSolar = 850
    backClawMidSolar = 1300
    backClawClose = 1450
    backClawCompGrab = 1550
    backClawCloseBlock = 1675
    
    #Back Arm
    backArmDown = 440
    backArmPushSolar = 600
    backArmBinGrab = 750
    backArmCompGrab = 780
    backArmWipe= 850 # gets red pom off solars
    backArmMid = 1000
    backArmUp = 1400
    
    frontArmSwitch = 2047 #1950
    backArmSwitch = 2047
    
        