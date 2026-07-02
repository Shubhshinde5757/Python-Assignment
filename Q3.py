 # 3 Perform addition, subtraction, multiplication and division
def Arithmetic(no1, no2):
    print("Addition =", no1 + no2)
    print("Subtraction =", no1 - no2)
    print("Multiplication =", no1 * no2)

    if no2 != 0:
        print("Division =", no1 / no2)
    else:
        print("Division not possible")

def main():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    Arithmetic(num1, num2)

if __name__ == "__main__":
    main()