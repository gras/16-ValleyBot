'''
Created on Mar 13, 2016

@author: Botball
'''
import wallaby as w
import constants as c
import servos as servo
import sensors as s


def driveTimed( left, right, time):
    drive(left, right)
    w.msleep(time)
    w.ao()

def drive( left, right): 
    if c.isPrime: 
        #PRIME motor settings
        w.motor(c.LMOTOR, left)
        w.motor(c.RMOTOR, right)
    else:
        #CLONE motor settings
        w.motor(c.LMOTOR, left)
        w.motor(c.RMOTOR, right)
  
def testMotors():
    drive(-100, -100)
    while not s.onBlack(): #wait to see line
        pass
    driveTimed(-80, 80, 500)
    driveTimed(80, -80, 500)
    driveTimed(100, 100, 500)
    servo.moveServo(c.CUBE_HOLDER, c.LOWERED, 25)
    w.msleep(1000)
