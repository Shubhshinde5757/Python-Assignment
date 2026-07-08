#Create two threads to find Maximum and Minimum element
import threading

def Maximum(lst):
    print("Maximum Element =", max(lst))

def Minimum(lst):
    print("Minimum Element =", min(lst))

List = list(map(int, input("Enter numbers: ").split()))

t1 = threading.Thread(target=Maximum, args=(List,))
t2 = threading.Thread(target=Minimum, args=(List,))

t1.start()
t2.start()

t1.join()
t2.join()

print("Exit from main")