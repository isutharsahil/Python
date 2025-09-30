class Account:
    def __init__(self, account, balance):
        self.account_no = account
        self.balance = balance

    def credit(self, amount):
        self.balance += amount
        print("Amount Credited 🟢 Rs:  ",amount)
        print("Total balance is ------> Rs: ",self.get_balance())
        
    def debit(self, amount):
        self.balance -= amount
        print("Amount debited 🔴 Rs: ",amount)
        print("Total balance is ------> Rs: ",self.get_balance())

    def get_balance(self):
        return self.balance


acc1 = Account(9587018188, 10000)
acc1.debit(1000)
acc1.credit(500)        
acc1.debit(950)