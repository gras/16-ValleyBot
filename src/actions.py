#16-ValleyBot actions.py
'''
Created on Mar 13, 2016

@author: Dead Robot Society
'''

import wallaby as w 
import servos as servo
import drive as d
import constants as c
import sensors as s

#Stops the program for testing
def DEBUG():
    w.ao()
    print"Stopped for debug \n"
    exit(0)

def init():
    servo.testServos()
    d.testMotors()
    w.disable_servos()
    s.waitForButton()
    w.enable_servos()
    servo.moveServo(c.CLAW, c.CLOSE, 25)
    servo.moveServo(c.ARM, c.UP, 25) 
    return 0

#Raises cube holder
#Backs out of start box and turns 
#Moves backward until black tape
def getOutOfStartBox():
    print "getOutOfStartBox\n"
    servo.moveServo(c.CUBE_HOLDER, c.RAISED, 25)
    w.msleep(500)
    d.driveTimed(-100, -100, 1600)
    d.driveTimed(0, 100, 400)
    d.driveTimed(70,70,600)

#Follows line for 3.5 seconds
#Moves forward until robot reaches debris
def goToDebris():
    print "goToDebris\n"
    s.timedLineFollowLeft(3.5); 
    d.driveTimed(50, 50, 1000);

#Moves claw arm down and drives backwards with debris
def removeDebris():
    print "removeDebris\n"
    servo.moveServo(c.ARM, c.DOWN, 15); 
    w.msleep(500);
    d.driveTimed(-80, -80, 500);

#Dumps debris next to compost
def dumpDebris():
    d.driveTimed(0,-100,1000);
    d.driveTimed(60,70,500);
    d.driveTimed(90,0,500);
    d.driveTimed(60,90,225); 
    d.driveTimed(60,70,650);

#Drives backwards and follows line to reach gate
def goToGate():
    servo.moveServo(c.ARM, c.UP, 15);
    d.driveTimed(-100,-100, 1250);
    s.timedLineFollowRight(1.3);
    s.timedLineFollowRightSmooth(3.3);

def goToCube():
    servo.moveServo(c.CLAW, c.OPEN, 15)
    servo.moveServo(c.ARM, c.DOWN, 15)
    d.drive(100, 100)
    while not s.onBlack():
        pass
    d.drive(0, 0)
    servo.moveServo(c.CLAW, c.CLOSE, 15)
    servo.moveServo(c.ARM, c.UP, 15)
    w.msleep(3000)
    #driveTimed(0, 100, 1500) Work on dropping red block off on own side of board

#Turns to drop cube off on our side of the board
def dropOffCube():
    d.driveTimed(100, 0, 1900)
    servo.moveServo(c.ARM, c.MID, 15)
    servo.moveServo(c.CLAW, c.OPEN, 15)
    w.msleep(500)
    servo.moveServo(c.ARM, c.UP, 15)


#drives to grab gold poms
def getGoldPoms():
    d.driveTimed(-100, 0, 2300)
    
    
    
    