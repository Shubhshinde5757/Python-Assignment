#1. Print "Jay Ganesh..." every 2 seconds

import schedule
import time

def display():
    print("Jay Ganesh...")

schedule.every(2).seconds.do(display)

while True:
    schedule.run_pending()
    time.sleep(1)