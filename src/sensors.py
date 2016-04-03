#16-ValleyBot sensors.py
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

def crossBlackFront():
    while not onBlackFront(): # wait for black
        pass
    while onBlackFront(): # wait for white
        pass
    ao()
    
def crossBlackBack():
    while not onBlackBack(): # wait for black
        pass
    while onBlackBack(): # wait for white
        pass
    ao()

def onBlackFront():
    return analog(c.FRONT_TOPHAT) > c.frontLineFollowerGrey 

def onBlackBack():
    return analog(c.REAR_TOPHAT) > c.frontLineFollowerGrey 

def waitForButton():
    print "Press Button..."
    while not digital(c.RIGHT_BUTTON): 
        pass
    msleep(1)
    print "Pressed"
    msleep(1000)

def DEBUG():
    ao()
    print 'Program stop for DEBUG\nSeconds: ', seconds() - c.startTime
    exit(0)