#5. Schedule a task that executes every five minutes and writes the current date and time into a file
import schedule
import time
from datetime import datetime

def write_file():
    with open("Marvellous.txt", "a") as file:
        file.write("Task executed at: " +
                   datetime.now().strftime("%d-%m-%Y %I:%M:%S %p") +
                   "\n")

schedule.every(10).seconds.do(write_file)
while True:
    schedule.run_pending()
    time.sleep(1)