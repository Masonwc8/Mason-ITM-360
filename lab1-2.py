import random

class Pet:
    cleanliness_max = 10
    food_reduce = 2
    food_max = 10
    food_warning = 3
    boredom_reduce = 2
    boredom_max = 10
    sounds = ['Tomagotchi!', 'Grrr...']

    def __init__(self, name):
        self.name = name
        self.hygiene = random.randrange(0, self.cleanliness_max + 1)
        self.food = random.randrange(0, self.food_max + 1)
        self.boredom = random.randrange(0, self.boredom_max + 1)
        self.sounds = self.sounds.copy()

    def bathe(self):
        if self.hygiene < self.cleanliness_max:
            self.hygiene += 3
            if self.hygiene > self.cleanliness_max:
                self.hygiene = self.cleanliness_max
        else:
            print(f"{self.name} is annoyed by the unnecessary bathe!")

    def clock_tick(self):
        self.boredom = max(0, self.boredom - self.boredom_reduce)
        self.food = max(0, self.food - 1)

    def reduce_boredom(self):
        self.boredom = max(0, self.boredom - self.boredom_reduce)

    def teach(self, new_word):
        self.sounds.append(new_word)
        self.reduce_boredom()

    def greet(self):
        if self.sounds:
            print(random.choice(self.sounds))
        self.reduce_boredom()

    def feed(self):
        meal = random.randint(self.food, self.food_max)
        self.food = min(self.food_max, meal)

    def mood(self):
        if self.food >= self.food_warning and self.boredom <= self.boredom_max:
            return "Happy"
        elif self.food < self.food_warning:
            return "Hungry"
        else:
            return "Bored"

    def __str__(self):
        return f"{self.name} is {self.mood()}."


class Cat(Pet):
    sounds = ["Meow"]

    def chase_rat(self, rat):
        if rat.lower() == 'yes':
            print(f"{self.name} is chasing a rat!")

    def mood(self):
        if 0 < self.boredom < 3:
            return "Feeling grumpy"
        elif self.boredom >= 3:
            return "Absolutely bored!"
        else:
            return "Randomly annoyed" if random.randint(0, 1) else "Happy"


class Dog(Pet):
    loyalty_max = 10

    def __init__(self, name):
        super().__init__(name)
        self.loyalty = random.randint(0, self.loyalty_max + 1)

    def fetch_ball(self):
        print(f"{self.name} is happily fetching the ball!")


# Create instances
pet_instance = Pet("Fluffy")
cat_instance = Cat("Whiskers")
dog_instance = Dog("Buddy")

# Call methods in different classes
pet_instance.feed()
cat_instance.chase_rat('no')
dog_instance.fetch_ball()

# Print status
print(pet_instance)
print(cat_instance)
print(dog_instance)