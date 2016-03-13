'''
Created on Mar 13, 2016

@author: Botball
'''
import wallaby as w
import constants as c


def testServos():
    w.set_servo_position(c.ARM, c.UP)
    w.set_servo_position(c.CLAW, c.CLOSE)
    w.set_servo_position(c.CUBE_HOLDER, c.LOWERED)
    w.enable_servos()
    w.msleep(1000)
    moveServo(c.ARM, c.DOWN, 25)
    moveServo(c.CLAW, c.OPEN, 25) 
    w.msleep(500)
    moveServo(c.CLAW, c.CLOSE, 25)
    moveServo(c.ARM, c.UP, 25) 
    moveServo(c.CUBE_HOLDER, c.RAISED, 25)
    w.msleep(1000)
   
    
# Moves specified servo to specified position at specified speed
def moveServo( servo, endPos, speed=10 ) :
    # speed of 1 is slow
    # speed of 2000 is fast
    # speed of 10 is the default
    now = w.get_servo_position( servo )
    if now > 2048 :
        PROGRAMMER_ERROR( "Servo setting too large" )
    if now < 0 :
        PROGRAMMER_ERROR( "Servo setting too small" )
    if now > endPos:
        speed = -speed
    for i in range (now, endPos, speed ):
        w.set_servo_position( servo, i)
        w.msleep(10)
    w.set_servo_position( servo, endPos )
    w.msleep(10)


def PROGRAMMER_ERROR( msg ) :
    w.ao()
    print msg
    exit()