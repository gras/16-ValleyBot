#16-ValleyBot main.py
'''
Created on Mar 13, 2016

@author: Dead Robot Society
'''
import actions as act

from sensors import DEBUG, DEBUGwithWait

def main():
    print "I am ValleyBot"    
    act.init()
    act.grabSolarArraysInBox()
    act.getOutOfStartBox()
    act.goToComposter()
    act.removeDebris()
    act.dumpDebris()
    act.goToGate()
    act.goToCube()
    act.dropOff() 
    act.goToValley()
    act.goToBotGuy()
    act.goToRamp()
    act.goUpRamp()
    act.cleanSolarPanels()
    DEBUG()    
    
    
    return 0
    
if __name__ == "__main__":
    # set print to unbuffered
    import os
    import sys
    sys.stdout = os.fdopen(sys.stdout.fileno(),'w',0)
    main()