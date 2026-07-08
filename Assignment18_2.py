#Accept the N number and return the maximum numner from the lost.

def Maximum(arr):
    max_no =  arr[0]
    
    for i in arr:
        if i > max_no:
            max_no = i 
        
        return max_no
    
size = int(input("Enter number of elements: "))

data=[]
for i in range(size):
    value = int(input("Enter element: "))
    data.append(value)
    
print("Maximum Number:",Maximum(data))