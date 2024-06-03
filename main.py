import os
import sys
import tkinter as tk 
import time

def Stop(event):
    sys.exit()

def start_mouse():
    while True:
        while "Minecraft" in GetWindowText(GetForegroundWindow()):
            pyautogui.mouseDown()
        else:
            pyautogui.mouseUp()
            time.sleep(25)

def start_walking(lengthofline):
    State = 0
    while True:
        if State == 0:
            endTime = datetime.datetime.now() + datetime.timedelta(seconds=lengthofline)
            print(endTime)
            while datetime.datetime.now() < endTime and  "Minecraft" in GetWindowText(GetForegroundWindow()):
                print(endTime - datetime.datetime.now())
                print("W + A")
                pyautogui.keyDown('w')
                pyautogui.keyDown('a')
                
                if not "Minecraft" in GetWindowText(GetForegroundWindow()):
                    print("Waiting 30 secs")
                    endTime +=  datetime.timedelta(seconds=30)
                    threadingBot.sleep(30)

                if datetime.datetime.now() >= endTime:
                    pyautogui.keyUp('w')
                    pyautogui.keyUp('a')
                    State = 1
        #Run right
        if State == 1:
            endTime = datetime.datetime.now() + datetime.timedelta(seconds=lengthofline)
            print(endTime)
            while datetime.datetime.now() < endTime and  "Minecraft" in GetWindowText(GetForegroundWindow()):
                print(endTime - datetime.datetime.now())
                print("W + D")
                pyautogui.keyDown('w')
                pyautogui.keyDown('d')
                
                if not "Minecraft" in GetWindowText(GetForegroundWindow()):
                    print("Waiting 30 secs")
                    endTime +=  datetime.timedelta(seconds=30)
                    threadingBot.sleep(30)

                if datetime.datetime.now() >= endTime:
                    pyautogui.keyUp('w')
                    pyautogui.keyUp('d')
                    State = 0

def bot(lengthofline):
    print("Waiting 5 seconds and then starting so prepare your Minecraft...")
    threading_mouse.start()
    threading_walkbot.start(lengthofline)

def createGUI():
    print("Creating GUI...")
    print("Loading components...")
    print("Placing beacons...")
    print("Slaying Ender Dragon")

    # Create Tkinter instance 
    window = tk.Tk()
    window.title("Farmer's helper ;)")
    window.geometry("300x300")
    global lengthofline
    lengthofline = tk.IntVar()
    lof = tk.Entry(window, lengthofline)


    Startbutton = tk.Button(window, text="Start Bot", command=lambda : bot(lengthofline=lengthofline))
    Startbutton.pack()

    StopBot = tk.Button(text="Stop Bot")
    StopBot.bind("", Stop)

    window.mainloop()




# General imports if missing install (when program starts) -> goto main function and build GUI
if __name__ == "__main__":
    try:
        from win32gui import GetWindowText, GetForegroundWindow
        import keyboard
        import pyautogui 
        import datetime
        import threading
    except ImportError:
        print("That sucks importing missing dependencies now! ")
        os.system("cmd /k pip install keyboard && pip install pyautogui && pip install datetime && pip install threading && pip install pywin32")
        os.system("python {}".format(__file__))
    

    threading_walkbot = threading.Thread(start_walking(lengthofline))
    threading_mouse = threading.Thread(start_mouse())
    createGUI()