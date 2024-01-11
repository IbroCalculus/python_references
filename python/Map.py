
#Map function applies a function to each item in an iterable (ie, lists, tuples etc)
#Check all 4 examples for better understanding

#map(function, iterable)
#map(int, iterable) <----- Convert every element in the iterable to an int data type
#map(len, names) <----- Get the length of every element in the iterable

list_of_nums = [2,3,4,5,6,7,8,8]
square_func = lambda z: z**2
square_value = map(square_func, list_of_nums)
#print(list(square_value))

print('\n=============')

for i,j in zip(list_of_nums, square_value):
    print(f'{i} -- {j}')


# More examples (1) ============================

x = [2,3,4,5,6,7]

calc_func = lambda  x : 2*(x**2)

def calc_func1(x):
  return 3*(x**2)

square_of_lists = map(calc_func1, x)

print(f'The returned mapped lists are: {list(square_of_lists)}')


# More examples (2) ===========================

x = [(2,3),(4,5),(6,7)]

calc_func = lambda  x : 2*(x[0]) +x[1]**3

def calc_func1(x):
  return 3*(x[0]) + x[1]**2

square_of_lists = map(calc_func1, x)

print(f'The returned mapped lists are: {list(square_of_lists)}')


# More examples (3) ===========================

contacts = [
  ("Ibrahim","Musa",27),
  ("James","Achimugu",56),
  ("Kolo","Ahmad",31),
  ("Phil","Johnson",45),
  ("Kabir","Aliyu",29)
]

# FirstName: Ibrahim, Surname: Musa, Age: 27

def toIterable(x):
  return f'FirstName: {x[0]}, Surname: {x[1]}, Age: {x[2]}'

toIterable2 = lambda x: f'Surname: {x[1]}, Age: {x[2]}, FirstName: {x[0]}'

output = map(toIterable2, contacts)
for i in list(output):
  print(i, end="\n")


# More examples (4) ===========================
num1 = [1,2,3,4,5]
num2 = [10,9,8,7,6]

def multiPly(x,y):
  return f'The product of {x} and {y} is {x*y}'

toIterable = map(multiPly, num1, num2)

for i in list(toIterable):
  print(i, end='\n')