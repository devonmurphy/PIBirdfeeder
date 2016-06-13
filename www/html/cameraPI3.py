from picamera import PiCamera
import datetime
camera = PiCamera()
def takepicture():
        localtime = datetime.datetime.now()
        name="%s-%s-%s-%s:%s:%s"%(localtime.year,localtime.month,localtime.day,localtime.hour,localtime.minute,localtime.second)
        camera.capture('/var/www/html/%s.jpg'%name)
        print("Picture saved as "+name)

takepicture()

"""
while(1):
	hold =''
        hold = raw_input('Press enter to take a picture, or control+c to quit')
        if(hold!='stop'):
                takepicture()
		hold = 'stop'
"""
