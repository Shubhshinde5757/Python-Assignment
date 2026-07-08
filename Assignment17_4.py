# Return Addition of factors a number 

def AddFactors(no):
    total = 0
    for i in range(1, no):
        if no % i == 0:
            total +=i
    return total

num =  int(input("Enter number: "))
print("Addition of factor :", AddFactors(num))
