#Dylan Cowley
#9/28/22
#Alarm Clock

from tkinter import *
from tkinter import ttk
from tkinter import font

import winsound
import calendar
import time
import datetime

alh = ""
alm = ""
als = ""
t = ""



timezone = 10
cdt = 5
mdt = 6
mst = 7
pdt = 7
adt = 8
hast = 10

darkred = "#8B0000"

def getTimeString(alh, alm, als, t):
    total_seconds = calendar.timegm(time.gmtime())
    cur_sec = total_seconds%60

    total_mins = total_seconds//60
    cur_min = total_mins%60

    total_hours = total_mins//60
    cur_hours = total_hours%24

    cur_hours -= mdt
    am_pm_tag = ""
    if cur_hours >= 12:
        cur_hours = cur_hours - 12
        am_pm_tag = "PM"

        if cur_hours == 0:
            cur_hours = cur_hours + 12
    else:
        am_pm_tag = "AM"
        if cur_hours == 0:
            cur_hours = cur_hours + 12
    xmin = str(cur_min)
    xsec = str(cur_sec)
    if cur_min < 10:
        xmin = "0"+str(cur_min)
    if cur_sec < 10:
        xsec = "0"+str(cur_sec)

    # alarm = str.format("{:2}:{:2}.{:2} {}", alh, alm, als, t)

    timeString = str.format("{:2}:{:2}.{:2} {}", cur_hours, xmin, xsec, am_pm_tag)
    timeString = str.format("{:2}:{:2}.{:2} {}", cur_hours, xmin, xsec, am_pm_tag)
    # if timeString == alarm:
    #     alarm_snd

    return timeString


def alarm_snd():
	for i in range(1, 10):
		winsound.Beep(i*100, 200)
	for i in range(9, 0, -1):
		winsound.Beep(i*100, 200)

def show_time():
    global alh
    global alm
    global als
    global t
    time = getTimeString(alh,alm,als,t)
    textvar.set(time)
    root.after(1000,show_time)



fullscreen = True


def setScreen(x):
    global fullscreen
    fullscreen = not fullscreen
    root.attributes("-fullscreen", fullscreen)
root = Tk()
root.geometry("500x500")
root.attributes("-fullscreen",fullscreen)
root.configure(background='Black')
root.bind("x", quit)
root.bind("f",setScreen)
root.title("Alarm Clock")
textvar=StringVar()
root.after(1000,show_time)
fnt = font.Font(family = "Robotic", size=45, weight= "bold")
lbl = ttk.Label(root,textvariable = textvar, font = fnt,foreground = darkred ,background = darkred )
lbl2 = ttk.Label(root,textvariable = textvar, font = fnt,foreground = "black" ,background = "maroon" )

lbl.place(relx=0.5, rely=0.5, anchor= CENTER)
lbl2.place(relx=0.49, rely=0.49, anchor= CENTER)


root.mainloop()