class BankAccount:

    all_accounts = []

    def __init__(self, int_rate = 0.01, balance = 0):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if(self.balance < amount):
            print("Insufficient Funds: Charging a $5 fee")
            self.balance -= 5
        else:
            self.balance -= amount
        return self

    def display_account_info(self):
        print(f"Balance: {self.balance}")
        return self

    def yield_interest(self):
        if(self.balance < 0):
            print("No balance to yield interest")
        else:
            self.balance += (self.balance * self.int_rate)
        return self

    @classmethod
    def get_account_info(cls):
        for account in cls.all_accounts:
            account.display_account_info()


checking = BankAccount()
saving = BankAccount(0.05)

checking.deposit(100).deposit(100).deposit(100).withdraw(50).yield_interest().display_account_info()

saving.deposit(200).deposit(200).withdraw(25).withdraw(25).withdraw(50).withdraw(75).yield_interest().display_account_info()

# BONUS
BankAccount.get_account_info()