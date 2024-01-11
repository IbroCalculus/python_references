import copy

#Note pyperclip and shutil

#NOTE Shallow vs Deepcopy
#Shallow copy -> One level deep, only references of nested child objects
#Deep copy -> full independent copy

listN = [2,3,6,3]
listN_copy = copy.copy(listN)       #Shallow copy
listN[0] = 45
print(f'listN: {listN}')
print(f'listN_Copy: {listN_copy}')

print('')
listN2 = [[2,3,6,3],[7,2,3]]
listN_copy2 = copy.deepcopy(listN2)       #Deep copy, Shallow copy does not work
listN2[0][1] = 45
print(f'listN2: {listN2}')
print(f'listN_Copy2: {listN_copy2}')