from pynput.mouse import Listener, Button
import time

log_file = "mouse_clicks_log.txt"
double_click_threshold = 0.3  # seconds
position_threshold = 5        # pixels

last_click_time = 0
last_click_pos = (0, 0)
last_click_button = None

def is_close(pos1, pos2, threshold):
    return abs(pos1[0] - pos2[0]) <= threshold and abs(pos1[1] - pos2[1]) <= threshold

def on_click(x, y, button, pressed):
    global last_click_time, last_click_pos, last_click_button

    if pressed:
        current_time = time.time()
        click_type = "Single"

        if (
            current_time - last_click_time <= double_click_threshold and
            is_close((x, y), last_click_pos, position_threshold) and
            button == last_click_button
        ):
            click_type = "Double"

        if button == Button.left:
            button_name = "Left"
        elif button == Button.right:
            button_name = "Right"
        else:
            button_name = str(button)

        entry = f"{click_type} {button_name} click at ({x}, {y})"
        print(entry)

        with open(log_file, "a") as f:
            f.write(entry + "\n")

        # Exit on double right click
        if button == Button.right and click_type == "Double":
            print("Double right-click detected. Exiting.")
            return False  # This stops the listener

        # Update last click
        last_click_time = current_time
        last_click_pos = (x, y)
        last_click_button = button

# Start the listener
with Listener(on_click=on_click) as listener:
    listener.join()
