import pyautogui
import time

while True:
    x, y = pyautogui.position()  # get current mouse position
    pyautogui.moveTo(x + 30, y, duration=1)  # move 30px to the right
    time.sleep(1)
