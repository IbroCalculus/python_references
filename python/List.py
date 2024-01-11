
#TUPLE / LIST: Tuple is less in size, hence better in size management compared to list

#NB: List accepts different data types in one list and duplicates

fnames = ['Ibrahim', "Muhammad", "Abdullahi", "Zak"]
snames = ['Suleiman', "Jamilu", "Sabo", "panshak"]
test = [['one', 'two', 'Three'], ["Ten", "Nine", "Eight"]]

print(fnames[1])
print(fnames[-1])
print(fnames)

#Count the numboer of times a particular element occurs in a list
L = ["A","B","C","A","A"]
print(f'COUNT: {L.count("A")}')

#Index of particular element in a list
L = ["A","B","C","A","A"]
print(f'INDEX: {L.index("C")}')

#Create New Empty List
myListZZZ = list()

#Number of items in a list
print(f'The number of names are: {len(fnames)}')

print("\n")
print(test)
print(test[1][2])

#Append elements to a list. (NOTE ALSO; .extend which is used to append many elements)
myListZZZ.append(["One","Two"])
myListZZZ.extend(["John","Samuel","Doe"])       # To append a list of items
print("myListZZZ Appended: ",myListZZZ)
#OR
myListZZZ += ["New name1", "New name2"]

#Add elements at specified position
myListZZZ.insert(0, "New One")
print("myListZZZ Appended2: ",myListZZZ)

#Remove items: Check below

#Reverse list
myListZZZ.reverse()
print(f'REVERSED LIST: {myListZZZ}')

#Sort elements in the list
yy = [8,5,3,-6,-20, 0]
fnames.sort()
print(f"SORTED: {fnames}")
fnames.sort(reverse=True)
print(f"SORTED2: {fnames}")
x5 = sorted(yy, reverse=True)
print(f'SORTED3: {x5}')

#Copy a list, 3 Ways
yy1 = [8,5,3,-6,-20, 0]
yy_Copy1 = yy1.copy()
yy_Copy2 = list(yy1)
yy_Copy3 = yy1[:]


#Modified element in list
test[0][2] = "Modified three"
print(test)

#Loop Through
for i in reversed(fnames):
    print(i, end=' ')
print("")

#adding elements to a list
fnames += ["New name1", "New name2"]
print(fnames)

#Removing elements from a list via element index
fnames.pop(1)       #remove element at index 1
fnames.pop()        #removes the last element in the list
print("POPPED list: ",fnames)

#Removing elements via element value
fnames.remove("New name1")      #Accepts only one argument
print(fnames)

#Remove all elements in the list
myListZZZ.clear()
print(f'Value of myListZZZ is {myListZZZ}')

#Remove many elements using list slicing
print(snames)
del(snames[:2])
print(snames)

#List slicing. syntax = str[begin, end+1].       Check String for similar
print(fnames[0:2])

#List methods.
#count(arg), insert(arg), append(), index, reverse, sort. Check Halterman


#List comprehension
numbers = [x for x in range(0,20, 2) if x != 10]
print(numbers)
