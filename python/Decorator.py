
# A decorator is a function that receives another function as an argument.
# It adds extra functions to an existing function without modifying the initial function.

# Example
def python_basic():
    print("This is a basic python function")

def python_advance(function):
    python_basic()
    print("This is an advanced python function")

python_advance(python_basic())


# Using decorator
print("=================== ********* =============== ********* ================")

def python_advance1(function):
    def python_object_oriented():
        print("first line of code")
        function()
    return python_object_oriented

@python_advance1
def python_basic1():
    print("Second line of code")
python_basic1()

def calculator(function):
    def smart_calculator(a,b):
        return function(a,b)
    return smart_calculator

@calculator
def addition(a,b):
    print(a+b)

addition(5,5)