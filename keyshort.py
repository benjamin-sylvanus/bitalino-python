import os, sys, subprocess
import pyautogui
import time
import webbrowser

# Open file for different operating systems
def open_file(filename):
    if sys.platform == "win32":
        os.startfile(filename)
    else:
        opener = "open" if sys.platform == "darwin" else "xdg-open"
        subprocess.call([opener, filename])

open_file('example_txt.txt')                    # example text file
time.sleep(2)                                   # wait 2 seconds
pyautogui.write('Hello There', interval = 0.01) # write what is in string
pyautogui.keyDown('command')                    # press command a
pyautogui.press('a')
pyautogui.keyUp('command')
pyautogui.press('delete')                       # delete contents of ex file
pyautogui.keyDown('command')                    # close the file command w
pyautogui.press('w')
pyautogui.keyUp('command')

time.sleep(2)
webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ") # open link
