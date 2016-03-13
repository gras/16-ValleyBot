'''
Created on Mar 13, 2016

@author: Botball
'''
import wallaby as w
import constants as c
import drive as d

def crossBlack():
    while not onBlack(): # wait for black
        pass
    while onBlack(): # wait for white
        pass
    w.ao()

def timedLineFollowLeft(time): 
    sec = w.seconds() + time
    while w.seconds() < sec :
        if not onBlack():
            d.driveTimed(20,90,10)
        else:
            d.driveTimed(90,20,10)
        w.msleep(10)
    
def onBlack():
    return w.analog(c.LINE_FOLLOWER) > c.MID_VALUE 

def waitForButton():
    print "Press Button..."
    while not w.digital(c.RIGHT_BUTTON): 
        pass
    w.msleep(1)
    print "Pressed"
    w.msleep(1000)
