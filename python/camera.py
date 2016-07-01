from picamera import PiCamera
import datetime
import os

if os.path.isfile('./authenticated')!=1:
        os.system("sudo grive --dry-run -a")
        f = open('authenticated','w')

def takepicture():
	camera = PiCamera()
	localtime = datetime.datetime.now()
        name="%s-%s-%s-%s:%s:%s"%(localtime.year,localtime.month,localtime.day,localtime.hour,localtime.minute,localtime.second)
        
	camera.capture('%s.jpg'%name)
        print("Picture saved as "+name)
	os.system("sudo grive -u -f")
	os.system("sudo rm *.jpg")

takepicture()
