#6. Schedule the following tasks
#Print Lunch Time! every day at 1:00 PM
#Print Wrap up work every day at 6:00 PM
import schedule
import time

def lunch():
    print("Lunch Time!")

def wrap_up():
    print("Wrap up work")

schedule.every().day.at("13:00").do(lunch)
schedule.every().day.at("17:00").do(wrap_up)

while True:
    schedule.run_pending()
    time.sleep(1)