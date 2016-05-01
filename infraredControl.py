from variables import *
from utilities import *

if PI_SETUP:
  import wiringpi

def triggerRemote():
  if PI_SETUP:
    wiringpi.pinMode(CAMERA_PIN, 1)
    wiringpi.digitalWrite(CAMERA_PIN, 1)
    wait(2)
    wiringpi.digitalWrite(CAMERA_PIN, 0)
  else:
    print "Can't trigger remote, not pi"
