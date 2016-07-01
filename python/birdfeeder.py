from gpiozero import MotionSensor
from picamera import PiCamera
from datetime import datetime
import time
import os


if os.path.isfile('./authenticated')!=1:
	os.system("sudo grive --dry-run -a")
	f = open('authenticated','w')

motion_timeout = 6;
next_video_timeout = 0;
camera = PiCamera()
pir = MotionSensor(4)
while True:
    pir.wait_for_motion()
    print 'motion detected'
    filename = datetime.now().strftime("%Y-%m-%d_%H.%M.%S.h264") 
    camfilename = datetime.now().strftime("%Y-%m-%d_%H.%M.%S.jpg")
    camera.capture(camfilename)
    camera.start_recording(filename)
    pir.wait_for_no_motion(motion_timeout)
    camera.stop_recording()
    print 'motion ended'
    os.system("sudo grive -u -f")
    os.system("sudo rm *.jpg *.h264")
    time.sleep(next_video_timeout)
