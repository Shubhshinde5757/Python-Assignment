# 3.Print the sum of digits
def SumDigits(no):
    total = 0

    while no > 0:
        digit = no % 10
        total += digit
        no = no // 10

    print("Sum =", total)

def main():
    num = int(input("Enter a number: "))
    SumDigits(num)

if __name__ == "__main__":
    main()