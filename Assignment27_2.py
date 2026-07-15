# Write a Python program to implement a class named BankAccount.

class BankAccount:
    ROI = 10.5

    def __init__(self, Name, Amount):
        self.Name = Name
        self.Amount = Amount

    def Display(self):
        print("Name:", self.Name)
        print("Balance:", self.Amount)

    def Deposit(self):
        amt = float(input("Enter amount to deposit: "))
        self.Amount += amt

    def Withdraw(self):
        amt = float(input("Enter amount to withdraw: "))
        if amt <= self.Amount:
            self.Amount -= amt
        else:
            print("Insufficient Balance")

    def CalculateInterest(self):
        Interest = (self.Amount * BankAccount.ROI) / 100
        print("Interest:", Interest)


Obj1 = BankAccount("Shubham", 10000)

Obj1.Display()
Obj1.Deposit()
Obj1.Withdraw()
Obj1.CalculateInterest()
Obj1.Display()