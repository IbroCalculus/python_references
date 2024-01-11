
#reduce apply a function to an iterable and reduce it to a single cummulative value.
#It performs function on first two elements and repeats the process until 1 value remains

#Fibonacci sequence of addition, Factorial of numbers, etc

#reduce(function, iterable)

import functools

letter = ['I','b','r','a','h','i','m']
action = lambda x,y: x + y
word = functools.reduce(action, letter)
print(f'WORD: {word}')

numbers1 = [1,2,3,4,5]
action = lambda x,y: x*y
factorial = functools.reduce(action, numbers1)
print(f'FACTORIAL OF 5 = {factorial}')

numbers2 = [1,2,3,4,5]
action = lambda x,y: x+y
fibonacci = functools.reduce(action, numbers2)
print(f'FIBONACCI OF 5 = {fibonacci}')