
#values = [1,2,3,4,5,4,3,21,2,3,4,5,6,5,4,3,2,1,2,3,4,5,6,5,4,3,2]
# result = lambda filter_value: filter_value if (filter_value!= 2 and filter_value != 3) else False

#Lambda square of number
square_of_number = lambda z: z**2
print(F'SQUARE: {square_of_number(20)}')


#Lambda quadratic equation: y = 3*(X**2) + 4*X + 5
quad = lambda X: 3*(X**2) + 4*X + 5
print(f'QUAD: {quad(3)}')

welcome = lambda fName, sName: f'You are welcome Mr {fName} {sName}'
print(welcome("Ibrahim", "Suleiman"))