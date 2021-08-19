class notOOP:
    pass

class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '_$company.com'

    def fullname(self):
        return '{} {}'.format(self.first,self.last)



emp_1 = notOOP()
emp_2 = notOOP()

print(emp_1)
print(emp_2)

emp_1.first = '_Corey_'
emp_1.last = 'Schafer'
emp_1.email = 'Corey.Schafer@company.com'
emp_1.pay = 50000

emp_2.first = 'Test'
emp_2.last = 'User'
emp_2.email = 'Test.User@company.com'
emp_2.pay = 60000

print(emp_1.email)
print(emp_2.email)





#let's try the oop version

emp_1 = Employee('Corey', 'ShankYou', 500000)
emp_2 = Employee('Melissa', 'Perexa', 60000)

print(emp_1)
print(emp_2)

print(f"name: {emp_1.first} {emp_1.last} pay: {emp_1.pay}")
print(f"name: {emp_2.first} {emp_2.last} pay: {emp_2.pay}")

print(emp_2.fullname())
