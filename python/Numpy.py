import numpy as np
import matplotlib.pyplot as plt

#NUMPY VS LIST
#1. Less memory
#2. Fast
#3. Convenient


#SINGLE-DIMENSIONAL ARRAY
a = np.array([1,2,3,4])
print(a)

#MULTI-DIMENSIONAL ARRAY
b = np.array([(1,2,3,4),(4,3,2,1)])
print(f'MULTIDEMENSIONAL: {b}')

#MULTI-DIMENSIONAL ARRAY TO SINLE-DIMENSIONAL ARRAY
b = np.array([(1,2,3,4),(4,3,2,1)])
x= b.ravel()
print(f'RAVELED: {x}')

#RANGE SIMILAR TO RANGE IN FOR LOOP
z = np.arange(0, 11, 2)
print(f'THE RANGE LIST IS: {z}')


#Check the dimension of the array, 1 -> single-dimesion, 2 -> Multi-dimension
c = np.array([(1,2,3,4),(4,3,2,1),(14,13,12,11),(24,23,22,21)])
print(f'The the dimension of the array is {c.ndim}')

#Check size in byte of each element in the array
c = np.array([(1,2,3,4),(4,3,2,1),(14,13,12,11),(24,23,22,21)])
print(f'The array element size is {c.itemsize} bytes')

#Check array element data type
d = np.array(['Ibrahim','Suleiman'])
print(f'The array elements data type is {d.dtype}')

#Check size of the array (Number of elements)
c = np.array([(1,2,3,4),(4,3,2,1),(14,13,12,11),(24,23,22,21)])
print(f'The number of elements in the array are {c.size}')

#Check the shape of the array (Row by Column). DIFFERENT if not n X n
e = np.array([(1,2,3,4),(4,3,2,1),(14,13,12,11),(24,23,22,21),(34,33,32,31)])
print(f'The shape of the array is: {e.shape}')
print(f'{e.shape[0]} rows by {e.shape[1]} columns')

#Reshaping an array. i.e 2x6 reshaped to 6x2 AND 4,3
d = np.array([(1,2,3,4,5,6),(7,8,9,10,11,12)])
reshaped = d.reshape(6,2)
reshaped1 = d.reshape(4,3)
print(f'RESHAPED = {reshaped}')
print(F'RESHAPED1 = {reshaped1}')

#slicing elements in array (Similar to list)
d = np.array([(1,2,3,4,5,6),(7,8,9,10,11,12),(13,14,15,16,17,18)])
print(f'SLICE 1 = {d[0, 2:5]}')
print(f'SLICE 2 = {d[1, 2:5]}')
print(f'SLICE 3 = {d[0:, 2:5]}') #All the rows
print(f'SLICE 4 = {d[0:2, 2:5]}') #First 2 rows


#List of values range equally spaced
f = np.linspace(0,2.5, 5) #Returns 5 values of range of values from 0 to 2.5
print(f'LINSPACE VALUE {f}')


#Minimum and Maximum value of arrays
d = np.array([(1,2,3,4,5,6),(7,8,9,10,11,12),(13,14,15,16,17,18)])
minValue = d.min()
maxValue = d.max()
print(f'THE MINIMUM VALUE OF THE NUMPY ARRAY IS: {minValue}')
print(f'THE MAXIMUM VALUE OF THE NUMPY ARRAY IS: {maxValue}')

#Sum of array elements
d = np.array([(1,2,3,4,5,6),(7,8,9,10,11,12),(13,14,15,16,17,18)])
sumValue = d.sum()
print(F'THE SUM OF THE ELEMENTS IN THE NUMPY ARRAY IS: {sumValue}')

#ARITHMETIC OPERATIONS (+,-,*,/) IN NUMPY OCCURS ELEMENT-WISE
a = np.array([(1,2,3), (3,2,1), (10,9,8)])
b = np.array([(7,2,7), (5,1,1), (8,3,2)])
print(f'THE SUM OF THE ARRAYS = {a+b}')


#Axis in arrays. ROWS = axis1, COLUMNS= axis 0
d = np.array([(1,2,3,4,5,6),(7,8,9,10,11,12),(13,14,15,16,17,18)])
rowSum = d.sum(axis= 1)
columnSum = d.sum(axis= 0)
print(f'THE SUM OF ELEMENTS IN THE ROWS = {rowSum}')
print(f'THE SUM OF ELEMENTS IN THE COLUMN = {columnSum}')


#SQUARE ROOT OF ELEMENTS IN A NUMPY ARRAY
d = np.array([(1,2,3,4,5,6),(7,8,9,10,11,12),(13,14,15,16,17,18)])
print(f'THE SQUARE ROOT OF ELEMENTS IN THE ARRAY ARE: {np.sqrt(d)}')

#STANDARD DAVIATION OF AN ARRAY
d = np.array([(1,2,3,4,5,6),(7,8,9,10,11,12),(13,14,15,16,17,18)])
print(f'THE STANDARD DEVIATON OF ELEMENTS IN THE ARRAY ARE: {np.std(d)}')



#CONCATINATING ARRAYS; HORIZONTAL STACKING AND VERTICAL STACKING
a = np.array([(1,2,3), (3,2,1), (10,9,8)])
b = np.array([(7,2,7), (5,1,1), (8,3,2)])

hStack = np.hstack((a,b))
vStack = np.vstack((a,b))

print(f'HORIZONTAL STACK: {hStack}')
print(f'VERTICAL STACK: {vStack}')


#SPECIAL FUNCTIONS
#SINE FUNCTION IN GRAPH PLOTTING VIA MATPLOTLIB

x_axis = np.arange(0, 10, 2)
y_axis = np.sin(x_axis)
plt.plot(x_axis, y_axis)
plt.show()

#EXPONENTIAL VALUE E^X (LOG TO BASE E)
a = np.array([1,2,3,4])
print(f'EXPONENTIAL VALUE {np.exp(a)}')

#NATURAL LOGARITHM
a = np.array([1,200,1000,400])
print(f'NATURAL LOG VALUE {np.log(a)}')

#LOGARITHM BASE 10
a = np.array([1,200,1000,400])
print(f'LOG BASE 10 VALUE {np.log10(a)}')
