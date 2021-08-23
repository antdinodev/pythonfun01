#oop for beginners
#tutorial - https://www.youtube.com/watch?v=JeznW_7DlB0
#haro I am vietnamesu programma i'm going to teach you oop in python todayy, let's get started

class Dog:
    def __init__(self,name, age):
        self.name = name
        self.age = age

    #@property #this is called a dunder property, it will let you access the name without using get_name().
    #example d2.getname
    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def add_one(self,x):
        return x +1

    def bark(self):
        print("bark")




d = Dog("Tim")
d2 = Dog("Bill")


print(d.name)
print(d2.name)
print(d2.get_name)
