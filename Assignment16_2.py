# Check Whether a number is even or odd

def ChkNum(no):
    if no % 2 == 0:
        print("Even Number")
    else:
        print("Odd Number")
num = int(input("Enter number: "))
ChkNum(num)