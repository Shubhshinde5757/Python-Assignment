#Q4. Copy all .txt files from one directory to another every ten minutes


import os
import shutil
import schedule
import time

source = input("Enter source directory: ")
destination = input("Enter destination directory: ")

def CopyFiles():

    if not os.path.isdir(source):
        print("Invalid source directory.")
        return

    if not os.path.isdir(destination):
        print("Invalid destination directory.")
        return

    logfile = open("CopyLog.txt", "a")

    for file in os.listdir(source):

        if file.endswith(".txt"):
            src = os.path.join(source, file)
            dest = os.path.join(destination, file)

            try:
                shutil.copy(src, dest)
                logfile.write(file + " copied successfully\n")
            except:
                logfile.write(file + " could not be copied\n")

    logfile.close()
    print("Copy completed.")

schedule.every(1).minutes.do(CopyFiles)

while True:
    schedule.run_pending()
    time.sleep(1)