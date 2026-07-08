#Create two threads named Even and Odd

import threading

def Even():
    print("First 10 Even Numbers:")
    for i in range(2, 21, 2):
        print(i)

def Odd():
    print("First 10 Odd Numbers:")
    for i in range(1, 20, 2):
        print(i)

t1 = threading.Thread(target=Even)
t2 = threading.Thread(target=Odd)

t1.start()
t2.start()

t1.join()
t2.join()

print("Exit from main")