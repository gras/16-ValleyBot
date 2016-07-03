# 16-ValleyBot actionpy
'''
Created on Mar 13, 2016

@author: Dead Robot Society
'''
import constants as c

from wallaby import seconds
from wallaby import disable_servos
from wallaby import disable_servo
from wallaby import enable_servo
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
#from drive import timedLineFollowLeftSmoothButton
from drive import lineFollowUntilEndRightFront
from drive import timedLineFollowRightSmoothET
from drive import freezeMotors
from drive import backToCounterRightMotor

from servos import testServos
from servos import moveFrontArm
from servos import moveFrontClaw
from servos import moveBackClaw
from servos import moveBackArm

from sensors import onBlackBack , waitForButton, wait4Ramp, wait4RampLine
from sensors import crossBlackFront
from sensors import onBlackFront
from sensors import wait4light
from sensors import testSensors
from sensors import waitTouch
from sensors import DEBUG
from sensors import DEBUGwithWait
from sensors import wait4WhiteFront
from sensors import wait4BlackFront
from sensors import seeRamp
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
    #print "button"
    #waitForButton()
    wait4light()
    c.startTime = seconds()
    shut_down_in(119.9)  
    
def grabSolarArrays():
    print "grabSolarArrays"
    moveBackClaw(c.backClawSmallSolar, 200)
    moveBackArm(c.backArmPushSolar, 5)
    if c.isPrime:
        driveTimed(-50, -50, 1000)
    else:
        driveTimed(-50, -55, 1000)
    moveBackArm(c.backArmDown, 20)#15
    moveBackClaw(c.backClawClose, 20)#15
    moveBackArm(c.backArmUp, 20)#15
    
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
    drive(100, 75)
    msleep(200)
    while not onBlackFront(1):
        pass
    drive(-50, 0)
    while onBlackFront(1):
        pass
    if c.isPrime:
        timedLineFollowLeftButton(3)
    else:
        timedLineFollowLeftButton(5)
    driveTimed(30, 60, 300)
    driveTimed(0, -100, 1000)
    freezeMotors()
    moveFrontClaw(c.frontClawClose, 50)#20
    moveFrontArm(c.frontArmSwing, 30)#20
    driveTimed(60, 60, 1900)
    driveTimed(35, 5, 2000)#2400
    driveTimed(21, 3, 2000)#1500    
            
# Moves claw arm down and drives backwards with debris
def removeDebris():
    print "removeDebris"
    driveTimed(-20, 0, 400)
    driveTimed(-75, 0, 750)
    moveFrontArm(c.frontArmUp, 20)
    drive(-95, -75)
    while not onBlackBack():
        pass
    drive(-100, 0)
    crossBlackFront()
    timedLineFollowLeftButton(2) 
    driveTimed(30, 60, 150)
    moveFrontArm(c.frontArmDown, 20)#15
    
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
    moveFrontArm(c.frontArmUp, 30)#20
    drive(-95, -75)
    while not onBlackBack():
        pass
    drive(-100, 0)
    while not onBlackFront():
        pass
    timedLineFollowRight(1.5)
    moveFrontArm(c.frontArmGrabBot, 45)
    moveFrontClaw(c.frontClawOpen, 45)
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
    moveFrontArm(c.frontArmMidDown, 30)
    
# Drives to the rift valley cube
def goToCube():
    print "goToCube"
    driveTimed(100, 100, 250)
    moveFrontArm(c.frontArmGrabCube, 30)#15
    driveTimed(100, 100, 200)
    moveFrontClaw(c.frontClawCube, 30)
    moveFrontArm(c.frontArmSwitch, 30)
    driveTimed(-100, -100, 1400)
    
# Drops off cube on start box line
def dropOff():
    print "drop off"
    driveTimed(-80, 80, 1250) 
    moveFrontArm(c.frontArmDown, 20)#10
    moveFrontClaw(c.frontClawOpen, 15)#10
    driveTimed(-50, 50, 50)
    moveFrontArm(c.frontArmUp, 10)
    drive(35, -50)#50, -50
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
    moveFrontArm(c.frontArmSweep, 25)#20

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
    #msleep(300)#
    clear_motor_position_counter(c.RMOTOR)
    if c.isPrime:
        timedLineFollowRight(1)  # was 1.5
        timedLineFollowRightSmoothET(6)  # was 1.6  
    else:
        timedLineFollowRight(1)
        timedLineFollowRightSmoothET(5)
    driveTimed(-50, 50, 75)
    moveFrontArm(c.frontArmGrabBot, 20)#10
    msleep(150)#300
    moveFrontClaw(c.frontClawClose, 200) 
    msleep(150)#300
    moveFrontArm(c.frontArmUp, 10)#
    msleep(250)#500
    print get_motor_position_counter(c.RMOTOR)
    
# Leaves rift valley
def leaveValley():
    print "leaveValley"
    drive(-98, -100)#-100, -100
    backToCounterRightMotor()# drive back 
    print get_motor_position_counter(c.RMOTOR)  
    if c.isPrime:
        driveTimed(0, 100, 800)#750
    else:
        driveTimed(0, 100, 1000)#750
    driveTimed(100, 100, 500)
    drive(0, 50) 
    while not onBlackFront():
        pass
    stop()
    
def squareUpForRamp():
    drive(0, 50)
    while onBlackFront():
        pass
    timedLineFollowLeftButton(10)
    # turn to go up the ramp
    drive(0, -80)
    wait4BlackFront(3)
    wait4WhiteFront(3)
    wait4BlackFront(3)
    drive(0, -30)
    wait4WhiteFront(3)
    if c.isPrime:
        driveTimed(100, 100, 1500)#100, 99, 3000
    else:
        driveTimed(100, 95, 3000)
    driveTimed(0, 30, 200)
    
def turnToRamp():
    drive(30, 0)
    wait4WhiteFront(3)
    timedLineFollowRight(1.9)#2
    timedLineFollowRightSmooth(1.5)
    driveTimed(75, -75, 850)#850
    driveTimed(100, 100, 1000)#400
    '''DEBUGwithWait()
    driveTimed(60, -60, 300) 
    msleep(1000)
    driveTimed(100, 100, 700) 
    DEBUGwithWait()'''
    
#finds ramp 
def centerOnRamp():
    print "centerOnRamp"
    if c.isPrime:
        driveTimed(-60, 60, 500)
    else:
        driveTimed(-60, 60, 300)
    drive(40, -40)
    wait4Ramp()
    wait4RampLine()
    wait4Ramp()
    stop()
    #driveTimed(40, right, time)
    
# drives up ramp
def goUpRamp():
    print "goUpRamp"
    if c.isPrime:
        driveTimed(100, 98, 1000)# 100,100,1000
    else:
        driveTimed(100, 88, 1000)# 100,100,1000
    moveFrontArm(c.frontArmUp, 20)#10
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
    moveFrontArm(c.frontArmUp, 25)#20
    msleep(500)
    
    
#shovels solar panels along crater rim
def moveSolarPanels():
    print "moveSolarPanels"
    drive(-50, 50)
    while not onBlackFront():
        pass
    stop()
    if c.isPrime:
        timedLineFollowRightSmooth(12.5)
    else:
        timedLineFollowRightSmooth(13.3)#12.9
    #DEBUGwithWait()
    
    
def deliverBotnaut():
    print "deliverBotnaut"
    driveTimed(-50, -50, 500)
    if c.isPrime:
        driveTimed(-60, -20, 3500)
        driveTimed(0, 60, 2300)  # was 2500
    else:
        driveTimed(-60, -10, 2800)
        driveTimed(0, 60, 2300)  # was 2500
    drive(60, 50)#50
    while not waitTouch():
        pass
    freezeMotors()
    if c.isPrime:
        driveTimed(-50, -50, 2200)  # was 1000
    else:
        driveTimed(-50, -50, 2000) #2000
    moveFrontArm(c.frontArmGrabBot, 10)
    moveFrontClaw(c.frontClawOpen, 20)
    moveFrontArm(c.frontArmUp, 10)

def removeDirt():
    print "removeDirt"
    if c.isPrime:
        driveTimed(-30, 30, 200) 
        moveBackArm(c.backArmSweep, 20)
        msleep(500)
        driveTimed(-33, -30, 500)  #400
        msleep(500)#
        driveTimed(30, -30, 1000)
        msleep(500)#
        moveBackClaw(c.backClawSqueeze, 30)
    
    else:
        driveTimed(-30, 30, 400) 
        moveBackArm(c.backArmSweep, 20)
        #msleep(500)
        disable_servo(2)
        msleep(500)
        enable_servo(2)
        msleep(500)
        driveTimed(-33, -30, 500) #1200
        msleep(500)#
        driveTimed(30, -30, 500)
        moveBackClaw(c.backClawOpen,20)
        driveTimed(30,-30, 500)
        moveBackClaw(c.backClawSqueeze, 400)
        msleep(500)#
        #moveBackClaw(c.backClawSqueeze, 30)
        
        
