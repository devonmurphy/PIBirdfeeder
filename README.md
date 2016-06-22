#Raspberry PI-Powered Bird Feeder

This project uses a Raspberry Pi connected to a camera and motion sensor to take pictures and videos of birds as they fly up to eat at a feeder.

The files synced to google drive with Grive2 so that they can be easily accessed from anywhere.

To insure that the Pi does not run out of memory the files are deleted locally after they are uploaded.

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

#Use

**Download The Project**
<pre>
sudo git clone github.com/devonmurphy/PIBirdfeeder
</pre>
**Authenticate With Google Drive**
<pre>
cd PIbirdfeeder/
grive -a -u -f
</pre>
Google will then give a link with a hash that can be used to authenticate a folder to sync with google drive.
**Take A Picture**
<pre>
sudo  python camera.py
</pre>
**Start The Birdfeeder**
<pre>
sudo python birdfeeder.py
</pre>

