import time
from variables import *

def init():
  global fallTime, bounceTime, collisionFallTime, collisionTime, customTime, dropWait

  fallTime = FALL_TIME
  bounceTime = BOUNCE_TIME
  collisionFallTime = COLLISION_FALL_TIME
  collisionTime = COLLISION_TIME
  customTime = CUSTOM_TIME
  dropWait = DROP_WAIT

def wait(amount, customSleeping=CUSTOM_SLEEP):
  if DEBUG:
    print "Waiting " + str(amount)

  start = time.time()
  if customSleeping:
    elapsedTime = time.time() - start
    while elapsedTime < amount:
      elapsedTime = time.time() - start
  else:
    time.sleep(amount)

  elapsedTime = time.time() - start

  if DEBUG:
    print "Waited  " + str(elapsedTime)

def setTime():
  global fallTime, bounceTime, collisionFallTime, collisionTime, customTime, dropWait

  print
  print "1) Set Fall"
  print "2) Set Bounce"
  print "3) Set Collision Fall"
  print "4) Set Collision"
  print "5) Set Custom"
  print "6) Set drop wait"
  choice = raw_input("Selection: ")
  print

  if choice == '1':
    fallTime = getNewTime()
    print "New Fall time: " + str(fallTime) + " seconds"

  elif choice == '2':
    bounceTime = getNewTime()
    print "New Bounce time: " + str(bounceTime) + " seconds"

  elif choice == '3':
    collisionFallTime = getNewTime()
    print "New Collision Fall time: " + str(collisionFallTime) + " seconds"

  elif choice == '4':
    collisionTime = getNewTime()
    print "New Collision time: " + str(collisionTime) + " seconds"

  elif choice == '5':
    customTime = getNewTime()
    print "New Custom time: " + str(customTime) + " seconds"

  elif choice == '6':
    dropWait = getNewTime()
    print "New Drop Wait time: " + str(dropWait) + " seconds"

def getNewTime():
    print
    choice = raw_input("Milliseconds: ")
    print

    return float(choice)/1000

def printTimeSettings():
  global fallTime, bounceTime, collisionFallTime, collisionTime, customTime, dropWait

  print "Fall Time: " + str(fallTime*1000.0) + " milliseconds"
  print "Bounce Time: " + str(bounceTime*1000.0) + " milliseconds"
  print "Collision Fall Time: " + str(collisionFallTime*1000.0) + " milliseconds"
  print "Collision Time: " + str(collisionTime*1000.0) + " milliseconds"
  print "Custom Time: " + str(customTime*1000.0) + " milliseconds"
  print "Drop Wait: " + str(dropWait*1000.0) + " milliseconds"

if __name__ == "__main__":
  waitTime = 8/1000.0

  wait(waitTime, customSleeping=True)
  wait(waitTime, customSleeping=False)
