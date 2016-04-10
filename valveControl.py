import time

# Pi control
pi = False
if pi:
  import wiringpi2 as wiringpi
  from variables import *

# Drop a drop
def dropWater(timeOverride=0):
  if timeOverride == 0:
    waitTime = DROP_WAIT
  else:
    waitTime = timeOverride

  if pi:
    print "Dropping Water"

    # Setup pin
    wiringpi.wiringPiSetupGpio()
    wiringpi.pinMode(SOLENOID_PIN, 1)

    # Open flow, wait, close flow
    wiringpi.digitalWrite(SOLENOID_PIN, 1)
    time.sleep(waitTime)
    wiringpi.digitalWrite(SOLENOID_PIN, 0)

  else:
    print "Can't drop, not a pi"
