import keyboard

print("Press any key (ESC to quit):")

while True:
    event = keyboard.read_event()
    if event.event_type == keyboard.KEY_DOWN:
        print(f"Key: {event.name} | Scan Code: {event.scan_code}")
        if event.name == 'esc':
            break
