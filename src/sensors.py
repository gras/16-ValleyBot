# 16-ValleyBot sensors.py
'''
Created on Mar 13, 2016

@author: Dead Robot Society
'''

import constants as c

from wallaby import ao
from wallaby import msleep
from wallaby import analog
from wallaby import digital
from wallaby import seconds
from wallaby import a_button_clicked
from wallaby import b_button_clicked
from wallaby import freeze

def crossBlackFront():
    while not onBlackFront():  # wait for black
        pass
    while onBlackFront():  # wait for white
        pass
    freeze(c.LMOTOR)
    freeze(c.RMOTOR)
    
def crossBlackBack():
    while not onBlackBack(1):  # wait for black
        pass
    while onBlackBack(1):  # wait for white
        pass
    freeze(c.LMOTOR)
    freeze(c.RMOTOR)

def waitTouch():
    return digital(c.TOUCH)

def onBlackFront(repeat = 3):
    for x in range(repeat):
        if analog(c.FRONT_TOPHAT) < c.frontLineFollowerGrey: 
            return False
        if repeat > 1:
            msleep(10)
    return True

def onBlackBack():
    return analog(c.REAR_TOPHAT) > c.frontLineFollowerGrey 

def seeBotGuy ():
    return analog(c.ET) > c.ETbotGuy

def waitForButton():
    print "Press Button..."
    while not digital(c.RIGHT_BUTTON): 
        pass
    msleep(1)
    print "Pressed"
    msleep(1000)

def testSensors():
    print "trigger ET (make better print)"
    while seeBotGuy():
        pass
    while not seeBotGuy():
        pass
    while seeBotGuy():
        pass
    print "thanks"
    
    if onBlackFront():
        print "Problem with front tophat."
        print "Check for unplugged tophat or bad robot setup"
        DEBUG()
    if onBlackBack():
        print "Problem with back tophat."
        print "Check for unplugged tophat or bad robot setup"
        DEBUG()

def DEBUG():
    freeze(c.LMOTOR)
    freeze(c.RMOTOR)
    ao()
    print 'Program stop for DEBUG\nSeconds: ', seconds() - c.startTime
    exit(0)
    
def DEBUGwithWait():
    freeze(c.LMOTOR)
    freeze(c.RMOTOR)
    ao()
    print 'Program stop for DEBUG\nSeconds: ', seconds() - c.startTime
    msleep(5000)
    exit(0)
    
def wait4light():
    while not calibrate(c.STARTLIGHT):
        pass
    wait4(c.STARTLIGHT)

def calibrate(port):
    print "Press A button with light on"
    while not a_button_clicked():
        if digital(c.RIGHT_BUTTON):
            DEBUG()
    lightOn = analog(port)
    print "On value =", lightOn
    if lightOn > 200:
        print "Bad calibration"
        return False
    
    print "Press B button with light off"
    while not b_button_clicked():
        if digital(c.RIGHT_BUTTON):
            DEBUG()
    lightOff = analog(port)
    print "Off value =", lightOff
    if lightOff < 3000:
        print "Bad calibration"
        return False
    
    if (lightOff - lightOn) < 2000:
        print "Bad calibration"
        return False
    c.startLightThresh = (lightOff - lightOn) / 2
    print "Good calibration! ", c.startLightThresh 
    return True

def wait4(port):
    print "waiting for light!! " 
    while analog(port) > c.startLightThresh:
        pass
    
