# Count Odd Numbers from 1 to N

import multiprocessing
import os

def count_odd(n):
    count = 0
    for i in range(1, n + 1, 2):
        count += 1
        
    return (os.getpid(), n, count)
if __name__ == "__main__":
    data = [1000000, 2000000, 3000000, 4000000]
    
    with multiprocessing.Pool() as Pool:
        result = Pool.map(count_odd, data)
        
    for pid, num, count in result:
        print("Process ID :", pid)
        print("Input Number : ",num)
        print("Odd Number Count :", count)
        print()