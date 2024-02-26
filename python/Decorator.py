import time


# A decorator is a function that receives another function as an argument.
# It adds extra functions to an existing function without modifying the initial function.



# ------ Syntax of creating a decorator function -----
def decorator_function(function):
    def wrapper_function():
        function()
    return wrapper_function

# ========== Example 1; (Add two seconds delay two each of these three functions before their print statement is called) ==============
# 1. The decorator function:
def add_delay_decorator(function):
    def add_delay():
        time.sleep(1)
        function()
    return add_delay


@add_delay_decorator
def say_hello():
    print("Hello, AFTER 1 second")
@add_delay_decorator
def say_bye():
    print("Bye, AFTER 1 second")

@add_delay_decorator
def say_greeting():
    print("Good morning, AFTER 1 second")

def alternative():
    print("This is an alternative way of using a decorator on a function")

say_hello()
say_bye()
say_greeting()

altern = add_delay_decorator(alternative)
altern()

time.sleep(2)

print("\n=============================== EXAMPLE 2 ========================================")

# ========== Example 2; (A decorator that loops 5 times over a function call) ==============
# Alternatively, check below to pass in the value for the number of iterations, instead of the static 5


def function_looper(function):
    def looper_function():
        for i in range(5):
            print(f'Iteration: {i+1}:   ', end="")
            function()
    return looper_function


@function_looper
def say_hi():
    print("Hi, you are welcome")

@function_looper
def welcome():
    print("You are welcome")


say_hi()
welcome()

time.sleep(1)

print("=============================== EXAMPLE 3 ========================================")

# ========== Example 3; (Same as Example 2 above, but passing in dynamic value) ==============
#
def function_looper2(iterations=1):             # default value is 2
    def decorator(function):
        def looper_function():
            for i in range(iterations):
                print(f'Iteration: {i+1}:   ', end="")
                function()
        return looper_function
    return decorator


@function_looper2(iterations=2)
def say_something():
    print("This is saying something")

@function_looper2(4)
def who_are_you():
    print("Can I know who you are?")

say_something()
who_are_you()