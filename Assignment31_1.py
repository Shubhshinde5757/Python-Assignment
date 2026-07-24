#Q1. Display a message repeatedly after a specified interval


import schedule
import time

message = input("Enter message: ")
interval = int(input("Enter interval in seconds: "))

if interval <= 0:
    print("Interval must be greater than zero.")
    exit()

def Display():
    print(message)

schedule.every(interval).seconds.do(Display)

while True:
    schedule.run_pending()
    time.sleep(1)