from valveControl import *
from variables import *

fallTime = FALL_TIME
bounceTime = BOUNCE_TIME
collisionFallTime = COLLISION_FALL_TIME
collisionTime = COLLISION_TIME
customTime = CUSTOM_TIME
dropWait = DROP_WAIT

def main():
  global fallTime, bounceTime, collisionFallTime, collisionTime, customTime, dropWait
  while True:
    print
    print "1) Test Fall"
    print "2) Test Bounce"
    print "3) Test Collision"
    print "4) Test Other"
    print "s) Set time"
    choice = raw_input("Selection: ")
    print

    if choice == '1':
      # Drop, wait, snap
      dropWater(dropWait)
      time.sleep(fallTime)
      print "Capture"

    elif choice == '2':
      # Drop, wait, snap
      dropWater(dropWait)
      time.sleep(bounceTime)
      print "Capture"

    elif choice == '3':
      # Drop, wait, drop, wait, snap
      dropWater(dropWait)
      time.sleep(collisionFallTime)
      dropWater(dropWait)
      time.sleep(collisionTime)
      print "Capture"

    elif choice == '4':
      # Drop, wait, snap
      dropWater(dropWait)
      time.sleep(customTime)
      print "Capture"

    elif choice == 's':
      setTime()

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

if __name__ == "__main__":
  main()
