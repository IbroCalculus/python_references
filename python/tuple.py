
#TUPLE / LIST: Tuple is less in size, hence better in size management compared to list

#Tuple is immutable. i.e: You can't add or modify a tuple, have to create another

x = ("One",)    #This is a tuple
x2 = ("One","Two", "One")
print(x,x2)

#COUNT PARTICULAR ELEMENTS IN A TUPLE
print(f'COUNT: {x2.count("One")}')
