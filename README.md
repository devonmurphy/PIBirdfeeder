#Raspberry PI-Powered Bird Feeder

This project uses a Raspberry Pi connected to a camera and motion sensor to take pictures and videos of birds as they fly up to eat at a feeder.
The files uploaded to google drive with Grive2 for easy access from anywhere and 15 GB of free storage.
To insure that the Pi does not run out of memory, the files are deleted locally after they are synced.



#Dependencies

**Grive2**

This module gives the Pi the ability to upload files to a Google drive.

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
