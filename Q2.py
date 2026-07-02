# 2 Print all factors of a number

def Factors(no):
    for i in range(1, no + 1):
        if no % i == 0:
            print(i, end=" ")

def main():
    num = int(input("Enter a number: "))
    Factors(num)

if __name__ == "__main__":
    main()