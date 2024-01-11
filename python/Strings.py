#List of alphabets
import string

print(string.ascii_letters)
print(string.ascii_lowercase)       #Check others
print(string.ascii_uppercase)
print(string.digits)
print(string.punctuation)
print(string.hexdigits)
print(string.printable)

#Raw Strings - Raw strings ignore escape characters. i.e prints any \
print(r'Hello, I\'m Ibrahim')

#Count characters in a string
full_name = "Ibrahim Musa Suleiman"
print(full_name.count("a"))

#Multiline Strings
'''
    I am
        Who I am
                '''
print(''' I
            am Ibrahim ''')

#Indexing and slicing. syntax = str[begin, end+1]
msg = "This is a test string"
print(msg[5:7])
print(msg[0:])
print(msg[:])
print(msg[:7])


#in & not
msg = "This is a test string"
if "test" not in msg:
    print("True")
else: print("False")

#Some methods:
#lower()
#upper()
#islower()
#isspace()
#isalnum()
#isdecimal()


#Join - .join(takes in list of items)
fname, mname, sname = "Ibrahim", "Musa", "Suleiman"
x = '**'.join([fname, mname, sname])
print(x)

#Split - returns a list of items
x = "Ibrahim**Musa**Suleiman"
y = x.split("**")
print(y)


#Justifying
x = 'This'
print(x.rjust(10))
print(x.rjust(10, "*"))
print(x.center(10, "*"))


# Romoving white space. strip(), rstrip(), lstrip()
x = "   This is a sample    "
print(x.strip())
print(x.rstrip())
print(x.lstrip())

y = "balaTest this outbala"
print(y.strip("bala"))

x = "This is a statement"
n = x.lower().count('a', 0, len(x))     #from 0 index to len(x) index
print(n)
