MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

#temp code i used to test if i can retrieve the cost dictionary item
#y = MENU['espresso']['cost']
#print(y)

#vending machine requirements
#take input
#do calculations
#display input
#return items

#Function and Variable Names

#Function names should be lowercase,
# with words separated by underscores as necessary to improve readability.

#https://www.python.org/dev/peps/pep-0008/#function-and-variable-names
def calculate_coins(quarters, dimes, nickles, pennies):
    tq = quarters * 25
    td = dimes * 10
    tn = nickles * 5
    tp = pennies * 1
    total = tq+td+tn+tp
    print("You used: " + str(total/100))
    return total/100


selection = str(input("Would you like? (espresso/latte/cappuccino): "))

if selection == "espresso" or selection == "latte" or selection == "cappuccino":
    print("Please insert coins")
    #loop through how many quarters
    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickles = int(input("How many nickles? "))
    pennies = int(input("How many pennies? "))
    total = calculate_coins(quarters,dimes,nickles,pennies)
    #after retreiving input it needs to do the math to make sure it is enough
    #if it is not enough, it will print, mmoney refunded
    if total >= MENU[selection]['cost']:
        change = total-MENU[selection]['cost']
        change_round = str(round(change, 2))
        format_change = ''
        if change > 1:
            format_change = '$' + change_round + ' cents'
        else:
            format_change = change_round + ' cents'

        change = str(change_round)

        print('here is your ' + selection + ' and change!')
        print("Your change is : " + format_change)

    else:
        print("Sorry you don't have enough money!")


elif selection == 'report':
    print('water: ' + str(resources['water']))
    print('milk: ' + str(resources['milk']))
    print('coffee: ' + str(resources['coffee']))

else:
    print("Error detected, please try again")

#if you type in report it will show how much  water, milk, coffee and money there is in the machine

#todo Print out report of resources available

#how to change values in a dictionry
#https://www.w3schools.com/python/gloss_python_change_dictionary_item.asp