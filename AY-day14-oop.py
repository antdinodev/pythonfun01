#day 14 of Angela Yu's Python Notes
#let's review this oop stuff for fun
#keep learning for fun, don't spend too much time trying to get a job- you need more porjects for fun!! jobs will distract you from this
#keep in mind that learning this is for fun, and also don't expect to get a job offer
#we are programers we make our own jobs :)

import another_module

print(another_module.another_variable)

#import turtle
#you can also do this - from turtle import Turtle


#timmy = turtle.Turtle()



#
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color('red')
# timmy.forward(100)
# #for more info see : https://docs.python.org/3/library/turtle.html
# my_screen = Screen()
# print(my_screen.canvwidth)
# my_screen.exitonclick()

#object methods

#prettytable sample
from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])

table.align = "l"
print(table.align)

print(table)