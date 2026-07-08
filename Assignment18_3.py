# Accept N numbers and return the minimum number from the list.

def Minimum(arr):
    min_no = arr[0]

    for i in arr:
        if i < min_no:
            min_no = i

    return min_no

size = int(input("Enter number of elements: "))

data = []
for i in range(size):
    value = int(input("Enter element: "))
    data.append(value)

print("Minimum Number:", Minimum(data))