import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import pyautogui
import time
import threading
import random

def type_text(text, wpm):
    words = text.split()
    num_words = len(words)
    total_time = (num_words / wpm) * 60  # Total time in seconds
    avg_delay = total_time / len(text)   # Average delay between characters

    total_chars = len(text)
    progress['maximum'] = total_chars

    # Simulate typing with random delays and occasional pauses
    for i, char in enumerate(text):
        pyautogui.typewrite(char)

        # Update the progress bar
        progress['value'] = i + 1
        root.update_idletasks()

        # Random delay around the average delay
        delay = random.uniform(avg_delay * 0.5, avg_delay * 1.5)
        time.sleep(delay)

        # Introduce an occasional pause every 5 to 15 characters
        if i % random.randint(5, 15) == 0 and i != 0:
            pause = random.uniform(0.5, 2.0)  # Pause between 0.5 to 2 seconds
            time.sleep(pause)

def start_typing():
    # Retrieve text from the text widget
    text = text_input.get("1.0", tk.END).strip()
    # Retrieve WPM from the entry widget
    wpm_value = wpm_input.get()

    # Validate inputs
    if not text:
        messagebox.showerror("Error", "Please enter the text to type.")
        return
    if not wpm_value.isdigit():
        messagebox.showerror("Error", "Please enter a valid WPM (integer).")
        return

    wpm = int(wpm_value)

    # Update status
    status_label.config(text="You have 5 seconds to focus on the target window...")
    root.update()

    # Wait for the user to focus the target window
    time.sleep(5)

    # Start typing
    status_label.config(text="Typing in progress...")
    root.update()
    type_text(text, wpm)
    status_label.config(text="Typing completed.")
    progress['value'] = 0  # Reset progress bar

def start_typing_thread():
    threading.Thread(target=start_typing).start()

# Create the main application window
root = tk.Tk()
root.title("Typing Simulator")

# Text Input Field
text_label = tk.Label(root, text="Enter Text to Type:")
text_label.pack()
text_input = tk.Text(root, height=10, width=50)
text_input.pack()

# WPM Input Field
wpm_label = tk.Label(root, text="Words Per Minute (WPM):")
wpm_label.pack()
wpm_input = tk.Entry(root)
wpm_input.pack()

# Start Button
start_button = tk.Button(root, text="Start Typing", command=lambda: start_typing_thread())
start_button.pack(pady=10)

# Status Label
status_label = tk.Label(root, text="")
status_label.pack()

# Progress Bar
progress = ttk.Progressbar(root, orient='horizontal', length=400, mode='determinate')
progress.pack(pady=10)

# Run the main loop
root.mainloop()