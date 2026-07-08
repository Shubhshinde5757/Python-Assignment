#Create two threads named EvenList and OddList
import threading

def EvenList(lst):
    even = []
    s = 0

    for i in lst:
        if i % 2 == 0:
            even.append(i)
            s = s + i

    print("Even Elements:", even)
    print("Sum of Even Elements =", s)

def OddList(lst):
    odd = []
    s = 0

    for i in lst:
        if i % 2 != 0:
            odd.append(i)
            s = s + i

    print("Odd Elements:", odd)
    print("Sum of Odd Elements =", s)

List = [10, 11, 12, 13, 14, 15, 16, 17]

t1 = threading.Thread(target=EvenList, args=(List,))
t2 = threading.Thread(target=OddList, args=(List,))

t1.start()
t2.start()

t1.join()
t2.join()

print("Exit from main")
