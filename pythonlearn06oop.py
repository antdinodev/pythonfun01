class Employee:

    num_of_emps = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '_$company.com'

        Employee.num_of_emps += 1
    def fullname(self):
        return '{} {}'.format(self.first,self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    @classmethod
    def set_raise_amt(cls, amount):
        #receive class as first argument - cls takes in a class, we cannot use class we can use cls
        cls.raise_amt = amount
#how to use python if or
#https://pythonexamples.org/python-if-or/
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

    #create new class to parse new employee from string
    #use ctrl+/ to add in comments to multiple highlighted lines
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    # @classmethod
    # def fromtimestamp(cls, t):
    #     y, m , d , hh , mm ,ss , weekday, jday, dst = _time.localtime(t)
    #     return cls(y, m, d)
    #
    # @classmethod
    # def today(cls, t):
    #     t = _time.time()
    #     return cls.fromtimestamp(t)
    # @classmethod
    # def fromordinal(cls, n):

emp_1 = Employee('Melissa', 'shankyou', 5000)
emp_2 = Employee("Test", 'User', 60000)

print(emp_1.pay)
emp_1.apply_raise() #see if raise is working
print(emp_1.pay)

#how do we access raise amount?
#emp_1.raise_amount
#create a static varible called raise amount inside your class




print(emp_1.raise_amt)
print(Employee.num_of_emps)

#class methods pass self, cls

#static methods dont pass anything

#let's try changing the raise amount to 5%
Employee.set_raise_amt(1.15) #so you can change the raise amount now
print(emp_1.raise_amt)

#split up employee name


emp_str_1 = 'John-Doe-800000'
emp_str_2 = 'Steve-Smith-30000'
emp_str_3 = 'Jane-Doe-90000'
first, last , pay = emp_str_1.split('-')
# new_emp_1 = Employee(first, last ,pay)

#try again using the class method from the oop creation of Employee
new_emp_1 = Employee.from_string(emp_str_1)
print(new_emp_1.fullname())



import datetime

my_date = datetime.date(2016, 7, 11)
print(Employee.is_workday(my_date))


#summary regular and class methods
#static methods dont operate within the instance of the class

#youtube tutorial https://www.youtube.com/watch?v=rq8cL2XMM5M