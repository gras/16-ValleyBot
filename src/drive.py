#16-ValleyBot drive.py
'''
Created on Mar 13, 2016

@author: Dead Robot Society
'''

import constants as c

from wallaby import motor
from wallaby import msleep
from wallaby import ao
from wallaby import seconds

from sensors import onBlackFront, onBlackBack
from constants import isPrime, isClone

def driveTimed( left, right, time):
    drive(left, right)
    msleep(time)
    ao()

def drive( left, right): 
    if c.isPrime: 
        #PRIME motor settings
        motor(c.LMOTOR, left)
        motor(c.RMOTOR, right)
    else:
        #CLONE motor settings
        motor(c.LMOTOR, left)
        motor(c.RMOTOR, right)
  
def testMotors():
    drive(-100, -100)
    while not onBlackFront(): #wait to see line
        pass
    if isPrime:
        driveTimed(-70, 70, 500)
        driveTimed(70, -70, 500)
    else:
        drive(-100, 0)
        while not onBlackBack(): #wait to see line
            pass
        driveTimed(100, 0, 650)
    driveTimed(100, 100, 500)
    msleep(1000)       
    
def timedLineFollowLeft(time): 
    sec = seconds() + time
    while seconds() < sec :
        if onBlackFront():
            driveTimed(20,90,10)
        else:
            driveTimed(90,20,10)
        msleep(10)

#Follows black line on right for specified amount of time
def timedLineFollowRight(time):
    sec = seconds() + time
    while seconds() < sec:
        if not onBlackFront():
            driveTimed(20,90,20)
        else:
            driveTimed(90,20,20)
        msleep(10)

def timedLineFollowRightSmooth(time):
    sec = seconds() + time
    while seconds() < sec:
        if not onBlackFront():
            driveTimed(20,40,20)
        else:
            driveTimed(40,20,20)
        msleep(10)

def timedLineFollowLeftSmooth(time):
    sec = seconds() + time
    while seconds() < sec:
        if onBlackFront():
            driveTimed(20,40,20)#time was 10
        else:
            driveTimed(40,20,20)#time was 10 
        msleep(10)

    
