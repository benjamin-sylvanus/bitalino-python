import os
import pyautogui
import time
import webbrowser
import sys, subprocess

def open_file(filename):
    if sys.platform == "win32":
        os.startfile(filename)
    else:
        opener = "open" if sys.platform == "darwin" else "xdg-open"
        subprocess.call([opener, filename])

open_file('example_txt.txt')
time.sleep(2)
pyautogui.write('Hello There', interval = 0.01)
pyautogui.keyDown('command')
pyautogui.press('a')
pyautogui.keyUp('command')
pyautogui.press('delete')

pyautogui.keyDown('command')
pyautogui.press('w')
pyautogui.keyUp('command')

time.sleep(2);
# pyautogui.press('delete');

# time.sleep(2)

webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
# pyautogui.keyDown('command')
# pyautogui.press('down')
# pyautogui.keyUp('command')
