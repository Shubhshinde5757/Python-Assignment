#Q5. Accept a directory name and count files every five minutes

import os
import schedule
import time
from datetime import datetime

path = input("Enter directory path: ")

def CountFiles():
    count = 0

    for item in os.listdir(path):
        if os.path.isfile(os.path.join(path, item)):
            count += 1

    with open("DirectoryCountLog.txt", "a") as file:
        file.write("Directory : " + path + "\n")
        file.write("Number of Files : " + str(count) + "\n")
        file.write("Date : " + datetime.now().strftime("%d-%m-%Y %I:%M:%S %p") + "\n\n")

    print("Information saved successfully.")

schedule.every(1).minutes.do(CountFiles)

while True:
    schedule.run_pending()
    time.sleep(1)
    
    
    
    