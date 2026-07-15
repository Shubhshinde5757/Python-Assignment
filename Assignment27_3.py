# Write a Python program to implement a class named Numbers.

class Numbers:

    def __init__(self, Value):
        self.Value = Value

    def ChkPrime(self):
        if self.Value < 2:
            return False
        for i in range(2, self.Value):
            if self.Value % i == 0:
                return False
        return True

    def ChkPerfect(self):
        total = 0
        for i in range(1, self.Value):
            if self.Value % i == 0:
                total += i
        return total == self.Value

    def Factors(self):
        print("Factors are:")
        for i in range(1, self.Value + 1):
            if self.Value % i == 0:
                print(i, end=" ")
        print()

    def SumFactors(self):
        total = 0
        for i in range(1, self.Value):
            if self.Value % i == 0:
                total += i
        return total


Obj1 = Numbers(int(input("Enter Number: ")))

print("Prime:", Obj1.ChkPrime())
print("Perfect:", Obj1.ChkPerfect())
Obj1.Factors()
print("Sum of Factors:", Obj1.SumFactors())