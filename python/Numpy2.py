import numpy as np

np.random.seed(1)

#Random float
a = np.random.rand(3)       #3 random floats in 1-D
b = np.random.rand(3,4)       #12 random floats in 3x3
print(f'RAND1: {a}')
print(f'RAND2:\n {b}')

#Random int
c = np.random.randint(2,8, (3,4))   #8 not included
print(f'RANDINT:\n {c}')

#Random shuffle
arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(f'UNSHUFFLED: \n {arr}')
np.random.shuffle(arr)
print(f'SHUFFLED: \n {arr}')

