#16-ValleyBot drive.py
'''
Created on Mar 13, 2016

@author: Dead Robot Society
'''
from wallaby import motor
from wallaby import msleep
from wallaby import ao

import constants as c
import servos as servo
import sensors as sensor


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
    while not sensor.onBlack(): #wait to see line
        pass
    driveTimed(-80, 80, 500)
    driveTimed(80, -80, 500)
    driveTimed(100, 100, 500)
    servo.moveServo(c.CUBE_HOLDER, c.LOWERED, 25)
    msleep(1000)
