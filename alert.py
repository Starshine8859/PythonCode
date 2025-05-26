import tkinter as tk
from tkinter import messagebox
import platform
import os

def play_alert_sound():
    system = platform.system()
    if system == "Windows":
        import winsound
        winsound.Beep(750, 300)
    elif system == "Darwin":  # macOS
        os.system('say "Alert!"')
    else:  # Linux or other
        print('\a')  # Bell character

def show_alert():
    root = tk.Tk()
    root.withdraw()  # Hide the empty window
    messagebox.showwarning("⚠️ ALERT", "Something important just happened!")
    root.destroy()

if __name__ == "__main__":
    play_alert_sound()
    show_alert()
