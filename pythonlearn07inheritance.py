class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)



class HotPepper:
  def __init__(self, name, level):
    self.name = name
    self.level = level

  def printname(self):
    print(self.name, self.level)

  def printspicyness(self):
    print(f"This {self.name} has a spiciness level of: {self.level}")

class Hotness(HotPepper):
  def __init__(self, name, level):
    super().__init__(name, level)

x = Student("Mike", "Olsen")
x.printname()


n = Student("bob", "computer science teacher")
n.printname()


a = HotPepper('Ghost Pepper', 'Extremely Hot')
a.printspicyness()


a = Hotness('Ghost Pepper', 'Extremely Extremely 5000 Hot')
a.printspicyness()



print(help(Hotness))