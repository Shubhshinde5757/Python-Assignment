# 1.Check whether a number is Prime or not
def ChkPrime(no):
    if no <= 1:
        print("Not Prime")
        return

    for i in range(2, no):
        if no % i == 0:
            print("Not Prime")
            return

    print("Prime Number")

def main():
    num = int(input("Enter a number: "))
    ChkPrime(num)

if __name__ == "__main__":
    main()