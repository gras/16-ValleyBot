#16-ValleyBot main.py
'''
Created on Mar 13, 2016

@author: Dead Robot Society
'''
import actions as act
import constants as c 

def main():
    print "I am ValleyBot"
    #if c.isClone():
    #    print "I am Clone"
    #else: 
    #    print "I am Prime"
    act.init()
    act.getOutOfStartBox()
    act.goToDebris()
    act.removeDebris()
    act.dumpDebris()
    act.goToGate()
    act.goToCube()
    act.dropOffCube()
    act.getGoldPoms()
    act.depositGoldPoms()
    act.goToValley()
    act.getRedPoms()
    return 0

    
if __name__ == "__main__":
    # set print to unbuffered
    import os
    import sys
    sys.stdout = os.fdopen(sys.stdout.fileno(),'w',0)
    main()