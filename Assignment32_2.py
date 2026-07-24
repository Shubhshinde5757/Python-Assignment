#Q2. Monitor the size of a specified file every 30 seconds

import os
import schedule
import time
from datetime import datetime

filename = input("Enter file name: ")

def FileSize():
    if os.path.exists(filename):
        size = os.path.getsize(filename)

        with open("FileSizeLog.txt", "a") as file:
            file.write("File : " + filename + "\n")
            file.write("Size : " + str(size) + " bytes\n")
            file.write("Date : " + datetime.now().strftime("%d-%m-%Y %I:%M:%S %p") + "\n\n")

        print("Size:", size, "bytes")
    else:
        print("File does not exist.")

schedule.every(30).seconds.do(FileSize)

while True:
    schedule.run_pending()
    time.sleep(1)