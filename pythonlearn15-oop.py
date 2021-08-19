class Dog:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print("bark bark!")

    def bark2(self):
        return 'bark'

    @property
    def display(self):
        print(f"name:{self.name} sound: {self.bark2}")


ozzy = Dog("Ozzy", 2)
print(ozzy.name)
print(ozzy.age)

ozzy.display