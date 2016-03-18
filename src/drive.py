#16-ValleyBot drive.py
'''
Created on Mar 13, 2016

@author: Dead Robot Society
'''
from wallaby import motor
from wallaby import msleep
from wallaby import ao
from wallaby import seconds

from constants import LMOTOR
from constants import isPrime
from constants import RMOTOR
from constants import cubeDown

from servos import moveCube

from sensors import onBlack

def driveTimed( left, right, time):
    drive(left, right)
    msleep(time)
    ao()

def drive( left, right): 
    if isPrime: 
        #PRIME motor settings
        motor(LMOTOR, left)
        motor(RMOTOR, right)
    else:
        #CLONE motor settings
        motor(LMOTOR, left)
        motor(RMOTOR, right)
  
def testMotors():
    drive(-100, -100)
    while not onBlack(): #wait to see line
        pass
    driveTimed(-80, 80, 500)
    driveTimed(80, -80, 500)
    driveTimed(100, 100, 500)
    moveCube(cubeDown, 25)
    msleep(1000)
    
def timedLineFollowLeft(time): 
    sec = seconds() + time
    while seconds() < sec :
        if onBlack():
            driveTimed(20,90,10)
        else:
            driveTimed(90,20,10)
        msleep(10)

#Follows black line on right for specified amount of time
def timedLineFollowRight(time):
    sec = seconds() + time
    while seconds() < sec:
        if not onBlack():
            driveTimed(20,90,20)
        else:
            driveTimed(90, 20, 20)
        msleep(10)

def timedLineFollowRightSmooth(time):
    sec = seconds() + time
    while seconds() < sec:
        if not onBlack():
            driveTimed(20,40,20)
        else:
            driveTimed(40, 20, 20)
        msleep(10)

def timedLineFollowLeftSmooth(time):
    sec = seconds() + time
    while seconds() < sec:
        if onBlack():
            driveTimed(20,40,10)
        else:
            driveTimed(40,20,10)
        msleep(10)

    
