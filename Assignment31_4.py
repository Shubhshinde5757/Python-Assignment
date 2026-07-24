#Q4. Create a new log file every ten minutes

import schedule
import time
from datetime import datetime

def CreateLog():
    filename = "MarvellousLog_" + datetime.now().strftime("%d_%m_%Y_%H_%M_%S") + ".txt"

    with open(filename, "w") as file:
        file.write("Log file created successfully.\n")
        file.write("Creation Time : " + datetime.now().strftime("%d-%m-%Y %I:%M:%S %p"))

    print(filename, "created.")

schedule.every(1).minutes.do(CreateLog)

while True:
    schedule.run_pending()
    time.sleep(1)