# 2.Count the digits in a number
def CountDigits(no):
    count = 0

    while no > 0:
        no = no // 10
        count += 1

    print("Count =", count)

def main():
    num = int(input("Enter a number: "))
    CountDigits(num)

if __name__ == "__main__":
    main()