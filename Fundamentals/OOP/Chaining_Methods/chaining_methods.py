class User():

    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_memeber = False
        self.gold_card_points = 0

    def display_info(self):
        print(f"{self.first_name}, {self.last_name}, {self.email}, {self.age}")
        return self

    def enroll(self):
        if (self.is_rewards_memeber == True):
            print("Already a member")
        else:
            self.is_rewards_memeber = True
            self.gold_card_points = 200
        return self

    def spend_points(self, amount):
        if (self.gold_card_points < amount):
            print("Not enough points")
        else:
            self.gold_card_points = self.gold_card_points - amount
        return self


john = User("John", "Smith", "john.smith@email.com", 30)
david = User("David", "Johnson", "david.johnson@email.com", 25)
michael = User("Michael", "Myers", "mmslasher@email.com", 73)

john.display_info().john.enroll().john.spend_points(50).david.enroll().david.spend_points(80).john.display_info().david.display_info().michael.display_info().john.enroll().michael.spend_points(40)

# john.enroll()
print(john.is_rewards_memeber, john.gold_card_points)



# john.spend_points(50)
print(john.gold_card_points)

# david.enroll()
print(david.is_rewards_memeber, david.gold_card_points)
# david.spend_points(80)
print(david.is_rewards_memeber, david.gold_card_points)

# john.display_info()
# david.display_info()
# michael.display_info()

# BONUS

# john.enroll()

# michael.spend_points(40)