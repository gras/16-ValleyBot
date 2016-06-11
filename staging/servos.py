# 16-ValleyBot servos.py
'''
Created on Mar 13, 2016

@author: Dead Robot Society
'''

import constants as c

from wallaby import set_servo_position
from wallaby import enable_servos
from wallaby import msleep
from wallaby import get_servo_position
from wallaby import ao

def testServos():
    set_servo_position(c.frontArm, c.frontArmUp)
    set_servo_position(c.frontClaw, c.frontClawClose)
    set_servo_position(c.backArm, c.backArmUp)
    set_servo_position(c.backClaw, c.backClawClose)
    enable_servos()
    msleep(1000)
    moveFrontArm(c.frontArmDown, 25)
    msleep(500)
    moveFrontArm(c.frontArmUp, 25)
    moveFrontClaw(c.frontClawOpen, 25) 
    msleep(500)
    moveFrontClaw(c.frontClawClose, 25)    
    moveBackArm(c.backArmDown, 25)
    msleep(500)
    moveBackArm(c.backArmUp, 25)
    moveBackClaw(c.backClawOpen, 25) 
    msleep(500)
    moveBackClaw(c.backClawClose, 25)
    msleep(1000)
   
def moveFrontArm(endPos, speed=15):
    _moveServo(c.frontArm, endPos, speed)

def moveFrontClaw(endPos, speed=15):
    _moveServo(c.frontClaw, endPos, speed)

def moveBackArm(endPos, speed=15):
    _moveServo(c.backArm, endPos, speed)

def moveBackClaw(endPos, speed=15):
    _moveServo(c.backClaw, endPos, speed)
    
# Moves specified servo to specified position at specified speed
def _moveServo(servo, endPos, speed) :
    # speed of 1 is slow
    # speed of 2000 is fast
    # speed of 10 is the default
    now = get_servo_position(servo)
    if now > 2048 :
        PROGRAMMER_ERROR("Servo setting too large ", servo)
    if now < 0 :
        PROGRAMMER_ERROR("Servo setting too small ", servo)
    if now > endPos:
        speed = -speed
    for i in range (now, endPos, speed):
        set_servo_position(servo, i)
        msleep(10)
    set_servo_position(servo, endPos)
    msleep(10)
    
def PROGRAMMER_ERROR(msg, value) :
    ao()
    print msg, value
    exit()
