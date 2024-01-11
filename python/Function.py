
#======================     POSITIONAL / KEYWORD ARGUMENT    =====================================================
def fullName(fName, mName, sName):
 x = f"Your first Name is {fName}"
 y = f"Your Middle Name is {mName}"
 z = f"Your Surname is {sName}"
 print(f'{x}\n{y}\n{z}')

fullName(sName="Suleiman", fName="Ibrahim", mName="Musa")



#=====================================  PARAMETER PACKING   ================================================================
def multiplier(*args):
 answer = 1
 for i in args:
  answer *= i
 print(f'THE MULTIPLIED VALUE = {answer}')

multiplier(2,3,4,10)



#=====================================  **Kwargs   ================================================================
#It is a parameter that will pack all arguments into a dictionary


#CHECK MORE, REFERENCE INCOMPLETE
def fullID(**kwargs):
    firstName = kwargs['fName']
    lastName = kwargs['lName']
    print(f'FIRST NAME: {firstName}    \nLAST NAME: {lastName}')

fullID(fName="Ibrahim", lName="Suleiman")
