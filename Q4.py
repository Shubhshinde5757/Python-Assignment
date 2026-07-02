# 4 Print numbers from 1 to N
def Display(no):
    for i in range(1, no + 1):
        print(i, end=" ")

def main():
    num = int(input("Enter a number: "))
    Display(num)

if __name__ == "__main__":
    main()