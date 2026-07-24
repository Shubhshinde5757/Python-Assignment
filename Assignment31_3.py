#Q3. Scan a specified directory every minute

import os
import schedule
import time
from datetime import datetime

path = input("Enter directory path: ")

if not os.path.exists(path):
    print("Directory does not exist!")
    exit()

def ScanDirectory():
    files = 0
    folders = 0

    for item in os.listdir(path):
        fullpath = os.path.join(path, item)

        if os.path.isfile(fullpath):
            files += 1
        elif os.path.isdir(fullpath):
            folders += 1

    print("\nDirectory Scanned :", path)
    print("Total Files :", files)
    print("Total Subdirectories :", folders)
    print("Scan Time :", datetime.now().strftime("%d-%m-%Y %I:%M:%S %p"))

schedule.every(1).minutes.do(ScanDirectory)

# Run once immediately
ScanDirectory()

while True:
    schedule.run_pending()
    time.sleep(1)