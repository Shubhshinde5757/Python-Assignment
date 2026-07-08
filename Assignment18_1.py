# Accept the number and return the addition of all element 

def SumList(arr):
    total = 0
    for i in arr:
        total += i
    return total

size = int(input("Enter element: "))

data = []
for i in range (size):
    value = int(input("Enter element: "))
    data.append(value)
    
print("Addition:",SumList(data))