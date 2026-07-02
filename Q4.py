# 4 Print the reverse of a number
def Reverse(no):
    rev = 0

    while no > 0:
        digit = no % 10
        rev = rev * 10 + digit
        no = no // 10

    print("Reverse =", rev)

def main():
    num = int(input("Enter a number: "))
    Reverse(num)

if __name__ == "__main__":
    main()