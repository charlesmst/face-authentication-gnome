#!/bin/bash

BASEDIR=$(dirname "$0")
cd $BASEDIR
dbus-monitor --session "type='signal',interface='org.gnome.ScreenSaver'" | \
( while true
    do read X
    if echo $X | grep "boolean true" &> /dev/null; then
       	echo "$(date) - Starting face scanner" 
	    python3 unlocker.py & echo $! > .running_pid
    elif echo $X | grep "boolean false" &> /dev/null; then
	    echo "$(date) Killing process because of unlock"
	    kill -9 `cat .running_pid`
    fi
    # echo "Running..."
    done )
