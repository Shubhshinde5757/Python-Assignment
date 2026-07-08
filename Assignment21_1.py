#Create two threads named Prime and NonPrime
import threading

def isPrime(no):
    if no < 2:
        return False
    for i in range(2, int(no**0.5) + 1):
        if no % i == 0:
            return False
    return True

def Prime(lst):
    print("Prime Numbers:")
    for i in lst:
        if isPrime(i):
            print(i)

def NonPrime(lst):
    print("Non-Prime Numbers:")
    for i in lst:
        if not isPrime(i):
            print(i)

List = list(map(int, input("Enter numbers: ").split()))

t1 = threading.Thread(target=Prime, args=(List,), name="Prime")
t2 = threading.Thread(target=NonPrime, args=(List,), name="NonPrime")

t1.start()
t2.start()

t1.join()
t2.join()

print("Exit from main")