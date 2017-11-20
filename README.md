
#Face Authentication for GNOME
Author: Charles Michael Stein

THIS PACKAGE IS NOT REALLY SAFE FOR AUTHENTICATION

This package will wait for 5 seconds after the gnome is locked, and run facial detection every .5 secs. If it finds your face, it will automatically unlock and turn on the screen.

##Requirements
    - OpenCV 3.0
    - OpenCV python Bindings
    - Python3

##Install requirements
    pip3 install -r requirements.txt


##How to use
     - Replace the images inside data with your face images
     - Run the gnome_monitor.sh
Alternatively you can run the script on startup, just add it to /etc/rc.local like this

`nohup PATH_TO_FOLDER/gnome_monitor.sh &`