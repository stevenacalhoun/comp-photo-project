# Timing
import time

import utilities
import variables

import valveControl
import cameraControl

import os
import sys

def main():
  utilities.init()

  if variables.PI_SETUP:
    wiringpi.wiringPiSetupGpio()
  else:
    print "Can't setup GPIO, not pi"

  while True:
    print
    print "1) Capture Fall"
    print "2) Capture Bounce"
    print "3) Capture Collision"
    print "4) Capture Custom"
    print "s) Change times"
    print "o) Open valve"
    print "c) Close valve"
    print "q) Quit"
    choice = raw_input("Selection: ")
    print

    if choice == '1':
      # Drop, wait, snap
      valveControl.dropWater()
      utilities.wait(utilities.fallTime)
      cameraControl.triggerRemote()

    elif choice == '2':
      # Drop, wait, snap
      valveControl.dropWater()
      utilities.wait(utilities.bounceTime)
      cameraControl.triggerRemote()

    elif choice == '3':
      # Drop, wait, drop, wait, snap
      valveControl.dropWater()
      utilities.wait(utilities.collisionFallTime)
      valveControl.dropWater()
      utilities.wait(utilities.collisionTime)
      cameraControl.triggerRemote()

    elif choice == '4':
      # Drop, wait, snap
      valveControl.dropWater()
      utilities.wait(utilities.customTime)
      cameraControl.triggerRemote()

    elif choice == 's':
      utilities.setTime()

    elif choice == 'o':
      openValve()

    elif choice == 'c':
      closeValve()

    elif choice == 'q':
      utilities.printTimeSettings()
      sys.exit()

if __name__ == "__main__":
  main()
