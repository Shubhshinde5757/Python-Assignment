# Calculate 1⁵ + 2⁵ + 3⁵ + ... + N⁵ for Multiple Values using Pool.map()
import multiprocessing
import time

def sum_of_powers(n):
    total = 0
    for i in range(1, n + 1):
        total += i ** 5
        return total
    
if __name__ == "__main__":

    numbers = [1000000, 2000000, 3000000, 4000000]
    start_time = time.time()
    with multiprocessing.Pool() as pool:
        result = pool.map(sum_of_powers, numbers)
        
    end_time = time.time()
    
    print("Input : ", numbers)
    print("\nOutput: ")
    for n, ans in zip(numbers, result):
        print(f"Sum of 1^5 + 2^5 + ... + {n}^5 = {ans}")
        
    print("\nTotal Execution Time : ", end_time - start_time, "seconds")