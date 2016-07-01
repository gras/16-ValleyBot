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
from wallaby import clear_motor_position_counter
from wallaby import get_motor_position_counter
 
from drive import testMotors, stop
from drive import driveTimed
from drive import drive
from drive import timedLineFollowLeftButton
from drive import timedLineFollowRight
from drive import timedLineFollowRightSmooth
from drive import timedLineFollowLeftSmoothButton
from drive import lineFollowUntilEndRightFront
from drive import timedLineFollowRightSmoothET
from drive import freezeMotors

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
# from constants import isPrime

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
    # wait4light() not here
    
    moveFrontClaw(c.frontClawClose, 25)
    moveFrontArm(c.frontArmUp, 5) 
    moveBackClaw(c.backClawSmallSolar, 25)
    moveBackArm(c.backArmDown, 5)
    print "press the touch sensor"
    while not waitTouch():
        pass
    enable_servos()
    moveBackArm(c.backArmUp, 5) 
    moveBackClaw(c.backClawStart, 5)
    msleep(200)
    print "button"
    waitForButton()
    c.startTime = seconds()
    shut_down_in(119.9)  # 119.9 DONT FORGET TO FIX 
    
def grabSolarArraysInBox():
    moveBackClaw(c.backClawSmallSolar, 20)
    moveBackArm(c.backArmPushSolar, 5)
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
    if c.isPrime:
        driveTimed(-75, -100, 1300)
    else:
        driveTimed(-75, -100, 1700)
    driveTimed(-100, 100, 400)
    driveTimed(70, 70, 600)

# Follows line for 3.5 seconds
# Moves forward until robot reaches debris
def goToComposter():
    print "goToComposter"
    driveTimed(-100, 100, 100)
    if c.isPrime:
        drive(100, 75)
    else:
        drive(100, 85)
    msleep(200)
    while not onBlackFront(1):
        pass
    drive(-50, 0)
    while onBlackFront(1):
        pass
    timedLineFollowLeftButton(3)
    driveTimed(30, 60, 300)
    if c.isPrime:
        driveTimed(0, -100, 1000)  # was 950
    else:
        driveTimed(0, -100, 950)
    freezeMotors()
    moveFrontClaw(c.frontClawClose, 20)
    moveFrontArm(c.frontArmSwing, 20)
    if c.isPrime:
        driveTimed(60, 60, 1900)
    else:
        driveTimed(60, 60, 1900)
    if c.isPrime:
        driveTimed(35, 5, 3400)
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
    driveTimed(30, 60, 150)
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
    moveFrontArm(c.frontArmGrabBot, 45)  # was 15
    moveFrontClaw(c.frontClawOpen, 45)  # was 15
    
    if onBlackFront():
        drive(20, 0)
        while onBlackFront():
            pass
        stop()
    
    drive(0, 20)
    while not onBlackFront():
        pass
    stop()
    
    lineFollowUntilEndRightFront()
    moveFrontArm(c.frontArmMidDown, 30)  # was 15
    
# Drives to the rift valley cube
def goToCube():
    print "goToCube"
    driveTimed(100, 100, 250)
    moveFrontArm(c.frontArmGrabCube, 15)
    driveTimed(100, 100, 200)
    moveFrontClaw(c.frontClawCube, 30)  # was 45
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
    freezeMotors()
    
# Goes into rift valley to grab BotGuy
def goToValley():
    print "goToValley"

    if onBlackFront():
        drive(20, 0)
        while onBlackFront():
            pass
        stop()
    
    drive(0, 20)
    while not onBlackFront():
        pass
    stop()

    lineFollowUntilEndRightFront()
    driveTimed(100, 100, 500) 
    drive(50, 50)
    crossBlackFront()
    driveTimed(50, 50, 250)
    moveFrontClaw(c.frontClawClose, 200)
    moveFrontArm(c.frontArmSweep, 20)
#     msleep(300)
    
# grabs BotGuy    
def goToBotGuy():
    print "goToBotGuy"
    drive(-50, 50)  # sweep red poms
    crossBlackFront()
    driveTimed(-50, 50, 150)  # end of sweep
    moveFrontArm(c.frontArmUp, 100)
    drive(50, 0)
    crossBlackFront()
    moveFrontClaw(c.frontClawOpen, 100)
    msleep(300)
    clear_motor_position_counter(c.RMOTOR)
    if c.isPrime:
        timedLineFollowRight(1)  # was 1.5
        timedLineFollowRightSmoothET(6)  # was 1.6  
    else:
        timedLineFollowRight(1)
        timedLineFollowRightSmoothET(5)
    driveTimed(-50, 50, 75)
    moveFrontArm(c.frontArmGrabBot, 10)
    msleep(300)
    moveFrontClaw(c.frontClawClose, 200) 
    msleep(300)
    moveFrontArm(c.frontArmUp, 10)
    msleep(500)
    print get_motor_position_counter(c.RMOTOR)
#     msleep(1000)

# Leaves rift valley
# drives up ramp
def goToRamp():
    print "goToRamp"
    
    backToCounterRightMotor()
    print get_motor_position_counter(c.RMOTOR)
#     driveTimed(-100, -100, 2100)#**************Change this 1800
#     driveTimed(-100, -100, 500)
#     freezeMotors()    
    if c.isPrime:
        driveTimed(0, 100, 750)  # was 650
    else:
        driveTimed(0, 100, 750)
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
    while not onBlackFront(2):
        pass
    msleep(50)
    while onBlackFront(2):
        pass
    msleep(50)
    while not onBlackFront(2):
        pass
    msleep(50)
    drive(0, -30)
    while onBlackFront(2):
        pass 
    if c.isPrime:
        driveTimed(100, 99, 3000)
    else:
        driveTimed(100, 95, 3000)
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
    msleep(500)
    
def moveSolarPanels():
    print "moveSolarPanels"
    drive(-50, 50)
    while not onBlackFront():
        pass
    stop()
    # if c.isPrime:
    #    timedLineFollowRightSmooth(10.5)
    # else:
    if c.isPrime:
        timedLineFollowRightSmooth(12.5)
    else:
        timedLineFollowRightSmooth(11.9)
    
def deliverBotnaut():
    print "deliverBotnaut"
    driveTimed(-50, -50, 500)
    if c.isPrime:
        driveTimed(-60, -20, 3500)
        driveTimed(0, 60, 2300)  # was 2500
    else:
        driveTimed(-60, -10, 2800)
        driveTimed(0, 60, 2500)  # was 2600
    drive(50, 50)
    while not waitTouch():
        pass
    freezeMotors()
    if c.isPrime:
        driveTimed(-50, -50, 2200)  # was 1000
    else:
        driveTimed(-50, -50, 1200)
    moveFrontArm(c.frontArmGrabBot, 10)
    moveFrontClaw(c.frontClawOpen, 20)
#     driveTimed(100, 100, 100)
    moveFrontArm(c.frontArmUp, 10)
    # driveTimed(50, 50, 1000)

def removeDirt():
    print "removeDirt"
    if c.isPrime:
        driveTimed(-30, 30, 150)  # 33
    else:
        pass
    moveBackArm(c.backArmSweep, 20)
    if c.isPrime:
        driveTimed(-33, -30, 1200)  # 33
    else:
        driveTimed(-33, -30, 1200)
    driveTimed(30, -30, 1000)
    moveBackClaw(c.backClawSqueeze, 30)
    
def deliverSolarArrays():
    print "deliverSolarArrays"
    driveTimed(-60, 0, 3000)
    drive(0, 60)
    while not onBlackBack():
        pass
    driveTimed(-50, -50, 500)
    moveBackArm(c.backArmDown, 20)
    moveBackClaw(c.backClawDropSolar, 20)
    moveBackArm(c.backArmPushSolar, 10)
    driveTimed(40, -40, 100)
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
    
def backToCounterRightMotor():
#     count = get_motor_position_counter(c.RMOTOR)
#     clear_motor_position_counter(c.RMOTOR)
    drive(-100, -100)
    while get_motor_position_counter(c.RMOTOR) >= -1200:
        pass
    freezeMotors()
