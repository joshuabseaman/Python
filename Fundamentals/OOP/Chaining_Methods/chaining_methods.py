class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0

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


john = User("John", "Smith", "john.smith@email.com", 30)
# john.display_info()

# john.enroll()
# print(john.is_rewards_member, john.gold_card_points)

david = User("David", "Johnson", "david.johnson@email.com", 25)
michael = User("Michael", "Myers", "mmslasher@email.com", 73)

# john.spend_points(50)
# print(john.gold_card_points)

# david.display_info()
# david.enroll()
# print(david.is_rewards_member, david.gold_card_points)
# david.spend_points(80)
# print(david.is_rewards_member, david.gold_card_points)

# john.display_info()
john.display_info().enroll().spend_points(50).enroll()
print(john.is_rewards_member, john.gold_card_points)
# david.display_info()
david.display_info().enroll().spend_points(80)
print(david.is_rewards_member, david.gold_card_points)
# michael.display_info()
michael.display_info().spend_points(40)
print(michael.is_rewards_member, michael.gold_card_points)

# BONUS
# john.enroll()

# michael.spend_points(40)