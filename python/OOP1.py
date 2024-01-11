
#Create class in seperate module. ie: OOP2

#from OOP2 import Car, Animals        #Import Class from module
from OOP2 import *        #Import Class from module
car1 = Car("Honda", "Model_4X56YT", 15000)
car1.identify()
print('\n'*2)

#========= Inheritance =============
animal1 = Animals()

rabbit1 = Rabbit()
fish1 = Fish()
hawk1 = Hawk()

print(rabbit1.id)
print(fish1.id)

rabbit1.sleep()


#============ Super keyword =============
from OOP3 import Rectangle, Square, Cube

square1 = Square(4,6)
square1.area()

cube1 = Cube(3,4,5)
cube1.volume()