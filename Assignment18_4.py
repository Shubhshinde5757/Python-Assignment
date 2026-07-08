#Accept N numbers and return the frequency of a given number.

def Frequency(arr, no):
    count = 0

    for i in arr:
        if i == no:
            count += 1

    return count

size = int(input("Enter number of elements: "))

data = []
for i in range(size):
    value = int(input("Enter element: "))
    data.append(value)

search = int(input("Enter number to search: "))

print("Frequency:", Frequency(data, search))