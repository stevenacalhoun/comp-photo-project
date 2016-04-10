# Camera control
import piggyphoto

# Timing
import time
from variables import *

# Snap an image
def captureImage(camera, captureType):
  print "Snapping " + captureType
  fileName = time.strftime("%Y_%m_%d-%H_%M_%S") + "-" + captureType + ".json"
  camera.capture_image('output/' + fileName + '.jpg')

def main():
  while True:
    # Setup camera
    camera = piggyphoto.Camera()
    camera.leave_locked()

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
      time.sleep(FALL_TIME)
      captureImage(camera, "fall")

    elif choice == '2':
      # Drop, wait, snap
      dropWater()
      time.sleep(BOUNCE_TIME)
      captureImage(camera, "bounce")

    elif choice == '3':
      # Drop, wait, drop, wait, snap
      dropWater()
      time.sleep(COLLISION_FALL_TIME)
      dropWater()
      time.sleep(COLLISION_TIME)
      captureImage(camera, "collision")

    elif choice == '4':
      # Drop, wait, snap
      dropWater()
      time.sleep(CUSTOM_TIME)
      captureImage(camera, "custom")

    # Only way to take a new picture
    camera.close()

if __name__ == "__main__":
  main()
