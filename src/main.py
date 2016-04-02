#16-ValleyBot main.py
'''
Created on Mar 13, 2016

@author: Dead Robot Society
'''
import actions as act

from sensors import DEBUG

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
    act.getGoldPoms()
    act.getRedPoms()
    act.leaveValley()
    act.goToHabitat()
    act.depositGoldPoms()
    DEBUG()   
    act.depositRedPoms() 
    act.getComposter()    
    act.deliverComposter()    
    act.depositGoldPoms()
    
    #act.returnToValley()
    
    return 0

    
if __name__ == "__main__":
    # set print to unbuffered
    import os
    import sys
    sys.stdout = os.fdopen(sys.stdout.fileno(),'w',0)
    main()