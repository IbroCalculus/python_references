
 #A generator is a programming object that produces (that is, generates) a sequence of values.

def gen():
    yield "Hello"
    yield "How are you"
    yield "Good to know you"
    yield "My name is Ibrahim"
    yield "The product of 5 and 6 is: "
    yield "30"

x = gen()
print(next(x))
print(next((x)))
print('\n'*3)

for i in gen():
    print(i)
