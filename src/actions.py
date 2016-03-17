#16-ValleyBot actionpy
'''
Created on Mar 13, 2016

@author: Dead Robot Society
'''

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

from servos import testServos
from servos import moveArm
from servos import moveClaw
from servos import moveCube

from constants import clawClosed
from constants import armUp
from constants import cubeUp
from constants import armDown
from constants import clawOpen
from constants import clawMid
from constants import armMid

from sensors import waitForButton
from sensors import onBlack
from sensors import crossBlack




# Tests all hardware
def init():
    print "init"
    testServos()
    testMotors()
    disable_servos()
    waitForButton()
    enable_servos()
    moveClaw(clawClosed, 25)
    moveArm(armUp, 25) 

# Raises cube holder
# Backs out of start box and turns 
# Moves backward until black tape
def getOutOfStartBox():
    print "getOutOfStartBox"
    moveCube(cubeUp, 25)
    msleep(500)
    driveTimed(-100, -100, 1600)
    driveTimed(0, 100, 400)
    driveTimed(70,70,600)

# Follows line for 3.5 seconds
# Moves forward until robot reaches debris
def goToDebris():
    print "goToDebris"
    timedLineFollowLeft(3.5); 
    driveTimed(50, 50, 1000);

# Moves claw arm down and drives backwards with debris
def removeDebris():
    print "removeDebris"
    moveArm(armDown, 15); 
    msleep(500);
    driveTimed(-80, -80, 500);

# Dumps debris next to compost
def dumpDebris():
    print "removeDebris"
    driveTimed(0,-100,1000);
    driveTimed(60,70,500);
    driveTimed(90,0,500);
    driveTimed(60,90,225); 
    driveTimed(60,70,650);
    
# Drives backwards and follows line to reach gate
def goToGate():
    print "goToGate"
    moveArm(armUp, 15);
    driveTimed(-100,-100, 1250);
    timedLineFollowRight(1.3);
    timedLineFollowRightSmooth(3.3);
    
# Drives to the rift valley cube
def goToCube():
    print "goToCube"
    moveClaw(clawOpen, 15)
    moveArm(armDown, 15)
    drive(100, 100)
    while not onBlack():
        pass
    drive(0, 0)
    moveClaw(clawMid, 15)
    moveArm(armUp, 15)
    msleep(1000)

# Turns to drop cube off on our side of the board
def dropOffCube():
    print"dropOffCube"
    driveTimed(100, 0, 1900)
    moveArm(armMid, 15)
    moveClaw(clawOpen, 15)
    msleep(500)
    moveArm(armUp, 15)

# drives to and grabs gold poms
def getGoldPoms():
    print"getGoldPoms"
    driveTimed(-100, 0, 2400)
    moveArm(armDown, 15)
    driveTimed(80, 80, 600)
    moveClaw(clawClosed, 15)
    moveArm(armUp, 15)
    
# moves gold poms to habitat 
def depositGoldPoms():
    print"depositGoldPoms"
    driveTimed(-80, -80, 250)
    driveTimed(0, -80, 1100)
    driveTimed(-100, -100, 1500)
    drive(-80, 80)
    msleep(500)
    ao()
    msleep(500)
    drive(-30, 30)
    crossBlack()
    driveTimed(100, 80, 300)
    moveArm(armDown, 15)
    moveClaw(clawOpen, 15)
    
# Go back to valley
def goToValley():
    moveArm(armUp, 15)
    moveClaw(clawClosed, 15)
    
# Stops the program for testing
def DEBUG():
    ao()
    print"Stopped for debug"
    exit(0)
    