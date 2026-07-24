#Q3. Read and display the contents of a file every minute

import schedule
import time
import os

filename = input("Enter file name: ")

def ReadFile():
    if not os.path.exists(filename):
        print("File does not exist.")
        return

    if os.path.getsize(filename) == 0:
        print("File is empty.")
        return

    try:
        with open(filename, "r") as file:
            print("\nFile Contents:")
            print(file.read())

    except PermissionError:
        print("Permission denied.")

    except Exception:
        print("Cannot open file.")

schedule.every(1).minutes.do(ReadFile)

while True:
    schedule.run_pending()
    time.sleep(1)