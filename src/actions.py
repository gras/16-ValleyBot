'''
Created on Mar 13, 2016

@author: Botball
'''

import wallaby as w 
#import time as t
import servos as servo
import drive as d
import constants as c
import sensors as s

def init():
    servo.testServos()
    d.testMotors()
    w.disable_servos()
    s.waitForButton()
    w.enable_servos()
    servo.moveServo(c.CLAW, c.CLOSE, 25)
    servo.moveServo(c.ARM, c.UP, 25) 
    return 0
    