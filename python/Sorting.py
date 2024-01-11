
#Sort() method - Used with lists
#Sort() function - Used with iterables


#=============== SORT METHOD (this works with only lists)===================
list1 = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten"]
list1.sort()
print(f'FIRST SORT: {list1}')

list1.sort(reverse=True)
print(f'SECOND SORT: {list1}')
print('\n')

#=============== SORTED FUNCTION (Accept other iterables including lists) ===================
tuple1 = ("Alpha", "Beta", "Gamma", "Delta", "Epsilon", "Zeta", "Eta", "Theta", "Iota", "Kappa")
list1_sorted = sorted(tuple1)
print(f'THIRD SORT: {list1_sorted}')

list1_sorted = sorted(tuple1, reverse=True)
print(f'FOURTH SORT: {list1_sorted}')
print('\n')

#=========== MORE ON SORT  WITH SORT METHOD (works only on lists) =================
list2 = [("Ibrahim", "Suleiman", 26),
         ("Abraham", "Lincon", 87),
         ("Sadiq", "Kashmar", 66),
         ("Philip", "Johnson", 41),
         ("Anthony", "Mark", 39),
         ("Pascal", "Blaize", 42),
         ("Isaac", "Newton", 78)]

sort_key = lambda sort_value: sort_value[2] #Sort by index 2
list2.sort(key=sort_key, reverse=True)
for i in list2:
    print(i)
print('\n')


#=========== MORE ON SORT  WITH SORTED FUNCTION (works only all iterables) =================
tuple2 = (("Ibrahim", "Suleiman", 26),
         ("Abraham", "Lincon", 87),
         ("Sadiq", "Kashmar", 66),
         ("Philip", "Johnson", 41),
         ("Anthony", "Mark", 39),
         ("Pascal", "Blaize", 42),
         ("Isaac", "Newton", 78))

sort_key = lambda sort_value: sort_value[1] #Sort by index 1
sorted_values = sorted(tuple2, key=sort_key, reverse=True)
for i in sorted_values:
    print(i)
print('\n')