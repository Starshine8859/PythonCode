from pynput.mouse import Controller, Button
import time

# List of positions (X, Y)
click_positions = [
    (-2510, 99), (-2472, -33), (-2096, 158),
    (-2515, 609), (-2465, 477), (-2099, 665), 
    (-1659, 100), (-1620, -35), (-1239, 161),
    (-1657, 603), (-1620, 476), (-1239, 667),
    (84, 336), (128, 139), (699, 418), 
    (63, 1008), (136, 832), (696, 1111)
]

# Mouse controller
mouse = Controller()

# Delay between clicks
delay = 0.8  # seconds

for pos in click_positions:
    x, y = pos
    print(f"Clicking at {pos}")
    mouse.position = (x, y)
    time.sleep(0.2)  # Small delay to move the mouse
    mouse.click(Button.left, 1)
    time.sleep(delay)