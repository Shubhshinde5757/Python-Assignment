# Display pattern.

#1
#1 2
#1 2 3
#1 2 3 4
#1 2 3 4 5


def Pattern(no):
    for i in range(1, no + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()

num = int(input("Enter number: "))
Pattern(num)