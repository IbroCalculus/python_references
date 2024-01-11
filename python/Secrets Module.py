import secrets

#It's also used for random number generations, but more secure, the others are: random and numpy(Numpy2)
#It only has 3 functions
#Used for i.e: Passwords, security tokens, account authentication
#DISADVANTAGE: It takes more time to generate the algorithms

for i in range(3):
    a = secrets.randbelow(10)       #Generates random int between 0 and 10, 10 not included
    print(f'RANDBELOW: {a}')

print()

for i in range(3):
    b = secrets.randbits(4)         #Generates random int of 4 bits values. ie 0000 - 1111 (0 - 15) 1111 included
    print(f'RANDBITS: {b}')

print()

for i in range(3):
    nameList = ["Ibrahim", "Musa", "Suleiman"]
    c = secrets.choice(nameList)            #Generates random choice from a list
    print(f'CHOICE: {c}')