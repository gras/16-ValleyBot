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

from servos import testServos
from servos import moveFrontArm
from servos import moveFrontClaw
from servos import moveBackClaw
from servos import moveBackArm

from sensors import waitForButton
from sensors import onBlack
from sensors import crossBlack
from sensors import DEBUG
from constants import isPrime


# Tests all hardware
def init():
    print "Running Valley"
    testServos()
    testMotors()
    disable_servos()
    waitForButton()
    enable_servos()
    moveFrontClaw(c.frontClawClose, 25)
    moveFrontArm(c.frontArmUp, 25) 
    moveBackClaw(c.backClawClose, 25)
    moveBackArm(c.backArmUp, 25)
    c.startTime = seconds()

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
        timedLineFollowLeft(3.0) 
        timedLineFollowLeftSmooth(0.75)
        driveTimed(50, 50, 1000)
    else:
        timedLineFollowLeft(4.0)
        timedLineFollowLeftSmooth(0.75)
        driveTimed(50, 53, 1000)


# Moves claw arm down and drives backwards with debris
def removeDebris():
    print "removeDebris"
    moveFrontArm(c.frontArmDown, 15)
    msleep(500)
    driveTimed(-80, -80, 1000)

# Dumps debris next to compost
def dumpDebris():
    print "removeDebris"
    if isPrime:
        driveTimed(0,-100,1100)#1000
        driveTimed(60,70,500)
        driveTimed(90,0,600)#500
        driveTimed(60,90,225)
        driveTimed(60,70,650)
    else:
        driveTimed(0,-100,1100)#1000
        driveTimed(60,70,500)
        driveTimed(90,0,500)#600
        driveTimed(60,90,200)
        driveTimed(60,70,900)
# Drives backwards and follows line to reach gate
def goToGate():
    print "goToGate"
    moveFrontArm(c.frontArmUp, 15)
    if isPrime:
        driveTimed(-100,-100, 1250)
        timedLineFollowRight(2.0)
        timedLineFollowRightSmooth(3.0) 
    else:
        driveTimed(-100,-100, 1300)
        timedLineFollowRight(2.5)
        timedLineFollowRightSmooth(3.7) 
        
# Drives to the rift valley cube
def goToCube():
    print "goToCube"
    moveFrontClaw(c.frontClawOpen, 15)
    moveFrontArm(c.frontArmDown, 15)
    driveTimed(100,100,500)
    if isPrime:
        drive(100, 100)
    else:
        drive(90, 100)
    while not onBlack():
        pass
    drive(0, 0)
    moveFrontClaw(c.frontClawMid, 15)
    moveFrontArm(c.frontArmUp, 15)
    msleep(500)

# Turns to drop cube off on our side of the board
def dropOffCube():
    print"dropOffCube"
    driveTimed(100, 0, 1900)
    moveFrontArm(c.frontArmMid, 15)
    moveFrontClaw(c.frontClawOpen, 15)
    msleep(500)
    moveFrontArm(c.frontArmUp, 15)

# Go to Red Poms
def getRedPoms():
    print "getRedPoms"
    if isPrime:
        driveTimed(-100,0, 600)
    else:
        driveTimed(-100,0, 750)
    moveFrontClaw(c.clawOpen, 25)
    moveFrontArm(c.armDown, 25)
    driveTimed(80, 80, 700)
    moveFrontClaw(c.clawClose, 15) 
    moveFrontArm(c.armUp, 15)
    
# Exit Valley  
def leaveValley():
    print "leaveValley"
    driveTimed(-80, -80, 550)#1100, 650
    driveTimed(-70,0,1550)
    
# Score Poms   
def depositRedPoms():
    print"depositRedPoms"
    driveTimed(-100, -100, 1400)#1350
    driveTimed(-80, 80,500)
    msleep(500)
    drive(-30, 30)
    crossBlack()
    driveTimed(40, -40, 100)
    driveTimed(100, 80, 850)
    moveFrontArm(c.armDown, 15)
    moveFrontClaw(c.clawOpen, 15)

# Get to Valley    
def goToValley():
    print "goToValley"
    moveFrontArm(c.armUp, 15)
    moveFrontClaw(c.clawClose, 15)
    driveTimed (-50,-50,230)
    driveTimed (100,-70,700)
    driveTimed (100,0,1000)
    drive (40,0)
    crossBlack()
    timedLineFollowRightSmooth(1.55)
    driveTimed (80,80,800)#1600
    drive(70, 70)
    crossBlack()
    
# drives to and grabs gold poms
def getGoldPoms():
    print"getGoldPoms"
    #driveTimed(-100, 0, 1500)#was 2400
    driveTimed(-50,50,800)
    moveFrontClaw(c.clawOpen, 15)
    moveFrontArm(c.armDown, 15)
    driveTimed(60, 60, 550)#was 550
    moveFrontClaw(c.clawClose, 15)
    msleep(500)
    moveFrontArm(c.armUp, 15)
    
# moves gold poms to habitat 
def getOutOfValley():
    print "getOutOfValley"
    driveTimed(-60,-60,900)
    driveTimed (50,-50,900)
    driveTimed(-80, -80, 250)
    #driveTimed(0, -80, 1100)

def depositGoldPoms():
    print"depositGoldPoms"
    driveTimed(-100, -100, 1350)
    driveTimed(-80, 80,1000)
    msleep(500)
    drive(-30, 30)
    crossBlack()
    driveTimed(100, 80, 650)
    moveFrontArm(c.armMid, 15)
    moveFrontClaw(c.clawOpen, 15)
    
# Go back to valley
def returnToValley():
    print "returnToValley"
    moveFrontArm(c.armUp, 15)
    moveFrontClaw(c.clawClose, 15)
    driveTimed (-50,-50,230)
    driveTimed (100,-70,500)
    drive (40,0)
    crossBlack()
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

    