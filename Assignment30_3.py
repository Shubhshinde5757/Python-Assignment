#3. Schedule a function to print "Coding Kar..." every 30 minutes

import schedule
import time

def message():
    print("Coding Kar...")

schedule.every(30).minutes.do(message)

while True:
    schedule.run_pending()
    time.sleep(1)