#16-ValleyBot sensors.py
'''
Created on Mar 13, 2016

@author: Dead Robot Society
'''
from wallaby import ao
from wallaby import msleep
from wallaby import analog
from wallaby import digital

from constants import LINE_FOLLOWER
from constants import cubeMid
from constants import RIGHT_BUTTON

def crossBlack():
    while not onBlack(): # wait for black
        pass
    while onBlack(): # wait for white
        pass
    ao()



def onBlack():
    return analog(LINE_FOLLOWER) > cubeMid 

def waitForButton():
    print "Press Button..."
    while not digital(RIGHT_BUTTON): 
        pass
    msleep(1)
    print "Pressed"
    msleep(1000)
