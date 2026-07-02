# 5 Check whether a number is Palindrome or not
def ChkPalindrome(no):
    temp = no
    rev = 0

    while no > 0:
        digit = no % 10
        rev = rev * 10 + digit
        no = no // 10

    if temp == rev:
        print("Palindrome")
    else:
        print("Not Palindrome")

def main():
    num = int(input("Enter a number: "))
    ChkPalindrome(num)

if __name__ == "__main__":
    main()