# Count Prime Numbers Between 1 and N using.map()

import multiprocessing 

def count_primes(n):
    count = 0
    
    for num in range(2, n + 1):
        
        prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                prime = False
                break
        if prime:
            count += 1
    return (n, count)
    
if __name__ == "__main__":
    numbers = [10000, 20000, 30000, 40000]
    
    with multiprocessing.Pool() as pool:
        result = pool.map(count_primes, numbers)
        
    print("Prime Count:")
    for n, count in result:
        print(f"Primes between 1 and {n} = {count}")