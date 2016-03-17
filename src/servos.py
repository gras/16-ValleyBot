#16-ValleyBot servos.py
'''
Created on Mar 13, 2016

@author: Dead Robot Society
'''
from wallaby import set_servo_position
from wallaby import enable_servos
from wallaby import msleep
from wallaby import get_servo_position
from wallaby import ao

from constants import CLAW
from constants import ARM
from constants import CUBE_HOLDER
from constants import armUp
from constants import clawClosed
from constants import cubeDown
from constants import armDown
from constants import clawOpen
from constants import cubeUp


def testServos():
    set_servo_position(ARM, armUp)
    set_servo_position(CLAW, clawClosed)
    set_servo_position(CUBE_HOLDER, cubeDown)
    enable_servos()
    msleep(1000)
    moveArm(armDown, 25)
    moveClaw(clawOpen, 25) 
    msleep(500)
    moveClaw(clawClosed, 25)
    moveArm(armUp, 25) 
    moveCube(cubeUp, 25)
    msleep(1000)
   
def moveArm( endPos, speed=15 ):
    _moveServo( ARM, endPos, speed )

def moveClaw( endPos, speed=15 ):
    _moveServo( CLAW, endPos, speed )

def moveCube( endPos, speed=15 ):
    _moveServo( CUBE_HOLDER, endPos, speed )
    
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