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


def crossBlack():
    while not onBlack(): # wait for black
        pass
    while onBlack(): # wait for white
        pass
    ao()



def onBlack():
    return analog(c.LINE_FOLLOWER) > c.cubeMid 

def waitForButton():
    print "Press Button..."
    while not digital(c.RIGHT_BUTTON): 
        pass
    msleep(1)
    print "Pressed"
    msleep(1000)
