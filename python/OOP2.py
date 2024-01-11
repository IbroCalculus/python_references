
class Car:
    '''
    def __init__(self):                     #Constructor
        print('Welcome to this class')
    '''

    color = 'Red'       #Class variable

    def __init__(self, carName, carModel, carPrice):                     #Constructor
        print('Welcome to this class')
        self.carName = carName          #Instance variable
        self.carModel = carModel
        self.carPrice = carPrice
        print(f'CAR NAME: {self.carName}\nCAR MODLE: {self.carModel}\nCAR PRICE: {self.carPrice}\nCAR COLOR: {self.color}')

    def identify(self):
        print(f'The name of this car is: {self.carName} and it costs {self.carPrice} dollars, of color {self.color}')


#====================== INHERITANCE ==================
class Animals:
    alive = True
    id = 'This object is an animal object'
    def __init__(self):
        print("This is an animal class")

    def sleep(self):
        print("The animal sleeps")

    def eat(self):
        print("This animal sleeps")


class Rabbit(Animals):
    pass
class Fish(Animals):
    pass
class Hawk(Animals):
    pass

class RabbitChild(Rabbit):          #Multi-level Inheritance
    pass