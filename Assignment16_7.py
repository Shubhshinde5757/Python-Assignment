# Return True number is divisible by 5 ,otherwise False

def ChkDiv(no):
    return no % 5 == 0

num = int(input("Enter Number"))
print(ChkDiv(num))