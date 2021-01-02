import psutil
import time
import os
import sys


def checkProcesses(processName):

    for proc in psutil.process_iter():
        try:
            if processName in proc.name():
                return True
        except(psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    return False

def killer(g):
    time.sleep(g)
    os.system('taskkill /F /IM chrome.exe')
    sys.exit()

while(1):
    if (checkProcesses('chrome.exe')):
        timecal = input("hour,min,sec?")
        if timecal == 'hour':
            f = int(input("How many a do you want?"))*120
            killer(f)
            break

        elif timecal =="min":
            c = int(input("How many min do you want?")) * 60
            killer(c)
            break
        elif timecal == "sec":
            b = int(input("How many sec do you want?"))
            killer(b)
            break
        else:
            print("Wrong input")
            continue
