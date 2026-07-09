# Count Even number From 1 to N

import multiprocessing 
import os

def count_even(n):
    count = 0
    for i in range(2, n + 1, 2):
        count +=1
    return (os.getpid(), n, count)

if __name__ == "__main__":
    data = [1000000, 2000000, 3000000, 4000000]
    
    with multiprocessing.Pool() as pool:
        result = pool.map(count_even, data)
        
        
    for pid, num, count in result:
        print("Process ID : ", pid)
        print("Input Number :", num)
        print("Even Number Count : ", count)
        print()
                

    