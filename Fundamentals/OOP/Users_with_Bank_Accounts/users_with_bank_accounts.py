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


class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0
        self.account = BankAccount()

    def display_info(self):
        print(f"{self.first_name}, {self.last_name}, {self.email}, {self.age}")
        return self

    def enroll(self):
        if(self.is_rewards_member == True):
            print("User already a member")
        else:
            self.is_rewards_member = True
            self.gold_card_points = 200
        return self

    def spend_points(self, amount):
        if(amount > self.gold_card_points):
            print("Not enough points")
        else:
            self.gold_card_points -= amount
        return self

    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self

    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
        return self

    def display_user_balance(self):
        self.account.display_account_info()


john = User("John", "Smith", "john.smith@email.com", 30)
david = User("David", "Johnson", "david.johnson@email.com", 25)
michael = User("Michael", "Myers", "mmslasher@email.com", 73)

john.make_deposit(100).make_withdrawal(25).display_user_balance()