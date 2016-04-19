#16-ValleyBot actionpy
'''
Created on Mar 13, 2016

@author: Dead Robot Society
'''
import constants as c

from wallaby import seconds
from wallaby import ao
from wallaby import disable_servos
from wallaby import enable_servos
from wallaby import msleep
from wallaby import shut_down_in
 
from drive import testMotors
from drive import driveTimed
from drive import drive
from drive import timedLineFollowLeft
from drive import timedLineFollowRight
from drive import timedLineFollowRightSmooth
from drive import timedLineFollowLeftSmooth
from drive import lineFollowRightSmoothCount
from drive import timedLineFollowLeftBack

from servos import testServos
from servos import moveFrontArm
from servos import moveFrontClaw
from servos import moveBackClaw
from servos import moveBackArm


from sensors import onBlackBack 
from sensors import crossBlackFront
from sensors import onBlackFront
from sensors import wait4light
from sensors import testSensors
from sensors import DEBUG

# Tests all hardware
def init():
    if c.isPrime:
        print "Running Valley - Prime"
    else:
        print "Running Valley - Clone"   
    testSensors()
    testServos()
    testMotors()
    disable_servos()
    wait4light()
    shut_down_in(119.9)
    c.startTime = seconds()
    moveFrontClaw(c.frontClawClose, 25)
    moveFrontArm(c.frontArmUp, 25) 
    moveBackClaw(c.backClawMidSolar, 25)
    moveBackArm(c.backArmUp, 25)
    enable_servos()
    
# Raises cube holder
# Backs out of start box and turns 
# Moves backward until black tape
def getOutOfStartBox():
    print "getOutOfStartBox"
    msleep(500)
    driveTimed(-100, -100, 2300)#2600
    driveTimed(0, 100, 400)
    driveTimed(70,70,600)

# Follows line for 3.5 seconds
# Moves forward until robot reaches debris
def goToDebris():
    print "goToDebris"
    timedLineFollowLeft(3.75)
    if c.isPrime:
        driveTimed(-70, 70, 750)
    else:
        driveTimed(-70, 70, 700)
    driveTimed(-50, -50, 1400)
    if c.isPrime:
        pass
    else:
        driveTimed(-20, 20, 200)
    moveBackArm(c.backArmDown, 15)
    moveBackClaw(c.backClawOpen, 15) #DELIVERS SOLAR ARRAYS
    moveBackArm(c.backArmUp, 15)
    moveBackClaw(c.backClawClose, 15)
    driveTimed(50, 50, 1400)
    driveTimed(70, -70, 750)
    timedLineFollowLeftSmooth(.75)
    driveTimed(50, 50, 1000)

# Moves claw arm down and drives backwards with debris
def removeDebris():
    print "removeDebris"
    moveFrontArm(c.frontArmDown, 15)
    msleep(500)
    driveTimed(-80, -80, 1000)

# Dumps debris next to compost
def dumpDebris():
    print "removeDebris"
    driveTimed(0,-100,1100)
    driveTimed(60,70,500)
    driveTimed(90,0,600)
    driveTimed(60,90,225)
    driveTimed(60,70,800)#900
#####Clone debugged to here!    
        
# Drives backwards and follows line to reach gate
def goToGate():
    print "goToGate"
    moveFrontArm(c.frontArmUp, 15)
    driveTimed(-90,-100, 1450)
    timedLineFollowRight(3.2)
    timedLineFollowRightSmooth(1.0)
    lineFollowRightSmoothCount(10)#7 
    
# Drives to the rift valley cube
def goToCube():
    print "goToCube"
    moveFrontClaw(c.frontClawOpen, 15)
    moveFrontArm(c.frontArmDown, 15)
    if c.isPrime:
        driveTimed(100,100,500)
    else: 
        driveTimed(100, 90, 500)
    drive(100, 100)
    while not onBlackFront():
        pass
    drive(0, 0)
    driveTimed(-65, -65, 300)
    moveFrontArm(c.frontArmMidCube, 15)
    moveFrontClaw(c.frontClawCube, 15)
    moveFrontArm(c.frontArmUp, 15)
    driveTimed(80, 80, 400)
    msleep(500)

# Turns to drop cube off on our side of the board
def dropOffCube():
    print"dropOffCube"
    driveTimed(100, 0, 2400)
    moveFrontArm(c.frontArmMidCube, 15)
    moveFrontClaw(c.frontClawOpen, 20)#15
    msleep(500)
    moveFrontArm(c.frontArmUp, 15)
    
# drives to and grabs gold poms
def getGoldPoms():
    print"getGoldPoms"
    driveTimed(-70, 0, 500)
    drive(-70, 0)
    while not onBlackBack():# turn to black
        pass
    ao()
    moveBackClaw(c.backClawOpen, 15)
    moveBackArm(c.backArmDown, 15)
    driveTimed(-100,-100,1000)   
    drive(-20, -20)
    moveBackClaw(c.backClawClose, 8)
    ao()
    moveBackArm(c.backArmUp, 10)
    
# Go to Red Poms
def getRedPoms():
    print "getRedPoms"    
    drive(0, 40)
    while not onBlackFront(): # wait for black
        pass
    drive(20, 0)
    while onBlackFront(): # wait for white
        pass
    ao()
    moveFrontArm(c.frontArmDown, 15)
    driveTimed(93, 100, 1000)
    drive(30, 30)
    msleep(500)
    moveFrontClaw(c.frontClawClose, 6)
    drive(0,0)
    moveFrontArm(c.frontArmUp, 10)
    
# Exit Valley  
def leaveValley():
    print "leaveValley"
    driveTimed(-65, -65, 720)#1100, 650
    if c.isPrime:
        driveTimed(-90,0, 1650) #1750
    else:
        driveTimed(-90, 0, 1550)  
    driveTimed(-100, -100, 1000) #back through gate
    if not onBlackBack():    
        drive(-50, -30) #angle robot to find black line
        while not onBlackBack():
            pass
    drive(-50, -30) 
    while onBlackBack():
        pass   
    timedLineFollowLeftBack(2.0) 
    
#wait For tater bot
def waitForTater():
    print "waitForTater"
    print "press button to continue..."
    msleep(2500) #was 4000     
         
# go to Habitat wait to score
def goToHabitat():
    print "goToHabitat"
    timedLineFollowLeftBack(2.0)#was 3.0
    driveTimed(-30, -30, 1000)
    if c.isPrime:
        driveTimed(50, 50, 300) 
    else:
        driveTimed(50, 50, 500) 

# Score Poms   
def depositGoldPoms():
    print"depositGoldPoms"
    moveBackArm(c.backArmBinGrab, 10)
    if c.isPrime:
        driveTimed(50, 50, 500)
    else:
        driveTimed(50, 50, 250)
    #msleep(1000)
    moveBackArm(c.backArmMid, 10)
    #msleep(1000)
    moveBackClaw(c.backClawOpen, 10)
        
# Score Poms   
def depositRedPoms():
    print"depositRedPoms"
    moveBackArm(c.backArmUp, 50)#10
    driveTimed(70, 70, 400)
    if c.isPrime:
        driveTimed(-100, 100, 1200)
        #drive(-50, 50)
        driveTimed(50, 50, 350) #was 200
    else:
        driveTimed(-100, 100, 1200) 
        driveTimed(70, 70, 1400)
    moveFrontArm(c.frontArmMidPom, 10)
    moveFrontClaw(c.frontClawOpen, 10)
    moveFrontArm(c.frontArmUp, 10)
    
# Get to Valley    
def getComposter():
    print "getComposter"
    driveTimed(-100,-100, 500)
    driveTimed(65, 0, 1620)#1690
    driveTimed(-100, -100, 500) #600
    msleep(400);
    moveBackClaw(c.backClawOpen,10)
    moveBackArm(c.backArmCompGrab, 10)
    moveBackClaw(c.backClawCompGrab, 35)
    moveBackArm(c.backArmUp, 10)


    
# moves composter to potato bin in habitat 
def deliverComposter():
    print "deliverComposter"
    driveTimed(60,60,900)
    driveTimed (50,-50, 1300)#1200
    driveTimed(-80, -80, 250)

    
# Score poop   
def depositComposter():
    print"depositComposter"
    moveBackArm(c.backArmCompGrab, 10)
    moveBackClaw(c.backClawOpenComp, 10)
    moveBackArm(c.backArmUp, 10)
   
def goToCube2():
    print"goToCube2"
    driveTimed(50, 50, 500)
    driveTimed(50, -50, 450)#600
    driveTimed(50, 50, 500)
    moveFrontClaw(c.frontClawOpen, 15)
    moveFrontArm(c.frontArmMidCube, 15)
    msleep(100)
    moveFrontClaw(c.frontClawCube, 10)
    moveFrontArm(c.frontArmUp, 15)
    msleep(200)
    
def scoreCube():
    print"scoreCube"
    driveTimed(-75,75,1575)#1650
    moveFrontArm(c.frontArmDown, 15)
    moveFrontClaw(c.frontClawOpen, 15)
    driveTimed(50, 50, 950)#900
    
def returnToValley():
    print "returnToValley"
    driveTimed(-50, -50, 500)
    moveFrontArm(c.frontArmUp, 15)
    drive (50, -50)
    crossBlackFront()
    driveTimed (100, 85, 1300)
    drive(100, 100)
    crossBlackFront()
    timedLineFollowRight(2.8)
    timedLineFollowRightSmooth(1.0)
    driveTimed(0, 50, 150)
    ao()
    
def deliverBotGuy():
    print "deliverBotGuy"
    moveFrontArm(c.frontArmGrabBot, 15)
    msleep(500)
    moveFrontClaw(c.frontClawClose, 2000)
    msleep(500)
    moveFrontArm(c.frontArmUp, 15)
    msleep(500)
    driveTimed(70, 60, 3400)#was 3500
    driveTimed(-50, 50, 1450)
    driveTimed(50, 50, 1000)
    moveFrontArm(c.frontArmGrabBot, 15)
    #moveFrontClaw(c.frontClawOpen, 15)
    #moveFrontArm(c.frontArmUp, 30)
    msleep(500)   
    
def crabDance():
    print "crabDance"
    moveBackArm(c.backArmUp, 15)
    moveBackClaw(c.backClawOpen, 15)
    msleep(200)
    moveFrontClaw(c.frontClawOpen, 15)
    msleep(200)
    moveBackClaw(c.backClawClose, 15)
    msleep(200)
    moveFrontClaw(c.frontClawClose, 15)
    msleep(200)
    moveBackClaw(c.backClawOpen, 15)
    msleep(200)
    moveFrontClaw(c.frontClawOpen, 15)
    msleep(200)
    moveBackClaw(c.backClawClose, 15)
    msleep(200)
    moveFrontClaw(c.frontClawClose, 15)
    msleep(200)
    
    
    