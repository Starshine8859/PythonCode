import tkinter as tk
from tkinter import ttk
import threading
import time

# Simulated data loading function
def load_data(progress_label):
    for i in range(5):
        time.sleep(1)
        progress_label.config(text=f"Loading... {'.' * ((i % 3) + 1)}")
    progress_label.config(text="✅ Done loading!")

def start_loading():
    # Run load_data in a separate thread so the GUI stays responsive
    threading.Thread(target=load_data, args=(progress_label,), daemon=True).start()

# Create the main dashboard window
root = tk.Tk()
root.title("Python Dashboard")
root.geometry("300x150")

# Label and button
title_label = tk.Label(root, text="📊 Dashboard", font=("Helvetica", 16))
title_label.pack(pady=10)

progress_label = tk.Label(root, text="", font=("Helvetica", 12))
progress_label.pack()

load_button = ttk.Button(root, text="Start Loading", command=start_loading)
load_button.pack(pady=10)

root.mainloop()
