# This script takes a screenshot using Python and saves it in a folder named 'Screenshots'.
# It uses pyautogui for capturing the screen and saves each screenshot with a timestamped filename.

import time                  # Used to add delay before taking the screenshot
import os                    # Used to create folders and work with file paths
import pyautogui             # Library for screen automation (like screenshots)
from datetime import datetime  # Used to generate a readable timestamp for the file name

def take_screenshot():
    print("Taking screenshot in 2 seconds... Please prepare your screen.")
    time.sleep(2)  # Delay to allow the user to set up the screen

    # Folder to save the screenshots
    folder = "Screenshots"
    if not os.path.exists(folder):
        os.makedirs(folder)  # Create the folder if it doesn't exist

    # Create a filename using the current date and time
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"Screenshot_{timestamp}.png"
    filepath = os.path.join(folder, filename)

    # Take the screenshot and save it
    img = pyautogui.screenshot()
    img.save(filepath)
    img.show()

# Run the function
take_screenshot()
