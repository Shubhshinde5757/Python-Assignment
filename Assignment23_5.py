#Factorial of Multiple Numbers
import multiprocessing
import os
import math

def factorial_number(n):
    return (os.getpid(), n, math.factorial(n))

if __name__ == "__main__":
    data = [10, 15, 20, 25]

    with multiprocessing.Pool() as pool:
        result = pool.map(factorial_number, data)

    for pid, num, fact in result:
        print("Process ID :", pid)
        print("Input Number :", num)
        print("Factorial :", fact)
        print()