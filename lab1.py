# Looks like a lot is missing in the file; please double check the starting python file for details.
import random

class Pet:
    # missing 3 class attributes: -6 points
    food_reduce = 2
    food_warning = 3
    boredom_max = 10
    sounds = ["Tomagotchi!","Grrr...."]

    def __init__(self, name):
        # missing food and boredom variables: -6 points
        self.name = name
        self.food = random.randint(0, self.food_reduce * 5)  # Random initial food level
        self.sounds = Pet.sounds

    # missing bathe and greet methods: -12 points
    
    def clock_tick(self):
        self.boredom_max += 1
        self.food = max(0, self.food - Pet.food_reduce)

    def greet(self):
        print(random.choice(self.sounds))

    def feed(self):
        meal = random.randint(self.food, self.food + Pet.food_reduce * 3)
        self.food = min(meal, self.food_reduce * 5)

    def mood(self):
        if self.food >= Pet.food_warning and self.boredom_max <= Pet.boredom_max:
            return "Happy"
        elif self.boredom_max < 3:
            return "Feeling grumpy"
        elif self.boredom_max > 7:
            return "Absolutely bored!"
        else:
            return "Randomly annoyed"

# Example usage:
pet_name = input("Enter your pet's name: ")
my_pet = Pet(pet_name)

for _ in range(5):
    my_pet.clock_tick()
    my_pet.greet()
    my_pet.feed()
    print(f"{my_pet.name}'s mood: {my_pet.mood()}")
    

class Dog(Pet): #I made it a dog customization because I have dogs at home and wanted my game to feature a dog.
    def __init__(self, name, loyalty_factor=5):
        super().__init__(name)
        self.loyalty_factor = loyalty_factor

    def fetch(self):
        if self.boredom_max < 5:
            return f"{self.name} happily fetched the ball!"
        else:
            return f"{self.name} is too bored to fetch."


dog_name = input("Enter your dog's name: ")
my_dog = Dog(dog_name, loyalty_factor=8)

for _ in range(3):
    my_dog.clock_tick()
    my_dog.greet()
    my_dog.feed()
    print(f"{my_dog.name}'s mood: {my_dog.mood()}")
    print(my_dog.fetch())

cat_instance = Pet("Whiskers")
dog_instance = Dog("Buddy", loyalty_factor=9)

class Cat(Pet):
    sounds = "Meow"

    def chase_rat(self, rat):
        if rat.lower() == 'yes':
            print(f"{self.name} is chasing a rat!")

    def mood(self):
        if self.food >= Pet.food_warning and 0 < self.boredom_max < 3:
            return "Happy"
        elif self.boredom_max < 3:
            return "Feeling grumpy"
        elif self.boredom_max > 7:
            return "Absolutely bored!"
        else:
            return "Randomly annoyed"

# Example usage:
cat_name = input("Enter your cat's name: ")
my_cat = Cat(cat_name)

for _ in range(3):
    my_cat.clock_tick()
    my_cat.greet()
    my_cat.feed()
    print(f"{my_cat.name}'s mood: {my_cat.mood()}")

rat_input = input("Is there a rat? (yes/no): ")
my_cat.chase_rat(rat_input)


for _ in range(2):
    cat_instance.clock_tick()
    cat_instance.greet()
    cat_instance.feed()
    print(f"{cat_instance.name}'s mood: {cat_instance.mood()}")

    dog_instance.clock_tick()
    dog_instance.greet()
    dog_instance.feed()
    print(f"{dog_instance.name}'s mood: {dog_instance.mood()}")
    print(dog_instance.fetch())
