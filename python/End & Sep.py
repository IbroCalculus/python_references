
#USING END
#Similar
print("Enter a number: ", end="")
x = input()
print(x)

y = input("Enter: ")
print(y)


#Similar
print("Enter a number: ", end='\n\n')
y = input()
print(y)

x = input("Enter: \n\n")
print(x)



#USING SEP
fname, mname, sname = "Ibrahim", "Musa", "Suleiman"
print(fname, mname, sname, sep='---')

#Similarly
name = "Ibrahim"
for i in name:
    print('[{}]'.format(i), end='', sep="++")
