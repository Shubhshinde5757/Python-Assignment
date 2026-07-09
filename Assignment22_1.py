# Sum of Squares from 1 to N using Pool,map()


import multiprocessing

def sum_of_squares(n):
    return sum(i * i for i in range(1, n + 1))

if __name__ == "__main__":
    numbers =[100000000, 200000000, 300000000,400000000]
    
    with multiprocessing.Pool()as pool:
        result = pool.map(sum_of_squares, numbers)
    print("Input:",numbers)
    print("output:")
    print(result)
    
    