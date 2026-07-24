#4. Create a task that executes every day at 9:00 AM

import schedule
import time

def greet():
    print("Namaskar...")

schedule.every().day.at("09:00").do(greet)

while True:
    schedule.run_pending()
    time.sleep(1)