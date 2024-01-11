#Common Standard Exceptions

#Attribute error.           E.g: 2/numerator. NO ATTRIBUTE NUMERATOR
#ZeroDivisionError
#NameError


num = 5
den = 0

try:
    x = num/den
    print('ANSWER =',x)
except: print("DIVISION BY ZERO NOT ALLOWED")

########## MULTIPLE EXCEPTION ###################
num = 5
den = 0
a = 'Hello'
try:
    #y = a/2
    x = num/den
    print('ANSWER =',x)
#except ZeroDivisionError as ze: print("You cannot divide by zero. ERROR OF TYPE:", ze)
except TypeError as te: print('ERROR OCCURRED of type', te)
except Exception as e: print(f'Exception of type: {e} occured')
finally: "Runs always whether exception or not"