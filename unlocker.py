import os
from time import sleep
from recognizer import wait_recognize_face
print("unlocker running, wait 5 seconds to start...")

#wait 5 secs until user leave the notebook
sleep(5)
print("Start analyzing")
wait_recognize_face()
#gnome command to unlock screen
os.system('DISPLAY=:0 gnome-screensaver-command -d')
os.system('xset dpms force on')
