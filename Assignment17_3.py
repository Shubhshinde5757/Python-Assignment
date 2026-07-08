# Return factorial of a number

def Faactorial(no):
    fact = 1
    for i in range(1, no +1):
        fact *=1
    return fact

num = int(input("Enter number: "))
print("Factorial:",Faactorial(num))