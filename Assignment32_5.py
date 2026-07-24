#Q5. Delete all empty files recursively every hour

import os
import schedule
import time

directory = input("Enter directory: ")

def DeleteEmptyFiles():

    logfile = open("DeletedFilesLog.txt", "a")

    for foldername, subfolders, filenames in os.walk(directory):

        for file in filenames:

            filepath = os.path.join(foldername, file)

            try:
                if os.path.getsize(filepath) == 0:
                    os.remove(filepath)
                    logfile.write(filepath + " deleted\n")
                    print(filepath, "deleted")

            except PermissionError:
                print("Permission denied:", filepath)

    logfile.close()

schedule.every().seconds.do(DeleteEmptyFiles)

while True:
    schedule.run_pending()
    time.sleep(1)