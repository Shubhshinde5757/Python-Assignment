#Q2. Create a function named DisplayMessage(message)

import schedule
import time

message = input("Enter message: ")
interval = int(input("Enter interval in seconds: "))

def DisplayMessage():
    print(message)

schedule.every(interval).seconds.do(DisplayMessage)

while True:
    schedule.run_pending()
    time.sleep(1)