"""Classes_Objects"""

""" Python is object-oriented programming, same as C++, JAVA, e.g.,,
    - OOP is easy to be reused, saves computing storage
    - class is the blue print, and the objects are the realizations (instances) of the class
    - class defines the data attributes (variable) and procedures (methods) of the objects
"""

class Customer:
    pass 

def cust_instance():
    cust = Customer()
    return cust 

cust_instance()


#Creating the Dog Class
class Dog: #Capitalized name for classes in Python
    
    def __init__(self, name, age): #Initializing name and age attributes for Dog.
        """ __init__ is an initializer method because it initializes the objects data; it is always executed when a class is created. 
        self parameter is REQUIRED as the first argument in each member method in the class. 
        self is a stand-in for object reference.
        """
        self.name = name  
        self.age = age
        self.treats = "Dental Chews" #set a default value for an attribute

    def sit(self): 
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        print(f"{self.name} is rolling over!")

    def update_treats(self, new_treat):
        self.treats = new_treat


def one_instance(): #Making an instance from a Class
    my_dog = Dog("Ollie", 4)  #self does not need an argument when it is called.
    print(f"My dog's name is {my_dog.name}")
    print(f"My dog's age is {my_dog.age}")
    """
    Notably, .treat doesn't exit in this instance, given update_treats() has not been called.
    """


def second_instance():
    dog_name = input("What's your dog's name?")
    dog_age = int(input("How old is your dog?"))
    your_dog = Dog(dog_name, dog_age)  
    your_dog.sit()
    your_dog.roll_over()

#To update an attribute's default value, either through a method or direct assignment
def third_instance():
    my_dog = Dog("Ollie", 4)
    my_dog.update_treats("Apple") #through a method
    print(f"{my_dog.name} loves {my_dog.treats}")

""" Design Classes 
    - Class
    - Data Attributes - nouns
    - Methods - actions
    
In the Dog class case: 
    - Dog
    - Name, AGE
    - sit(), roll_over()
"""

# In-class exercises: 
"""
Make a class called Restaurant with two attributes, restaurant_name and cuisine_type. 
Make a method called describe_restaurant() that prints these two pieces of information,
and another method called open_restaurant() that prints a message indicating that the 
restaurant is open.

Make 3 instances of the class, print two attributes individually and then call the two methods.
"""

class Restaurant:
    
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant (self):
        print (f"{self.restaurant_name} is a {self.cuisine_type} restuaurant.")

    def open_restaurant (self):
        print (f"{self.restaurant_name} is open!")

def first_instance ():
    my_restaurant = Restaurant ("Culvers","Fast Food")
    print(f"The restaurant's name is {my_restaurant.restaurant_name}")
    print(f"This restaurant serves {my_restaurant.cuisine_type}")

def second_instance ():
    openRestaurant = Restaurant ("Culvers","Fast Food")
    print (f"The {}")


