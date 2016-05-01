# Camera control
import piggyphoto

# Timing
import time
from valveControl import *
from variables import *
from dropboxConfig import DropboxInstance
from utilites import *

import os

dropboxInstance = DropboxInstance()

# Snap an image
def captureImage(camera, captureType):
  camera.capture_image("output/out.jpg")
  camera.close()

  fileName = 'output/' + time.strftime("%Y_%m_%d-%H_%M_%S") + "-" + captureType + ".jpg"

  return fileName

def saveToDropbox(fileName):
  # Upload to dropbox
  dropboxInstance.saveFile('output/out.jpg', fileName)

  # Delete locally
  os.remove('output/out.jpg')

def main():
  if PI_SETUP:
    wiringpi.wiringPiSetupGpio()
  else:
    print "Can't setup GPIO, not pi"

  while True:
    # Setup camera
    camera = piggyphoto.Camera()
    # camera.leave_locked()

    print
    print "1) Capture Fall"
    print "2) Capture Bounce"
    print "3) Capture Collision"
    print "4) Capture Custom"
    choice = raw_input("Selection: ")
    print

    if choice == '1':
      # Drop, wait, snap
      dropWater()
      wait(FALL_TIME)
      fileName = captureImage(camera, "fall")
      dropboxInstance.saveFile('output/out.jpg', fileName)

    elif choice == '2':
      # Drop, wait, snap
      dropWater()
      wait(BOUNCE_TIME)
      fileName = captureImage(camera, "bounce")
      dropboxInstance.saveFile('output/out.jpg', fileName)

    elif choice == '3':
      # Drop, wait, drop, wait, snap
      dropWater()
      wait(COLLISION_FALL_TIME)
      dropWater()
      wait(COLLISION_TIME)
      fileName = captureImage(camera, "collision")
      dropboxInstance.saveFile('output/out.jpg', fileName)

    elif choice == '4':
      # Drop, wait, snap
      fileName = captureImage(camera, "custom")
      dropboxInstance.saveFile('output/out.jpg', fileName)

if __name__ == "__main__":
  main()
