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
    #DEBUG()
    act.goToGate() 
    act.goToCube()
    act.dropOffCube()  
    act.getGoldPoms()
    act.getRedPoms()
    act.leaveValley()
    act.waitForTater()
    act.goToHabitat()
    act.depositGoldPoms()
    act.depositRedPoms()
    act.getComposter()  
    act.deliverComposter()  
    act.depositComposter()
    act.goToCube2()
    act.scoreCube() 
    act.returnToValley()
    act.deliverBotGuy()
    DEBUG()    
    return 0
    
if __name__ == "__main__":
    # set print to unbuffered
    import os
    import sys
    sys.stdout = os.fdopen(sys.stdout.fileno(),'w',0)
    main()