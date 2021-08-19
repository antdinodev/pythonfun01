# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

#fun python
#learn for fun
#fun projects
#https://www.youtube.com/watch?v=1F_OgqRuSdI&list=PL0-84-yl1fUnRuXGFe_F7qSH1LEnn9LkW
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

    x = 50+50-25*0+2+2
    print(x)

    print("Python 2 hour rush")

    price = 10
    price = 20
    rating = 4.9
    name = 'Mosh'
    is_published = False
    is_published = True

    print(price)


    full_name = 'John Smith'
    age = 20
    is_new = True

    name = input('What is your name?\n')
    favorite_color = input('What is your favorite color?\n')
    print('Hi ' + name + "I like " + favorite_color + " too!")

    birth_year = input('Birth Year: ')
    #this gives error age = 2019 - birth_year
    age = 2019 - int(birth_year)

    #convert string to int() float() bool()
    print(type(age))
    print(age)


    weight_lbs = input("Weight (lbs): ")
    #error weight_kg = weight_lbs * 0.45
    weight_kg = float(weight_lbs) * 0.45
    print(weight_kg)






# See PyCharm help at https://www.jetbrains.com/help/pycharm/


