
#CREATE A DICTIONARY: 2 METHODS
cars = {"Benz": 2,
        "Corola": 1}

cars2 = dict(fname="Ibrahim", mname="Musa", sname="Suleiman")

print(f'The number of Benz cars are: {cars["Benz"]}')
print(f'You are welcome Mr {cars2["fname"]} {cars2["mname"]} {cars2["sname"]}')

#Copy a dictionary
cars2 = dict(fname="Ibrahim", mname="Musa", sname="Suleiman")
cars2_copy = cars2.copy()

#Add element
cars['Toyota'] = 5
print(cars)

#Access keys and values
print(f'The keys of the dictionary are: {cars.keys()}')
print(f'The values of the dictionary are: {cars.values()}')

for i in (cars.keys()):
    print(f'The number of {i} cars are: {cars.get(i)} OR {cars[i]}') #of cars[i]
print("\n")


for i,j in (cars.items()):
    print(f'The number of {i} cars are {j}')
print('\n')

#Update a dictionary
dict1 = dict(fname="One", sname="Two", email="someone@email.com", phone=41234)
dict2 = dict(fname="One", sname="Three", email="nobody@email.com", phone=98765, address="My home address")
dict1.update(dict2)
print(f'DICT_MERGE: {dict1}')

#Dictionary from lists
keyList = ['cat', 'Dog', 'Fish', 'Hen']
valueList = [2,4,8,3]

for i in zip(keyList, valueList):
    print(i)
print('\n')

for i,j in zip(keyList, valueList):
    print(f'The number of {i} are {j}')
print('\n')


animals = dict(zip(keyList, valueList))
for i in animals:
    print(f'The value of {i} are {animals[i]}')
print('\n')

#Deleting Elements
print(animals)
del animals['Dog']
print(animals.items())
print(animals)
print('\n')

#cars.pop('Benz')   #Remove the Benz key value pair
#cars.popitem()     #Removes the last inserted element in the dictionary

#Clear elements from the dictionary
animals.clear()
print(animals)
print('\n')

#Delete a dictionary
print(cars)
del cars
print(f'After del, Cars = ', end='')
print(cars)

