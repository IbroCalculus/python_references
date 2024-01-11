import random

#The random module is not advisable for generating secure random numbers, rather use the secrets module

#They are 3 good modules for random numbers generation
#1 random  module -> For pseudo random numbers generation (Called pseudo random because they are not really random, can be reproduced)
#2 secrets module -> For cryptographic strong random numbers
#3 numpy module (Numpy2)

#random.seed(1)

print("Random")
for i in range(5):
    print(random.random())  #returns random numbers 0 < x < 1. ie 0.8634. Where x is the random number.

print("Uniform")
for i in range(5):
    print(random.uniform(1,5))  #returns random float numbers 1 and 5 inclusive

print("\nRandInt")
for i in range(5):
    print(random.randint(2,4)) #returns random int numbers 2,3 0r 4

print("\nRandRange")
for i in range(5):
    print(random.randrange(2,4)) #returns random numbers 2 or 3. 4 is not included

print('\nNormalVariate')
for i in range(3):
    print(random.normalvariate(0,1))    #random.normalvariate(mu,sigma) Good in statistics. mu=mean, sigma=standard deviation

print("\nChoice")
number_list = ["One", "Two", "Three", "Four", "Five"]
for i in range(5):
    print(random.choice(number_list))       #Returns any single random element from the list

print("\nChoices")
number_list = ["One", "Two", "Three", "Four", "Five"]
for i in range(5):
    print(random.choices(number_list, k=3))       #Returns random group of elements from the list (i.e Repetitions allowed)

print("\nSample")
number_list = ["One", "Two", "Three", "Four", "Five"]
for i in range(5):
    print(random.sample(number_list, 3))       #Returns unique random group of elements from the list (i.e no repetition)

print("\nShuffle")
name = "Ibrahim"
nameList = list(name)
print(nameList)
random.shuffle(nameList)
print(''.join(nameList))