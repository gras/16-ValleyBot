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
 
from drive import testMotors
from drive import driveTimed
from drive import drive
from drive import timedLineFollowLeft
from drive import timedLineFollowRight
from drive import timedLineFollowRightSmooth
from drive import timedLineFollowLeftSmooth
from drive import timedLineFollowLeftBack

from servos import testServos
from servos import moveFrontArm
from servos import moveFrontClaw
from servos import moveBackClaw
from servos import moveBackArm

from sensors import waitForButton
from sensors import onBlackBack
from sensors import onBlackFront
from sensors import crossBlackFront
from sensors import DEBUG
from constants import isPrime


# Tests all hardware
def init():
    if c.isPrime:
        print "Running Valley - Prime"
    else:
        print "Running Valley - Clone"   
    testServos()
    testMotors()
    disable_servos()
    waitForButton()
    c.startTime = seconds()
    enable_servos()
    moveFrontClaw(c.frontClawClose, 25)
    moveFrontArm(c.frontArmUp, 25) 
    moveBackClaw(c.backClawClose, 25)
    moveBackArm(c.backArmUp, 25)

# Raises cube holder
# Backs out of start box and turns 
# Moves backward until black tape
def getOutOfStartBox():
    print "getOutOfStartBox"
    msleep(500)
    driveTimed(-100, -100, 1600)
    driveTimed(0, 100, 400)
    driveTimed(70,70,600)

# Follows line for 3.5 seconds
# Moves forward until robot reaches debris
def goToDebris():
    print "goToDebris"
    if c.isPrime:
        timedLineFollowLeft(3.75) 
        timedLineFollowLeftSmooth(0.75)
        driveTimed(50, 50, 1000)
    else:
        timedLineFollowLeft(5.0)
        timedLineFollowLeftSmooth(1.25)
        driveTimed(50, 57, 1000)


# Moves claw arm down and drives backwards with debris
def removeDebris():
    print "removeDebris"
    moveFrontArm(c.frontArmDown, 15)
    msleep(500)
    driveTimed(-80, -80, 1000)

# Dumps debris next to compost
def dumpDebris():
    print "removeDebris"
    if c.isPrime:
        driveTimed(0,-100,1100)#1000
        driveTimed(60,70,500)
        driveTimed(90,0,600)#500
        driveTimed(60,90,225)
        driveTimed(60,70,900)#1000
    else:
        driveTimed(0,-100,900)
        driveTimed(60,70,500)
        driveTimed(90,0,500)#600
        driveTimed(60,90,350)
        driveTimed(60,70,1000)
        
# Drives backwards and follows line to reach gate
def goToGate():
    print "goToGate"
    moveFrontArm(c.frontArmUp, 15)
    if c.isPrime:
        driveTimed(-90,-100, 1450)
        timedLineFollowRight(2.5)
        timedLineFollowRightSmooth(3.2) 
    else:
        driveTimed(-100,-100, 1300)
        timedLineFollowRight(2.7)
        timedLineFollowRightSmooth(3.2) 
        
# Drives to the rift valley cube
def goToCube():
    print "goToCube"
    moveFrontClaw(c.frontClawOpen, 15)
    moveFrontArm(c.frontArmMidCube, 15)
    driveTimed(100,100,500)
    if c.isPrime:
        drive(100, 100)
    else:
        drive(90, 100)
    while not onBlackFront():
        pass
    drive(0, 0)
    moveFrontClaw(c.frontClawMid, 15)
    moveFrontArm(c.frontArmUp, 15)
    msleep(500)

# Turns to drop cube off on our side of the board
def dropOffCube():
    print"dropOffCube"
    driveTimed(100, 0, 1900)
    moveFrontArm(c.frontArmMidCube, 15)
    moveFrontClaw(c.frontClawOpen, 20)#15
    msleep(500)
    moveFrontArm(c.frontArmUp, 15)
    
# drives to and grabs gold poms
def getGoldPoms():
    print"getGoldPoms"
    if isPrime:
        driveTimed(-70, 0, 400)
    else:
        driveTimed(-70, 0, 230)
    moveBackClaw(c.backClawOpen, 15)
    moveBackArm(c.backArmDown, 15)
    driveTimed(-100, -100, 700)
    if isPrime:
        drive(-20, -20)
        moveBackClaw(c.backClawClose, 10)
        ao()
    else:
        drive(-20, -20)
        moveBackClaw(c.backClawClose, 10)
        ao()
    moveBackArm(c.backArmUp, 10)
    
# Go to Red Poms
def getRedPoms():
    print "getRedPoms"    
    drive(0, 40)
    while not onBlackFront(): # wait for black
        pass
    ao()
    drive(20, 0)
    while onBlackFront(): # wait for black
        pass
    ao()
    driveTimed(20, 0, 200)
    moveFrontArm(c.frontArmDown, 15)
    driveTimed(100, 100, 800)
    drive(30, 30)
    moveFrontClaw(c.frontClawClose, 6)
    drive(0,0)
    moveFrontArm(c.frontArmUp, 10)
    
# Exit Valley  
def leaveValley():
    print "leaveValley"
    driveTimed(-80, -80, 720)#1100, 650
    if isPrime:
        driveTimed(-70,0, 1900)
    else:
        driveTimed(-70, 0, 1500)               
         
# go to Habitat wait to score
def goToHabitat():
    print "goToHabitat"
    driveTimed(-100, -100, 1000) #back through gate
    drive(-50, 0) #angle robot to find black line
    while not onBlackBack():
        pass
    if isPrime:
        timedLineFollowLeftBack(5.0)
    else:
        timedLineFollowLeftBack(3.0)
    driveTimed(-30, -30, 1000)
    if isPrime:
        driveTimed(50, 50, 750) 
    else:
        driveTimed(50, 50, 500) 

#wait For tater bot
def waitForTater():
    print "waitForTater"

# Score Poms   
def depositGoldPoms():
    print"depositGoldPoms"
    moveBackArm(c.backArmMid, 10)
    moveBackClaw(c.backClawOpen, 10)
        
# Score Poms   
def depositRedPoms():
    print"depositRedPoms"
    moveBackArm(c.backArmUp, 10)
    moveBackClaw(c.backClawClose, 10)   
    driveTimed(70, 70, 1400)
    if isPrime:
        driveTimed(-100, 100, 1000)
        drive(-50, 50)
        crossBlackFront()
        timedLineFollowLeftSmooth(4)
        driveTimed(50, 50, 300)
    else:
        #adjust to match prime? line follow
        driveTimed(-100, 100, 1200) 
        driveTimed(70, 70, 1400)
    moveFrontArm(c.frontArmMidPom, 10)
    moveFrontClaw(c.frontClawOpen, 10)
    moveFrontArm(c.frontArmUp, 10)
    moveFrontClaw(c.frontClawClose, 10)
    
    
# Get to Valley    
def getComposter():
    print "getComposter"
    driveTimed(-100,-100, 500)
    driveTimed(65, 0, 1700)#1735
    driveTimed(-100, -100, 600) #670
    msleep(400);
    moveBackClaw(c.backClawOpen,10)
    moveBackArm(580, 10)
    moveBackClaw(1050, 10)
    moveBackArm(c.backArmUp, 10)
    msleep(1000);
    
        
# moves gold poms to habitat 
def deliverComposter():
    print "deliverComposter"
    driveTimed(60,60,900)
    driveTimed (50,-50, 1200)
    driveTimed(-80, -80, 250)

# Go back to valley
def returnToValley():
    print "returnToValley"
    moveFrontArm(c.frontArmUp, 15)
    moveFrontClaw(c.frontClawClose, 15)
    driveTimed (-50,-50,230)
    driveTimed (100,-70,500)
    drive (40,0)
    crossBlackFront()
    timedLineFollowRightSmooth(1.55)
    driveTimed(60, 0, 250)
    driveTimed (80,80,1200)
    

'''# Go to Red Poms
def getRedPoms():
    print "getRedPoms"
    drive(60, 60)
    while not onBlack():
        pass
    drive(0, 0)
    driveTimed(70,0,1150)
    moveFrontClaw(c.clawOpen, 25)
    moveFrontArm(c.armDown, 25)
    driveTimed(80, 80, 700)
    moveFrontClaw(c.clawClosed, 15) 
    msleep(300)
    moveFrontClaw(c.clawOpen,15)
    driveTimed(50,50,400)
    moveFrontClaw(c.clawClosed, 15)
    moveFrontArm(c.armUp, 15)
  '''

    