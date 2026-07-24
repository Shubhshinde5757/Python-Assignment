#Q6. Schedule weekly messages

import schedule
import time

def MondayTask():
    print("Start your weekly goals")

def WednesdayTask():
    print("Review your weekly progress")

def FridayTask():
    print("Weekly work completed")

schedule.every().monday.at("09:00").do(MondayTask)
schedule.every().wednesday.at("17:00").do(WednesdayTask)
schedule.every().friday.at("19:28").do(FridayTask)

while True:
    schedule.run_pending()
    time.sleep(1)