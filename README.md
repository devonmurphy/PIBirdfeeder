#Raspberry Pi-Powered Bird Feeder

This project uses a Raspberry Pi connected to a camera and motion sensor to take pictures and videos of birds as they fly up to eat at a feeder.

The files are uploaded to Google drive with Grive2 and then deleted locally. This insures that the Pi will never run out of memory.

#Use

**Download The Project**
<pre>
git clone github.com/devonmurphy/PIBirdfeeder
</pre>
**Connect python Folder With Google Drive**
<pre>
cd PIbirdfeeder/python
grive -a -u -f
</pre>
Grive will return a link to a hash that can be used to authenticate a folder to sync with Google drive.

After an account is connected, the Pi can save the videos and pictures it takes to the cloud.

**Take A Picture**
<pre>
python camera.py
</pre>
**Start The Birdfeeder**
<pre>
sudo python birdfeeder.py
</pre>

#Dependencies

**Grive2**

This module gives the Pi the ability to upload files to a Google drive.

Follow the guide in this link:

http://yourcmc.ru/wiki/Grive2#Installation

**Applications**
<pre>
sudo apt-get install python
</pre>

**Python Libraries**
<pre>
pip install gpiozero
pip install picamera
</pre>

