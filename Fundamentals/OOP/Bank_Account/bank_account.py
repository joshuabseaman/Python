class BankAccount():

    all_accounts = []

    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate = 0.01, balance = 0):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)
        # your code here! (remember, instance attributes go here)
        # don't worry about user info here; we'll involve the User class soon

    def deposit(self, amount):
        self.balance += amount
        return self
        # your code here

    def withdraw(self, amount):
        if (self.balance < amount):
            print("Insufficient funds: Charging a $5 fee.")
            self.balance -= 5
        else:
            self.balance -= amount
        return self
        # your code here

    def display_account_info(self):
        print(f"Balance: {self.balance}")
        return self
        # your code here

    def yield_interest(self):
        if (self.balance < 0):
            print("No balance")
        else:
            self.balance = (self.balance * self.int_rate) + self.balance
        return self
        # your code here

    @classmethod
    def get_account_info(cls):
        for account in cls.all_accounts:
            account.display_account_info()

    @classmethod
    def all_balances(cls):
        sum = 0
        for account in cls.all_accounts:
            sum += account.balance
        print(f"All balances = {sum}")


checking = BankAccount()
saving = BankAccount(0.05)

checking.deposit(100).deposit(100).deposit(100).withdraw(50).yield_interest().display_account_info()

saving.deposit(200).deposit(200).withdraw(25).withdraw(25).withdraw(50).withdraw(75).yield_interest().display_account_info()

# Bonus
BankAccount.get_account_info()

BankAccount.all_balances()
