#Create two threads to find Sum and Product of list elements
import threading

Sum = 0
Product = 1

def FindSum(lst):
    global Sum
    Sum = sum(lst)

def FindProduct(lst):
    global Product
    Product = 1
    for i in lst:
        Product *= i

List = list(map(int, input("Enter numbers: ").split()))

t1 = threading.Thread(target=FindSum, args=(List,))
t2 = threading.Thread(target=FindProduct, args=(List,))

t1.start()
t2.start()

t1.join()
t2.join()

print("Sum =", Sum)
print("Product =", Product)

print("Exit from main")