#16-ValleyBot actionpy
'''
Created on Mar 13, 2016

@author: Dead Robot Society
'''
import constants as c

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
from servos import moveArm
from servos import moveClaw
from servos import moveCube

from sensors import waitForButton
from sensors import onBlack
from sensors import crossBlack


# Tests all hardware
def init():
    print "init"
    c.setVars()
    testServos()
    testMotors()
    disable_servos()
    waitForButton()
    enable_servos()
    moveClaw(c.clawClosed, 25)
    moveArm(c.armUp, 25) 

# Raises cube holder
# Backs out of start box and turns 
# Moves backward until black tape
def getOutOfStartBox():
    print "getOutOfStartBox"
    moveCube(c.cubeUp, 25)
    msleep(500)
    driveTimed(-100, -100, 1600)
    driveTimed(0, 100, 400)
    driveTimed(70,70,600)

# Follows line for 3.5 seconds
# Moves forward until robot reaches debris
def goToDebris():
    print "goToDebris"
    if c.isPrime:
        timedLineFollowLeft(3.0) #3.5
        timedLineFollowLeftSmooth(0.75)
        driveTimed(50, 50, 1000)
    else:
        timedLineFollowLeft(4)
        driveTimed(50, 53, 1000)


# Moves claw arm down and drives backwards with debris
def removeDebris():
    print "removeDebris"
    moveArm(c.armDown, 15)
    msleep(500)
    driveTimed(-80, -80, 500)

# Dumps debris next to compost
def dumpDebris():
    print "removeDebris"
    driveTimed(0,-100,1000)
    driveTimed(60,70,500)
    driveTimed(90,0,500)
    driveTimed(60,90,225)
    driveTimed(60,70,650)
    
# Drives backwards and follows line to reach gate
def goToGate():
    print "goToGate"
    moveArm(c.armUp, 15)
    driveTimed(-100,-100, 1250)
    timedLineFollowRight(1.3)
    timedLineFollowRightSmooth(3.0) #was 3.3
    
# Drives to the rift valley cube
def goToCube():
    print "goToCube"
    moveClaw(c.clawOpen, 15)
    moveArm(c.armDown, 15)
    drive(100, 100)
    while not onBlack():
        pass
    drive(0, 0)
    moveClaw(c.clawMid, 15)
    moveArm(c.armUp, 15)
    msleep(500)

# Turns to drop cube off on our side of the board
def dropOffCube():
    print"dropOffCube"
    driveTimed(100, 0, 1900)
    moveArm(c.armMid, 15)
    moveClaw(c.clawOpen, 15)
    msleep(500)
    moveArm(c.armUp, 15)

# drives to and grabs gold poms
def getGoldPoms():
    print"getGoldPoms"
    driveTimed(-100, 0, 1500)#was 2400
    driveTimed(-50,50,1200)
    moveArm(c.armDown, 15)
    driveTimed(60, 60, 550)#was 550
    moveClaw(c.clawClosed, 15)
    msleep(500)
    moveArm(c.armUp, 15)
    
# moves gold poms to habitat 
def getOutOfValley():
    print "getOutOfValley"
    driveTimed(-60,-60,900)
    driveTimed (50,-50,1000)
    driveTimed(-80, -80, 250)
    #driveTimed(0, -80, 1100)

def depositGoldPoms():
    print"depositGoldPoms"
    driveTimed(-100, -100, 1350)
    driveTimed(-80, 80,500)
    msleep(500)
    drive(-30, 30)
    crossBlack()
    driveTimed(100, 80, 650)
    moveArm(c.armDown, 15)
    moveClaw(c.clawOpen, 15)
    
# Go back to valley
def goToValley():
    print "returnToValley"
    moveArm(c.armUp, 15)
    moveClaw(c.clawClosed, 15)
    driveTimed (-50,-50,230)
    driveTimed (100,-70,500)
    drive (40,0)
    crossBlack()
    timedLineFollowRightSmooth(1.55)
    driveTimed(60, 0, 250)
    driveTimed (80,80,1200)
    
# Go to Red Poms
def getRedPoms():
    print "getRedPoms"
    drive(60, 60)
    while not onBlack():
        pass
    drive(0, 0)
    driveTimed(70,0,1150)
    moveClaw(c.clawOpen, 25)
    moveArm(c.armDown, 25)
    driveTimed(80, 80, 700)
    moveClaw(c.clawClosed, 15) 
    msleep(300)
    moveClaw(c.clawOpen,15)
    driveTimed(50,50,400)
    moveClaw(c.clawClosed, 15)
    moveArm(c.armUp, 15)
  
# Exit Valley  
def leaveValley():
    print "leaveValley"
    driveTimed(-80, -80, 1100)
    driveTimed(-70,0,1550)
    
def depositRedPoms():
    print"depositRedPoms"
    driveTimed(-100, -100, 1350)
    driveTimed(-80, 80,500)
    msleep(500)
    drive(-30, 30)
    crossBlack()
    driveTimed(100, 80, 750)
    moveArm(c.armMid, 15)
    moveClaw(c.clawOpen, 15)
    
# Stops the program for testing
def DEBUG():
    ao()
    print"Stopped for debug"
    exit(0)
    