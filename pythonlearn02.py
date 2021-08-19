
#https://www.youtube.com/watch?v=_uQrJ0TkZlc&t=2634s
course = 'Python for Beginners'
print(course.replace('P', 'J'))
print('Python' in course) #will print true or false bool if it matches
#in operator returns a bool if found :true, if not found : false
print(len(course))
print(course.upper())
print(course.lower())
print(course.title())
print(course.find('y')) #returns index of found character


numbers = (1,2,3)
y = numbers[2] #cannot change tuple - error numbers[0] = 10
print(y)


coordinates = (1, 2, 3)
y = coordinates[0] * coordinates [1] * coordinates[2]
print(y)

x = coordinates [0]
y = coordinates [1]
z = coordinates [2]
print(x+y+z)


x, y, z = coordinates
print(x)
print(y)

#this is called unpacking
coordinates = [1,2,3]
x, y, z = coordinates
print(y)

customer = {
    "name": "John Smith",
    "age": 30,
    "is_verified": True

}

print(customer["name"])
print(customer["age"])
print(customer["is_verified"])

print(customer.get("name"))
print(customer.get("names")) #the get value will return in none if it does not find the right key

#add a new key in the customer dictionary
customer["birthdate"] = "Jan 1 1980"
print(customer["birthdate"])

phone = input("Phone: ")
digits_mapping = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four"
}

output = ""
for ch in phone:
    output += digits_mapping.get(ch, "!") + " "

print(output)