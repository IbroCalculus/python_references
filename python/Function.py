#======================     POSITIONAL    =====================================================
def fullName(fName, mName, sName):
    x = f"Your first Name is {fName}"
    y = f"Your Middle Name is {mName}"
    z = f"Your Surname is {sName}"
    print(f'{x}\n{y}\n{z}')


fullName(sName="Suleiman", fName="Ibrahim", mName="Musa")       # Named argument not required, check below
fullName("Suleiman", "Ibrahim", "Musa")


#======================     NAMED ARGUMENT (Required)   =====================================================
def get_full_name(*, first_name, last_name):
    full_name = first_name.title() + " " + last_name.title()
    return full_name


print(get_full_name(first_name="john", last_name="doe"))


#=====================================  PARAMETER PACKING   ================================================================
def multiplier(*args):
    answer = 1
    for i in args:
        answer *= i
    print(f'THE MULTIPLIED VALUE = {answer}')


multiplier(2, 3, 4, 10)


#=====================================  **Kwargs   ================================================================
#It is a parameter that will pack all arguments into a dictionary


#CHECK MORE, REFERENCE INCOMPLETE
def fullID(**kwargs):
    firstName = kwargs['fName']
    lastName = kwargs['lName']
    print(f'FIRST NAME: {firstName}    \nLAST NAME: {lastName}')


fullID(fName="Ibrahim", lName="Suleiman")


# ================================ FIRST ORDER FUNCTION ============================
def add(n1, n2):
    return n1 + n2


def multiply(n1, n2):
    return n1 * n2


def calculate(calc_function, n1, n2):
    return calc_function(n1, n2)


resut_add = calculate(add, 2, 3)
resut_multiply = calculate(multiply, 2, 3)

print(f'Result_add: {resut_add}')
print(f'Result_multiply: {resut_multiply}')


# ================================ NESTED FUNCTIONS ============================
def outter():
    print("I am outter function")

    def inner():
        print("I am inner function")

    inner()


outter()
