#Return number of digits in a number.

def CountDigits(no):
    count = 0

    while no > 0:
        count += 1
        no //= 10

    return count

num = int(input("Enter number: "))
print("Number of digits:", CountDigits(num))