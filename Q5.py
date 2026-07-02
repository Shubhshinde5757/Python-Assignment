# 5 Print numbers from N to 1 (Reverse Order)
def DisplayReverse(no):
    for i in range(no, 0, -1):
        print(i, end=" ")

def main():
    num = int(input("Enter a number: "))
    DisplayReverse(num)

if __name__ == "__main__":
    main()