
fname, mname, sname = "Ibrahim", "Musa", "Suleiman"
print("Welcome Mr {2}, {0} {1}".format(fname, mname, sname))


# By default, left justified
# {:>3} => Right-justify the first argument with a width of 3 characters

a,b,c,d = 1,10,100,1000
print('a={0:>4}, b={1:>4}, c={2:>4}, d={3:>4}'.format(a,b,c,d))
print('a={0:>3}, b={1:>3}, c={2:>3}, d={3:>3}'.format(a,b,c,d))
print('a={0:>2}, b={1:>2}, c={2:>2}, d={3:>2}'.format(a,b,c,d))
print('a={0:>1}, b={1:>1}, c={2:>1}, d={3:>1}'.format(a,b,c,d))
print('a={0:>0}, b={1:>0}, c={2:>0}, d={3:>0}'.format(a,b,c,d))
print('a={0}, b={1}, c={2}, d={3}'.format(a,b,c,d))

#Second method
x,y,z = "Ibrahim", "Musa", "Suleiman"
print(f'You are welcome Mr {z} {x} {y}')

#Third method

fname, sname = "Ibrahim", "Musa"
print("I am %s of surname %s. Thank you." % (fname, sname))

x,y = 45, 234.3456
print("The numbers are: %d and %f" % (x,y))

#Check reference for more
