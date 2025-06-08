import pyautogui
import time

print("Move your mouse around. Press Ctrl+C to stop.\n")
try:
    while True:
        x, y = pyautogui.position()
        print(f"Mouse position: ({x}, {y})", end='\r')  # Overwrites the line
        time.sleep(0.1)
except KeyboardInterrupt:
    print("\nStopped.")
