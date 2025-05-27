# This project contains the code to take a screenshot using Python.
# It uses the pyautogui library for screen capturing and tkinter for GUI.
# Make sure to create a virtual environment and install pyautogui before running.

import time  # To add delays
import os  # To create folders and handle file paths
import pyautogui  # To take screenshots
import tkinter as tk  # To build the GUI interface
from datetime import datetime  # To create timestamped filenames


# Define the function that takes a screenshot when called
def take_screenshot():
    root.withdraw()  # Hide the GUI window so it doesn't appear in the screenshot
    time.sleep(2)  # Wait for 2 seconds to give the user time to set up the screen

    # Define the folder where screenshots will be stored
    folder = "Screenshots"

    # If the folder doesn't exist, create it
    if not os.path.exists(folder):
        os.makedirs(folder)

    # Generate a timestamp for the filename (like 20250527_154210)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    # Use the timestamp to create a unique, readable filename
    filename = f"Screenshot_{timestamp}.png"

    # Combine folder and filename to get the full path
    filepath = os.path.join(folder, filename)

    # Take the screenshot and save it directly to the file path
    img = pyautogui.screenshot(filepath)

    # Save the screenshot image again (redundant, but safe)
    img.save(filepath)

    # Show the screenshot using the default image viewer (temporary file might be used here)
    img.show()

    # Show the GUI window again after the screenshot is taken
    root.deiconify()


# Create the main window for the GUI
root = tk.Tk()

# Create a frame to hold the buttons (organizes layout)
frame = tk.Frame(root)
frame.pack()

# Create the "Take Screenshot" button and assign it to call the take_screenshot() function
button = tk.Button(frame, text="Take Screenshot", command=take_screenshot)
button.pack(side=tk.LEFT)  # Place it on the left side of the frame

# Create the "QUIT" button to close the application
close = tk.Button(frame, text="QUIT", command=quit)
close.pack(side=tk.LEFT)  # Place it next to the screenshot button

# Start the GUI event loop (keeps the window running)
root.mainloop()
