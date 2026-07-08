# Accept N numbers and return the addition of all prime numbers using MarvellousNum module.

import MarvellousNum

def ListPrime(arr):
    total = 0

    for i in arr:
        if MarvellousNum.ChkPrime(i):
            total += i

    return total

size = int(input("Enter number of elements: "))

data = []
for i in range(size):
    value = int(input("Enter element: "))
    data.append(value)

print("Addition of Prime Numbers:", ListPrime(data))