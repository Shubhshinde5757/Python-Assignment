# Sum of Even Number from 1 to N

import multiprocessing
import os

def sum_even(n):
    total = 0
    for i in range(2, n + 1, 2):
        total += i
    return(os.getpid(),n, total)

if __name__ =="__main__":
    data = [1000000, 2000000, 3000000, 4000000]
    
    with multiprocessing.Pool()as pool:
        result = pool.map(sum_even, data)
        
    for pid, num, total in result:
        print("Process ID : ",pid)
        print("Input Number : ",num)
        print("Sum of Even Number : ", total)
        print()