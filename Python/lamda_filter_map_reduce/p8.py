from functools import reduce

num = [1,2,3,4,5,6,7,8,9,0]
num1 = int(input())

# Converting a given number to a cube number
cube_numbers= lambda x:x**3
print(cube_numbers(num1))

# Converting cube numbers with lambda and map 
cube_number = list(map(lambda y:y**3,num))
print(cube_number)

# Getting the square values from the dictionary using filter with lambda 
find_square = list(filter(lambda n: int(n ** 0.5) ** 2 == n, num))
print(find_square)

# Getting the sum of all squares values from the list using lamba and reduce
# Imported the functools package for using reduce function
sum_of_squares = reduce(lambda x, y: x + y**2, num, 0)
print(sum_of_squares)

# Getting the sum of all cubes values from the list using lamba and reduce
# Imported the functools package for using reduce function
sum_of_cubes = reduce(lambda x, y: x + y**3, num, 0)
print(sum_of_cubes)


