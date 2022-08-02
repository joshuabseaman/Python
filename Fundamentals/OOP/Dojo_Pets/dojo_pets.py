class Ninja:

    def __init__(self, first_name, last_name, treats, pet_food, pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet

    def walk(self):
        self.pet.play()
        print(f"Health is now: {self.pet.health}")
        return self

    def feed(self):
        self.pet.eat()
        print(f"Energy is now: {self.pet.energy}")
        print(f"Health is now: {self.pet.health}")
        return self

    def bathe(self):
        self.pet.noise()
        return self


class Pet:

    def __init__(self, name, type, tricks):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = 100
        self.energy = 100

    def sleep(self):
        self.energy += 25
        return self

    def eat(self):
        self.energy += 5
        self.health += 10
        return self

    def play(self):
        self.health += 5
        return self

    def noise(self):
        print("Pet is making a very strange sound")
        return self


my_treats = ["Sausage", "Bacon", "Turkey"]
my_pet_food = ["Pizza", "Burger"]

sensei = Pet("Sensei", "Doggo", ["Sit", "Shake", "Play Dead"])

ninja = Ninja("Bruce", "Lee", my_treats, my_pet_food, sensei)


ninja.feed().walk().bathe()