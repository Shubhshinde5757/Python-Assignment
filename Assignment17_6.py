# Display pattern.

# *
# * *
# * * *
# * * * *
# * * * * *

def Pattern(no):
    for i in range(1, no + 1):
        for j in range(i):
            print("*", end=" ")
        print()

num = int(input("Enter number: "))
Pattern(num)