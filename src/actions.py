# 16-ValleyBot actionpy
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
 
from drive import testMotors, stop
from drive import driveTimed
from drive import drive
from drive import timedLineFollowLeftButton
from drive import timedLineFollowRight
from drive import timedLineFollowRightSmooth
from drive import timedLineFollowLeftSmooth
from drive import timedLineFollowLeftSmoothButton
from drive import lineFollowRightSmoothCount
from drive import timedLineFollowLeftBack
from drive import lineFollowUntilEndLeftFront 
from drive import lineFollowUntilEndRightFront

from servos import testServos
from servos import moveFrontArm
from servos import moveFrontClaw
from servos import moveBackClaw
from servos import moveBackArm

from sensors import onBlackBack , waitForButton
from sensors import crossBlackFront
from sensors import onBlackFront
from sensors import wait4light
from sensors import testSensors
from sensors import waitTouch
from sensors import DEBUG
from sensors import DEBUGwithWait
from constants import backArmUp

# Tests all hardware
def init():
    if c.isPrime:
        print "Running Valley - Prime"
    else:
        print "Running Valley - Clone"   
    testSensors()
#     testServos()
#     testMotors()
#     disable_servos()
    # wait4light()
    
    moveFrontClaw(c.frontClawClose, 25)
    moveFrontArm(c.frontArmUp, 5) 
    moveBackClaw(c.backClawSmallSolar, 25)
    moveBackArm(c.backArmDown, 5)
#     msleep(1000)
#     disable_servos()
    waitForButton()
    c.startTime = seconds()
    enable_servos()
    moveBackArm(c.backArmUp, 5)
    waitForButton()
    shut_down_in(179.9) #119.9 DONT FORGET TO FIX 
    # moveBackClaw(c.backClawSmallSolar, 15)
    
def grabSolarArraysInBox():
    moveBackArm(c.backArmPushSolar, 5)
    msleep(200)
    moveBackClaw(c.backClawSmallSolar, 15)
    msleep(200)
    driveTimed(-50, -50, 1000)
    moveBackArm(c.backArmDown, 15)
    msleep(200)
    moveBackClaw(c.backClawClose, 15)
    msleep(200)
    moveBackArm(c.backArmUp, 15)
    msleep(200)
    
# Backs out of start box and turns 
# Moves backward until black tape
def getOutOfStartBox():
    print "getOutOfStartBox"
    driveTimed(-75, -100, 2000)
    driveTimed(-100, 100, 400)
    driveTimed(70, 70, 600)

# Follows line for 3.5 seconds
# Moves forward until robot reaches debris
def goToComposter():
    print "goToComposter"
    driveTimed(-100, 100, 200)
    if c.isClone:
        drive(100, 85)
    else:
        drive(100, 75)
    msleep(300)
    while not onBlackFront():
        pass
    print "Sees line"
    timedLineFollowLeftButton(1.7)
    timedLineFollowLeftSmoothButton(3)
    driveTimed(0, -100, 950)
    driveTimed(60, 60, 1900)
    moveFrontClaw(c.frontClawClose, 20)
    moveFrontArm(c.frontArmSwing, 20)
    msleep(300)
    driveTimed(35, 0, 3550)

# Moves claw arm down and drives backwards with debris
def removeDebris():
    print "removeDebris"
    driveTimed(-75, 0, 750)
    moveFrontArm(c.frontArmUp, 20)
    drive(-95, -75)
    while not onBlackBack():
        pass
    drive(-100, 0)
    crossBlackFront()
    timedLineFollowLeftSmooth(4.5)
    moveFrontArm(c.frontArmDown, 15)
    msleep(500)
    
# Dumps debris next to compost
def dumpDebris():
    print "removeDebris"
    driveTimed(-100, -100, 100)
    driveTimed(0, -100, 1100)
    driveTimed(60, 70, 500)
    driveTimed(90, 0, 600)
    driveTimed(60, 90, 225)
    driveTimed(60, 70, 800)
   
# Drives backwards and follows line to reach gate
def goToGate():
    print "goToGate"
    moveFrontArm(c.frontArmUp, 20)
    drive(-95, -75)
    while not onBlackBack():
        pass
    drive(-100, 0)
    while not onBlackFront():
        pass
    timedLineFollowRight(1.5)
    drive(0, 20)
    while not onBlackFront():
        pass
    stop()
    moveFrontArm(c.frontArmGrabBot, 15)
    moveFrontClaw(c.frontClawOpen, 15)
    msleep(200)
    drive(0, 50)
    while not onBlackFront():
        pass
    lineFollowUntilEndRightFront()
    moveFrontArm(c.frontArmDown, 15)
    
# Drives to the rift valley cube
def goToCube():
    print "goToCube"
    driveTimed(100, 100, 500)
    moveFrontClaw(c.frontClawCube, 5)
    msleep(200)
    moveFrontArm(c.frontArmSwitch, 30)
    driveTimed(-100, -100, 1400)

# Drops off cube on start box line
def dropOff():
    print "drop off"
    driveTimed(-80, 80, 1200)
    moveFrontArm(c.frontArmDown, 10)
    msleep(300)
    moveFrontClaw(c.frontClawOpen, 10)
    msleep(300)
    moveFrontArm(c.frontArmUp, 10)
    msleep(300)
    drive(80, -80)
    crossBlackFront()

# Goes into rift valley to grab BotGuy
def goToValley():
    print "goToValley"
    timedLineFollowRight(.5)
    lineFollowUntilEndRightFront()
    driveTimed(100, 90, 500)
    drive(50, 50)
    crossBlackFront()
    moveFrontClaw(c.frontClawClose, 200)
    moveFrontArm(c.frontArmSwing, 200)
    msleep(300)
    
# grabs BotGuy    
def goToBotGuy():
    print "goToBotGuy"
    drive(-50, 50)
    crossBlackFront()
    driveTimed(-50, 50, 150)
    drive(50, 0)
    crossBlackFront()
    moveFrontArm(c.frontArmUp, 10)
    moveFrontClaw(c.frontClawOpen, 10)
    msleep(300)
    timedLineFollowRight(2.2)
    driveTimed(-50, 50, 100)
    moveFrontArm(c.frontArmGrabBot, 5)
    msleep(300)
    moveFrontClaw(c.frontClawClose, 100)
    msleep(300)
    moveFrontArm(c.frontArmUp, 10)
    msleep(1000)

# Leaves rift valley
# drives up ramp
def goToRamp():
    print "goToRamp"
    driveTimed(-100, -100, 2200)
    driveTimed(0, 100, 650)
    driveTimed(100, 100, 500)
    drive(0, 50)
    while not onBlackFront():
        pass
    timedLineFollowRight(2.2)
    stop()
    timedLineFollowRightSmooth(1)
#     driveTimed(60, 60, 1400)
    driveTimed(100, 0, 1300)
    
    driveTimed(100, 100, 300)
    
    
# drives up ramp
def goUpRamp():
    print "goUpRamp"
    moveFrontArm(c.frontArmUp, 10)  # was frontArmUpRamp
    msleep(300)
    driveTimed(100, 80, 1000)
    driveTimed(100, 100, 800)
    moveFrontArm(c.frontArmUpRamp, 10)
    driveTimed(100, 80, 3000)
    drive(100, 95)
    while not waitTouch():
        pass
    stop()
    moveFrontArm(c.frontArmUp, 10)
    msleep(1000)
    

    
def cleanSolarPanels():
    drive(-50, 50)
    while not onBlackFront():
        pass
    stop()
    timedLineFollowRightSmooth(12)
    driveTimed(-50, -50, 500)
    driveTimed(-60,0,6000)
    
    '''
    driveTimed(-50, 50, 1200)
    DEBUGwithWait()
    driveTimed(35, 30, 8000)
    '''
        
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


def dumpSolarArrays():  
    moveBackArm(c.backArmDown, 20)
    msleep(300)
    moveBackClaw(c.backClawOpen, 20) 
    msleep(300)
    moveBackArm(c.backArmUp, 5)
    msleep(300)
    
    
