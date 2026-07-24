import schedule
import time
import shutil
from datetime import datetime

source = "sample.txt"
destination = "."

def backup():
    backup_name = "backup_" + datetime.now().strftime("%Y_%m_%d_%H_%M_%S") + ".txt"

    shutil.copy(source, backup_name)

    with open("backup_log.txt", "a") as log:
        log.write("Backup completed successfully at " +
                  datetime.now().strftime("%d-%m-%Y %I:%M:%S %p") +
                  "\n")

    print("Backup Created:", backup_name)

schedule.every().hour.do(backup)

while True:
    schedule.run_pending()
    time.sleep(1)