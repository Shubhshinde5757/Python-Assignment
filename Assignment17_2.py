#Display the following pattern
# * * * * * 
# * * * * *
# * * * * * 
# * * * * *

def Pattern(no):
    for i in range(no):
        for j in range (no):
            print("*" , end="")
        print()
        
num = int(input("Enter number :"))
Pattern(num)
