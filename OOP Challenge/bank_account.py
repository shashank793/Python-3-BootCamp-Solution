class Account():
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance

    def deposite(self,amount):
        self.balance = self.balance+amount
        return print("Deposite Accepted")

    def withdrawl(self,amount):
        if amount <= self.balance:
            self.balance = self.balance - amount
            return print("Withdrawal Accepted")
        else:
            return print("Funds Unavailable!")

    def __str__(self):
        return f"Account owner: {self.owner}\nAccount balance: ${self.balance}"

    def __len__(self):
        return self.balance


acct = Account(owner='Shashank', balance=100)
print(str(acct))
acct.deposite(50)

print(f"Current Account balance: ${len(acct)}")

acct.withdrawl(75)

print(f"Current Account balance: ${len(acct)}")

acct.withdrawl(500)
