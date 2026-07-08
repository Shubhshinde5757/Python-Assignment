# Create two threads named Thread1 and Thread2
import threading

def Thread1():
    print("Numbers from 1 to 50")
    for i in range(1, 51):
        print(i)


def Thread2():
    print("Numbers from 50 to 1")
    for i in range(50, 0, -1):
        print(i)


t1 = threading.Thread(target=Thread1, name="Thread1")
t2 = threading.Thread(target=Thread2, name="Thread2")

t1.start()
t1.join()      # Wait until Thread1 completes

t2.start()
t2.join()

print("Exit from main")