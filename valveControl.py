import time
from variables import *

# Pi control
if PI_SETUP:
  import wiringpi

from variables import *

# Drop a drop
def dropWater(timeOverride=0):
  if timeOverride == 0:
    waitTime = DROP_WAIT
  else:
    waitTime = timeOverride

  print "Dropping Water"

  # Setup pin
  if pi:
    wiringpi.pinMode(SOLENOID_PIN, 1)
  else:
    print "Can't setup pin, not pi"

  # Open flow, wait, close flow
  openValve()
  wait(waitTime)
  closeValve()


def openValve():
  if pi:
    wiringpi.digitalWrite(SOLENOID_PIN, 1)
  else:
    print "Can't open, not pi"

def closeValve():
  if pi:
    wiringpi.digitalWrite(SOLENOID_PIN, 0)
  else:
    print "Can't close, not pi"
