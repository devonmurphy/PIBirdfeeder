from gpiozero import MotionSensor
from picamera import PiCamera
from datetime import datetime
import cameraPI3
import time

camera = PiCamera()
pir = MotionSensor(4)
while True:
    pir.wait_for_motion()
    print 'motion detected'
    filename = datetime.now().strftime("/var/www/html/%Y-%m-%d_%H.%M.%S.h264")
   
   # camfilename = datetime.now().strftime("/var/www/html/%Y-%m-%d_%H.%M.%S.jpg")
   # camera.capture(camfilename)
    camera.start_recording(filename)
    pir.wait_for_no_motion()
    camera.stop_recording()
    print 'motion ended'
