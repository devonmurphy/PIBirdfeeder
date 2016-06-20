from gpiozero import MotionSensor
from picamera import PiCamera
from datetime import datetime
import time

motion_timeout = 6;
next_video_timeout = 0;
camera = PiCamera()
pir = MotionSensor(4)
while True:
    pir.wait_for_motion()
    print 'motion detected'
    filename = datetime.now().strftime("/var/www/html/%Y-%m-%d_%H.%M.%S.h264")
    camfilename = datetime.now().strftime("/var/www/html/%Y-%m-%d_%H.%M.%S.jpg")
    camera.capture(camfilename)
    camera.start_recording(filename)
    pir.wait_for_no_motion(motion_timeout)
    camera.stop_recording()
    print 'motion ended'
    time.sleep(next_video_timeout);
