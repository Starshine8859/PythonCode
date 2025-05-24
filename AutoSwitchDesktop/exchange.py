import keyboard
import time

def switch_desktop(direction="left"):
    if direction not in ["left", "right"]:
        raise ValueError("Direction must be 'left' or 'right'.")

    key = 'left' if direction == "left" else 'right'

    # Simulate Ctrl + Win + Left/Right
    keyboard.press('ctrl')
    keyboard.press('windows')
    keyboard.press(key)
    time.sleep(0.1)
    keyboard.release(key)
    keyboard.release('windows')
    keyboard.release('ctrl')

# Example: switch to the right desktop
switch_desktop("right")

# Example: switch to the left desktop
# switch_desktop("left")
