#dunder methods


class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '_$company.com'

    def fullname(self):
        return '{} {}'.format(self.first,self.last)
    #this is a dunder method it has __name__
    def __str__(self):
        return '{} -{}'.format(self.fullname(), self.email)
    #to override add sub or multiply:
    #you define the __add__, __sub__, and __mul__ methods for the class, that's how. Each method takes two objects (the operands of +/-/*)
    # as arguments and is expected to return the result of the computation.

    def __add__(self, other):
        return self.pay + other.pay

    def __sub__(self,other):
        return self.pay - other.pay

    def __mul__(self,other):
        return self.pay * other.pay




emp_1 = Employee('Bob', 'Money', 50000)
emp_2 = Employee('Bob2', 'Money2', 10000)

print(emp_1 + emp_2)
print(emp_1 - emp_2)
#to use this you need to create a dunder method called __mul__
print(emp_1 * emp_2) #notice how this gives an error because we did not override the *

#with dunder methods you can over things and create custom add methods






