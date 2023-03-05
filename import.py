import tkinter as tk
import cv2
import numpy
import datetime

# file name / link of file :

cap = cv2.VideoCapture("______.mp4")
root = tk.Tk()

# To find the resolution of the screen :

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Font style of the date and time to show in the video :

font = cv2.FONT_HERSHEY_SCRIPT_COMPLEX

# Input to start the video " must be in ' : '  "
 
timestamp = input('enter the time stamp in hh:mm:ss  ')

# Split the hours, minutes, seconds :
timestamp_list = timestamp.split(':')

# Assigning those hours, minutes, seconds with respective variables :
hh, mm, ss = timestamp_list

# changing timestamp in float from string :

timestamp_list_floats = [float(i) for i in timestamp_list]
hours, minutes, seconds = timestamp_list_floats

# Coverting all the desired variables in the seconds :
position=hours*3600+minutes*60+seconds

# set the video position to the desired position
cap.set(cv2.CAP_PROP_POS_MSEC, position * 1000)

# get the video's current position in seconds
current_position = cap.get(cv2.CAP_PROP_POS_MSEC) / 1000

while True:

    # Assigning the current date and time in a variable :
    dt = str(datetime.datetime.today())
    
    # Assigning the frame to show the video :
    ret, frame = cap.read()
    
    # Resizing the frame the video :
    frame=cv2.resize(frame,(screen_width//2,screen_height))
    
    
    frame = cv2.putText(frame, dt,(10, 100),font, 1,(210, 155, 155),4, cv2.LINE_8)
    key = cv2.waitKey(1) & 0xff

    if not ret:
        break

    cv2.imshow('frame',frame)
    if key == ord(' '):

        while True:

            key2 = cv2.waitKey(1) or 0xff
            cv2.imshow('frame', frame)

            if key2 == ord(' '):
                break
                
    elif key== ord('x') or key==27:
        break
cap.release()
cv2.destroyAllWindows()
