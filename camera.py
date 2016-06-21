from picamera import PiCamera
import datetime
import os


def takepicture():
	camera = PiCamera()
	localtime = datetime.datetime.now()
        name="%s-%s-%s-%s:%s:%s"%(localtime.year,localtime.month,localtime.day,localtime.hour,localtime.minute,localtime.second)
        
	camera.capture('%s.jpg'%name)
        print("Picture saved as "+name)
	os.system("sudo grive -u -f")
	os.system("sudo rm *.jpg")
takepicture()
