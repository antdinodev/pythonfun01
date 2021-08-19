matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]

]
print(matrix[0][0])
print(matrix[0][1])
print(matrix[0][2])


print(matrix[1][0])
print(matrix[1][1])
print(matrix[1][2])


print(matrix[2][0])
print(matrix[2][1])
print(matrix[2][2])

#you can also use nesed for loop to print out all items in list using for loop

for row in matrix:
    for item in row:
        print(item)

A = [[1, 4, 5, 12],
    [-5, 8, 9, 0],
    [-6, 7, 11, 19]]

print("A =", A)
print("A[1] =", A[1])      # 2nd row
print("A[1][2] =", A[1][2])   # 3rd element of 2nd row
print("A[0][-1] =", A[0][-1])   # Last element of 1st Row

column = [];        # empty list
for row in A:
  column.append(row[2])

print("3rd column =", column)

column2 = [];        # empty list
for row in A:
  column2.append(row[3])

print("4th column =", column2)


row = [];        # empty list
for column in A:
  row.append(column[0])

print("2nd column =", row)

numbers = [5, 2, 1 , 5 ,7 ,4]
print(numbers.sort()) #this gives none
numbers.sort()
numbers.reverse() #sorts in descending orders
print(numbers)






