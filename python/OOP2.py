class Car:
    """
    def __init__(self):                     #Constructor
        print('Welcome to this class')
    """

    color = 'Red'  # Static variable

    def __init__(self, carName, carModel, carPrice):  # Constructor
        print('Welcome to this class')
        self.carName = carName  # Instance variable
        self.carModel = carModel
        self.carPrice = carPrice
        print(f'Car name: {self.carName}, Car model: {self.carModel}, Car price: {self.carPrice}, Car color: {Car.color}')

    def identify(self):
        print(f'The name of this car is: {self.carName} and it costs {self.carPrice} dollars, of color {Car.color}')

    @staticmethod
    def myStaticMethod():
        print("This is a static method within this class")


# ====================== INHERITANCE (CHECK DOWN BELOW FOR INHERITANCE (Example 2) ==================
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


class RabbitChild(Rabbit):  # Multi-level Inheritance
    pass



# =========================================  INHERITANCE (Example 2)  =================================================


class Dimen:
    def __init__(self, length, width):
        self.length = length
        self.width = width


class Area(Dimen):
    def __init__(self, length, width):
        super().__init__(length, width)
        self.area = self.length * self.width
        print(f'Area = {self.area}')


class Volume(Dimen):
    def __init__(self, length, width, height):
        super().__init__(length, width)
        self.height = height
        self.volume = self.length * self.width * self.height
        print(f'Volume = {self.volume}')


area1 = Area(5,10)
vol1 = Volume(5,10,2)