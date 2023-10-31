# Inheritance Override

class Account:
    def __init__(self, name, number, balance): # Special Constructor
        self.acc_name = name
        self.acc_number = number
        self.account_balance = balance

    def deposit(self, amount):
        self.account_balance += amount

    def withdraw(self, amount):
        if amount > self.account_balance:
            print(f"Insufficient Funds. Balance is {self.account_balance}")
        else:
            self.account_balance -= amount

    def __str__(self):
        return f"name: {self.acc_name}, AccNo: {self.acc_number}, Balance {self.account_balance}"


class DollarAccount(Account):
    def rates(self):
        return 153.80

    def deposit(self, amount):
        usd = amount/self.rates()
        self.account_balance += usd

dc1 = DollarAccount("Michael Khanda", "100001", 3200)
dc1.withdraw(800)
print(dc1.account_balance)
print(dc1.rates())
print(dc1)




# acc1 = Account("Jude Nyongesa", "39522626", 30000)
#
# # Depositing into the account
# acc1.deposit(500)
# print("Account Name:", acc1.acc_name)
# print(f"Account Number:{acc1.acc_number}")
# print("Account Balance:", acc1.account_balance)
# print(acc1)



