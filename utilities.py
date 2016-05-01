import time
from variables import *

def wait(amount, customSleeping=CUSTOM_SLEEP):
  if debug:
    print "Waiting " + str(amount)

  start = time.time()
  if customSleeping:
    elapsedTime = time.time() - start
    while elapsedTime < amount:
      elapsedTime = time.time() - start
  else:
    time.sleep(amount)

  elapsedTime = time.time() - start

  if debug:
    print "Waited  " + str(elapsedTime)

if __name__ == "__main__":
  waitTime = 8/1000.0

  wait(waitTime, customSleeping=True)
  wait(waitTime, customSleeping=False)
