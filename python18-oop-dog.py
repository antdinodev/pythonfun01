class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return print(f"{self.name} is {self.age} years old")

    def speak(self, sound):
        return print(f"{self.name} says {sound}")

class JackRussellTerrier(Dog):
    def speak(self, sound="Arf"):
        return super().speak(sound)

class GoldenRetriever(Dog):
    def speak(self, sound="Bark"):
        return super().speak(sound)

class Dachshund(Dog):
    def speak(self, sound="Wee Wee Wee"):
        return super().speak(sound)

class Bulldog(Dog):
    def speak(self, sound="Grrr"):
        return super().speak(sound)


miles = JackRussellTerrier("Miles", 4)
miles.speak()

bull = Bulldog("Ruffles", 2)
bull.speak()



# In this tutorial, you learned how to:
#source : https://realpython.com/python3-object-oriented-programming/
#
#     Define a class, which is a sort of blueprint for an object
#     Instantiate an object from a class
#     Use attributes and methods to define the properties and behaviors of an object
#     Use inheritance to create child classes from a parent class
#     Reference a method on a parent class using super()
#     Check if an object inherits from another class using isinstance()
