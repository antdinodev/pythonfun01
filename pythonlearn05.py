numbers = [99, 100, 500, 2, 100, 300, 405, 700, 100 , 200 ,300 ,400 ,500]
#print(numbers.sort()) #this gives none
numbers.sort()
#numbers.reverse() #sorts in descending orders
print(numbers)


numbers2 = [1,2,3,4,5,6,7,8,100,200,500,400,300]
print(sorted(numbers2))

numbers3 = numbers.copy() #copys the list
numbers.append(10)
print(numbers)
print(numbers3)


#write program to remove duplicate in list
#so we create a new empty list,
#and loop through the numbers list,
#then we write an if statement not in... and append it to the unqiues
numbers = [2, 2, 4, 6, 3, 4, 6, 1]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)

#print out numbers that are duplicates


def checkIfDuplicates_2(listOfElems):
    ''' Check if given list contains any duplicates '''
    setOfElems = set()
    for elem in listOfElems:
        if elem in setOfElems:
            return True
        else:
            setOfElems.add(elem)
    return False

listOfElems = ['Hello', 'Ok', 'is', 'Ok', 'test', 'this', 'is', 'a', 'test']
result = checkIfDuplicates_2(listOfElems)
if result:
    print('Yes, list contains duplicates')
else:
    print('No duplicates found in list')

numbers = [2, 2, 4, 6, 3, 4, 6, 1, 5,5, 6,6, 9,9,9,9, 8]
duplicates = []
for number in numbers:
    if number in duplicates:
        duplicates.append(number)
print(duplicates)


