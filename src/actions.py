# 16-ValleyBot actionpy
'''
Created on Mar 13, 2016

@author: Dead Robot Society
'''
import constants as c

from wallaby import seconds
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
from drive import timedLineFollowLeftSmoothButton
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
from constants import isPrime

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
    # wait4light()
    
    moveFrontClaw(c.frontClawClose, 25)
    moveFrontArm(c.frontArmUp, 5) 
    moveBackClaw(c.backClawSmallSolar, 25)
    moveBackArm(c.backArmDown, 5)
    print "press the touch sensor"
    while not waitTouch():
        pass
    enable_servos()
    moveBackArm(c.backArmUp, 5) 
    msleep(200)
    print "button"
    waitForButton()
    c.startTime = seconds()
    shut_down_in(179.9)  # 119.9 DONT FORGET TO FIX 
    
def grabSolarArraysInBox():
    moveBackArm(c.backArmPushSolar, 5)
    moveBackClaw(c.backClawSmallSolar, 15)
    if c.isPrime:
        driveTimed(-50, -50, 1000)
    else:
        driveTimed(-45, -50, 1000)
    moveBackArm(c.backArmDown, 15)
    moveBackClaw(c.backClawClose, 15)
    moveBackArm(c.backArmUp, 15)
    
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
    if c.isPrime:
        drive(100, 75)
    else:
        drive(100, 85)
    msleep(200)
    while not onBlackFront():
        pass
    print "Sees line"
    timedLineFollowLeftButton(3)
    driveTimed(50, 50, 200)
    driveTimed(0, -100, 950)
    if c.isPrime:
        driveTimed(60, 60, 1800)
    else:
        driveTimed(60, 60, 1900)
    moveFrontClaw(c.frontClawClose, 20)
    moveFrontArm(c.frontArmSwing, 20)
    if c.isPrime:
        driveTimed(35, 5, 3600)
    else:
        driveTimed(35, 5, 3550)

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
    timedLineFollowLeftButton(2) 
    moveFrontArm(c.frontArmDown, 15)
    
# Dumps debris next to compost
def dumpDebris():
    print "removeDebris"
    driveTimed(-100, -100, 100)
    driveTimed(0, -100, 1100)
    driveTimed(60, 70, 500)
    driveTimed(90, 0, 600)
    driveTimed(50, 100, 225)
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
    drive(0, 50)
    while not onBlackFront():
        pass
    drive(20, 0)
    while onBlackFront(): # make sure not middle of line
        pass
    lineFollowUntilEndRightFront()
    moveFrontArm(c.frontArmMidDown, 15)
    
# Drives to the rift valley cube
def goToCube():
    print "goToCube"
    driveTimed(100, 100, 250)
    moveFrontArm(c.frontArmGrabCube, 15)
    driveTimed(100, 100, 200)
    moveFrontClaw(c.frontClawCube, 45)
#     msleep(200)
    moveFrontArm(c.frontArmSwitch, 30)
    driveTimed(-100, -100, 1400)

# Drops off cube on start box line
def dropOff():
    print "drop off"
    driveTimed(-80, 80, 1250) 
    moveFrontArm(c.frontArmDown, 10)
    moveFrontClaw(c.frontClawOpen, 10)
    driveTimed(-50, 50, 50)
    moveFrontArm(c.frontArmUp, 10)
    drive(80, -80)
    crossBlackFront()
    stop()
    
# Goes into rift valley to grab BotGuy
def goToValley():
    print "goToValley"
    drive(0, 50)
    while not onBlackFront():
        pass
    lineFollowUntilEndRightFront()
    driveTimed(100, 100, 500) 
    drive(50, 50)
    crossBlackFront()
    driveTimed(50, 50, 250)
    moveFrontClaw(c.frontClawClose, 200)
    moveFrontArm(c.frontArmMidDown, 20)
#     msleep(300)
    
# grabs BotGuy    
def goToBotGuy():
    print "goToBotGuy"
    drive(-50, 50)#sweep red poms
    crossBlackFront()
    driveTimed(-50, 50, 150)#end of sweep
    moveFrontArm(c.frontArmUp, 100)
    drive(50, 0)
    crossBlackFront()
    moveFrontClaw(c.frontClawOpen, 100)
    msleep(300)
    if c.isPrime:
        timedLineFollowRight(1.5)#was 1.5
        timedLineFollowRightSmooth(.75)#was 1.6  
    else:
        timedLineFollowRight(2.3)
    driveTimed(-50, 50, 75)
    moveFrontArm(c.frontArmGrabBot, 10)
    msleep(300)
    moveFrontClaw(c.frontClawClose, 200) 
    msleep(300)
    moveFrontArm(c.frontArmUp, 10)
#     msleep(1000)

# Leaves rift valley
# drives up ramp
def goToRamp():
    print "goToRamp"
    driveTimed(-100, -100, 2100)#**************Change this 1800
    driveTimed(0, 100, 650)#was 650
    driveTimed(100, 100, 500)
    drive(0, 50) 
    while not onBlackFront():
        pass
    drive(0, 50)
    while onBlackFront():
        pass
    timedLineFollowLeftButton(10)
    
# turn to go up the ramp
    drive(0, -80)
    while not onBlackFront():
        pass
    msleep(50)
    while onBlackFront():
        pass
    msleep(50)
    while not onBlackFront():
        pass
    msleep(50)
    drive(0, -30)
    while onBlackFront():
        pass 
    driveTimed(100, 100, 3000)
    driveTimed(0, 30, 200)
    
# drives up ramp
def goUpRamp():
    print "goUpRamp"
    moveFrontArm(c.frontArmUp, 10)
    drive(100, 80)
    moveFrontArm(c.frontArmUpRamp, 10)
    drive(100, 100)
    msleep(800)
    drive(100, 80)
    msleep(3000)
    drive(100, 95)
    while not waitTouch():
        pass
    stop()
    moveFrontArm(c.frontArmUp, 20)
    
def moveSolarPanels():
    print "moveSolarPanels"
    drive(-50, 50)
    while not onBlackFront():
        pass
    stop()
   # if isPrime:
    #    timedLineFollowRightSmooth(10.5)
    #else:
    timedLineFollowRightSmooth(11.5)
def deliverBotnaut():
    print "deliverBotnaut"
    driveTimed(-50, -50, 500)
    if c.isPrime:
        driveTimed(-60, 0, 3500)
        driveTimed(0, 60, 2300)#was 2500
    else:
        driveTimed(-60, 0, 2700)
        driveTimed(0, 60, 3000)
    if isPrime:
        driveTimed(-50, -50, 2000)#was 1000
    else:
        driveTimed(-50, -50, 1200)
    moveFrontArm(c.frontArmGrabBot, 10)
    moveFrontClaw(c.frontClawOpen, 20)
    driveTimed(100, 100, 100)
    moveFrontArm(c.frontArmUp, 10)
    #driveTimed(50, 50, 1000)
    DEBUGwithWait()
    
def deliverSolarArrays():
    print "deliverSolarArrays"
    driveTimed(-60, 0, 3000)
    drive(0, 60)
    while not onBlackBack():
        pass
    driveTimed(-50, -50, 500)
    moveBackArm(c.backArmDown, 20)
    moveBackClaw(c.backClawDropSolar, 20)
    moveBackArm(c.backArmPushSolar,10)
    driveTimed(40,-40,100)
    driveTimed(50, 50, 500)
    moveBackArm(c.backArmUp, 20)
#     msleep(200)
    drive(0, 60)
    while onBlackBack():
        pass
    stop()
#     msleep(200)
    moveFrontClaw(c.frontClawClose, 50)
    moveFrontArm(c.frontArmMidPom, 15)
    driveTimed(100, -100, 200)






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
    
