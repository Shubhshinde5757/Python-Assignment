#Create three threads named Small, Capital, and Digits
import threading

def Small(str1):
    count = 0
    for ch in str1:
        if ch.islower():
            count += 1

    print("Thread ID :", threading.get_ident())
    print("Thread Name :", threading.current_thread().name)
    print("Lowercase Count :", count)


def Capital(str1):
    count = 0
    for ch in str1:
        if ch.isupper():
            count += 1

    print("Thread ID :", threading.get_ident())
    print("Thread Name :", threading.current_thread().name)
    print("Uppercase Count :", count)


def Digits(str1):
    count = 0
    for ch in str1:
        if ch.isdigit():
            count += 1

    print("Thread ID :", threading.get_ident())
    print("Thread Name :", threading.current_thread().name)
    print("Digit Count :", count)


text = input("Enter a string : ")

t1 = threading.Thread(target=Small, args=(text,), name="Small")
t2 = threading.Thread(target=Capital, args=(text,), name="Capital")
t3 = threading.Thread(target=Digits, args=(text,), name="Digits")

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

print("Exit from main")