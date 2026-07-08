#Return addition of digits of a number.

def SumDigits(no):
    total = 0

    while no > 0:
        digit = no % 10
        total += digit
        no //= 10

    return total

num = int(input("Enter number: "))
print("Addition of digits:", SumDigits(num))