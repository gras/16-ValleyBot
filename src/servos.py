#16-ValleyBot servos.py
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
    set_servo_position(c.ARM, c.armUp)
    set_servo_position(c.CLAW, c.clawClose)
    set_servo_position(c.CUBE_HOLDER, c.cubeDown)
    enable_servos()
    msleep(1000)
    moveArm(c.armDown, 25)
    moveClaw(c.clawOpen, 25) 
    moveCube(c.cubeDown, 25)
    msleep(500)
    moveClaw(c.clawClose, 25)
    msleep(500)
    moveArm(c.armUp, 25)
    msleep(500) 
    moveCube(c.cubeUp, 25)
    msleep(1000)
   
def moveArm( endPos, speed=15 ):
    _moveServo( c.ARM, endPos, speed )

def moveClaw( endPos, speed=15 ):
    _moveServo( c.CLAW, endPos, speed )

def moveCube( endPos, speed=15 ):
    _moveServo( c.CUBE_HOLDER, endPos, speed )
    
# Moves specified servo to specified position at specified speed
def _moveServo( servo, endPos, speed) :
    # speed of 1 is slow
    # speed of 2000 is fast
    # speed of 10 is the default
    now = get_servo_position( servo )
    if now > 2048 :
        PROGRAMMER_ERROR( "Servo setting too large" )
    if now < 0 :
        PROGRAMMER_ERROR( "Servo setting too small" )
    if now > endPos:
        speed = -speed
    for i in range (now, endPos, speed ):
        set_servo_position( servo, i)
        msleep(10)
    set_servo_position( servo, endPos )
    msleep(10)
    



def PROGRAMMER_ERROR( msg ) :
    ao()
    print msg
    exit()