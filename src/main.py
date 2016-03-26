#16-ValleyBot main.py
'''
Created on Mar 13, 2016

@author: Dead Robot Society
'''
import actions as act
from actions import DEBUG

def main():
    print "I am ValleyBot"
    act.init()
    act.getOutOfStartBox()
    act.goToDebris()
    act.removeDebris()
    act.dumpDebris()
    act.goToGate()
    act.goToCube()
    act.dropOffCube()
    DEBUG()
    act.getRedPoms()
    act.DEBUG()
    act.leaveValley()
    act.depositRedPoms()
    act.goToValley()
    act.getGoldPoms()
    act.getOutOfValley()
    act.depositGoldPoms()
    #act.returnToValley()
    
    return 0

    
if __name__ == "__main__":
    # set print to unbuffered
    import os
    import sys
    sys.stdout = os.fdopen(sys.stdout.fileno(),'w',0)
    main()