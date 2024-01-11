
#Does not allow duplicate, and unordered, but mutable.
#It is faster than a list

#Python supports the standard mathematical set operations of
# intersection, union, set difference, and symmetric difference.

#DECLARING EMPTY SET
x= set()                #NOTE: x = {} is not an empty set, rather an empty dictionary

s = {10,10,10,3,2}
print(s, end='\n\n')

L = ['Ibrahim','Ibrahim','Ibrahim',"Musa"]
print(L,end='\n')
S = set(L)
print(S)

#Counting characters using set
testT = "Ibrahim Musa Suleiman"
print(f'CHARACTERS PRESENT: {set(testT)}, NUMBER OF CHARACTERS: {len(set(testT))}')

#Add elements to a set
y = set()
y.add("One")
y.add("Two")
y.add("Three")
y.add("Four")
print(y)
print(f'ADDED ELEMENT: {y}')

#Remove element from a set
y.remove("Three") #OR y.discard("Three")
print(f'ROM0VED ELEMENT: {y}')

#y.pop()    removes the last element in the tuple, but tuple is unordered, ie: removes any element


#Clear a set
y.clear()

#Delete a tuple
del y


#JOIN TWO SETS
#Assume Set1 and Set2 are defined, use the Set1.update(Set2). print(Set1)

#SET OPERATIONS
#UNION                      A|B
#INTERSECTION               A&B
#SET DIFFERENCE             A-B         ELEMENTS IN A BUT NOT IN B
#SYMETRIC DIFFERENCE        A^B         ELEMENTS IN A OR B, BUT NOT IN BOTH

#Check reference for more

A = {"IBRAHIM", "IBRAHIM", "MUSA"}
B = {"SULEIMAN", "20s", "IBRAHIM"}

print(f'THE UNION: {A|B}')
print(f'THE INTERSECT: {A&B}')
print(f'THE DIFFERENCE: {A-B}')
print(f'THE SYMETRIC DIFFERENCE: {A^B}')

x = (A|B) - (A&B)

print(f'SIMILARLY: {x}')

#SET QUANTIFICATION WITH ALL AND ANY
#Check reference