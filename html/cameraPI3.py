from picamera import PiCamera
import datetime



def takepicture():
	camera = PiCamera()
	localtime = datetime.datetime.now()
        name="%s-%s-%s-%s:%s:%s"%(localtime.year,localtime.month,localtime.day,localtime.hour,localtime.minute,localtime.second)
        
	camera.capture('/var/www/html/%s.jpg'%name)
        print("Picture saved as "+name)


takepicture()
