class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return f"Account owner - {self.owner}\nAccount balance - {self.balance}"

    def deposit(self, x):
        self.balance += x
        print("Deposit Accepted!")

    def withdraw(self, x):
        if self.balance >= x:
            self.balance -= x
            print("Withdraw Accepted!")
        else:
            print("Insufficient Funds!")

owner, sum = input().split()
owner = str(owner)
sum = int(sum)

acc = Account(owner, sum)
print(acc)

acc.deposit(100)
acc.withdraw(101)
acc.withdraw(1000)