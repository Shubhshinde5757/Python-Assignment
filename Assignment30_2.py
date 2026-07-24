#2. Display the current date and time every one minute

import schedule
import time
from datetime import datetime

def show_datetime():
    print("Current Date and Time:", datetime.now().strftime("%d-%m-%Y %I:%M:%S %p"))

schedule.every(1).minutes.do(show_datetime)

while True:
    schedule.run_pending()
    time.sleep(1)