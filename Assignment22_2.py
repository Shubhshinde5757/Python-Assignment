import multiprocessing 
import os
import math

def factorial_number(n):
    return(os.getpid(), n , math.factorial(n))

if __name__ == "__main__":
    numbers=[10, 15, 20, 25]
    
    with multiprocessing.Pool() as pool:
        result = pool.map(factorial_number,numbers)
        
        print("Process ID\tInput\tFactorial")
        for pid,num,fact in result:
            print(f"{pid}\t\t{num}\t{fact}")
            