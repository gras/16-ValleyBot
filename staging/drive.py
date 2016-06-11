# 16-ValleyBot drive.py
'''
Created on Mar 13, 2016

@author: Dead Robot Society
'''

import constants as c

# from sensors import DEBUG

from wallaby import motor
from wallaby import msleep
from wallaby import ao
from wallaby import seconds

from sensors import onBlackFront, onBlackBack

def driveTimed(left, right, time):
    drive(left, right)
    msleep(time)
    drive(0, 0)

def drive(left, right): 
    if c.isPrime: 
        # PRIME motor settings
        motor(c.LMOTOR, left)
        motor(c.RMOTOR, right)
    else:
        # CLONE motor settings
        motor(c.LMOTOR, left)
        motor(c.RMOTOR, right)
  
def testMotors():
    drive(-100, -100)
    while not onBlackFront():  # wait to see line
        pass
    stop()
    
    drive(100, 100)
    while not onBlackBack():  # wait to see line
        pass
    stop()
    
    driveTimed(-70, 0, 1000)
    driveTimed(70, 0, 1200)
    msleep(1000)      
    
def timedLineFollowLeft(time): 
    sec = seconds() + time
    while seconds() < sec :
        if onBlackFront():
            driveTimed(20, 90, 20)
        else:
            driveTimed(90, 20, 20)
        msleep(10)

# Follows black line on right for specified amount of time
def timedLineFollowRight(time):
    sec = seconds() + time
    while seconds() < sec:
        if not onBlackFront():
            driveTimed(20, 90, 20)
        else:
            driveTimed(90, 20, 20)
        msleep(10)

def timedLineFollowRightSmooth(time):
    sec = seconds() + time
    while seconds() < sec:
        if not onBlackFront():
            driveTimed(20, 40, 20)
        else:
            driveTimed(40, 20, 20)
        msleep(10)

def lineFollowRightSmoothCount(amount):
    count = 0
    while count < amount :
        if not onBlackFront():
            driveTimed(10, 30, 10)
            count = count + 1
        else:
            driveTimed(30, 10, 10)
            count = 0 
        
def timedLineFollowLeftSmooth(time):
    sec = seconds() + time
    while seconds() < sec :
        if onBlackFront():
            driveTimed(20, 40, 20)
        else:
            driveTimed(40, 20, 20)
        msleep(10)
        
def timedLineFollowLeftBack(time):  # follows on starboard side
    sec = seconds() + time
    while seconds() < sec : 
        if onBlackBack():
            driveTimed(-90, -20, 20)
        else:
            driveTimed(-20, -90, 20)
        msleep(10)
        
def lineFollowUntilEndLeftFront():
    i = 0
    while (i < 10):
        if onBlackFront():
            i = 0
            driveTimed(50, 90, 20)
        else:
            i = i + 1
            driveTimed(90, 50, 20)
            
def lineFollowUntilEndRightFront():
    i = 0
    while (i < 10):
        if onBlackFront():
            i = 0
            driveTimed(40, 35, 20)
        else:
            i = i + 1
            driveTimed(30, 50, 20)
        
def stop():
    ao()
