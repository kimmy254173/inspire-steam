# Name : Kimberley Gitau
# Date : 19/02/2026
# Program to show objects in python

class Human:
    # First we define the attributes of a human being
    type = "Mammal"
    legs = 2
    brain = True
    warm_blooded = True
    city = "Nairobi"

    # We then create a constructor for the class object
    # The constuctor will be used to create copies of this object
    def __init__(self, name, age):
        self.human_name = name
        self.human_age = age

    def tell_story(self):
        print(f" Hello, I am {self.human_name} Here is a story")
        print("There was once a bot that said hello world")


# Create the humans
Amani = Human("Amani", 18)
Essy = Human("Essy", 20)

# Let the humans created do things
Amani.tell_story()
print("Amani's age is:", Amani.human_age)


# Modify one of the objects, without modifying other objects
print("Essy's location:", Essy.city)
print("Amani's location:", Amani.city)

Essy.city = "Kiambu"

print("Essy's location:", Essy.city)
print("Amani's location:", Amani.city)