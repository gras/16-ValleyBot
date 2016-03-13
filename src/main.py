'''
Created on Mar 13, 2016

@author: Dead Robot Society
'''
import actions as act
#import constants as c
import servos as servo
import drive as d

def main():
    print "I am ValleyBot\n"
    print "ValleyBot test"
    act.init()
'''
    getOutOfStartBox()
    goToDebris()
    removeDebris()
    dumpDebris()
    goToGate()
    getGoldPoms()
    DEBUG()
'''
    
    
    
if __name__ == "__main__":
    # set print to unbuffered
    import os
    import sys
    sys.stdout = os.fdopen(sys.stdout.fileno(),'w',0)
    main()