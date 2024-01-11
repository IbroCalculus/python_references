def fib():
    a,b = 0,1
    while True:
        yield a
        a,b = b, a+b

#Fibbonaci sequence of less than 50
for i in fib():
    if i > 50:
        break
    print(i)