
#CHECK: OOP for more ie Class and Instance variables, Inheritance etc, though many repetitions

import  pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
rate = engine.getProperty('rate')
print(rate)
engine.setProperty('rate', 190)

#Classes - is a blueprint for creating objects
#NB: Attributes(Properties) and Behaviours(methods)

class Phone:

    def __init__(self, brand, price):
        self.brand = brand      # Property(Attribute)
        self.price = price

    def call(self):
        print("Making a call")

    def sayMyname(self, fname):
        pyttsx3.speak(f'This phone as identified you {fname} as the new owner this phone, of brand, {self.brand}, which costs {self.price} dollars')

    #Ctrl + O
    def __str__(self) -> str:
        return f'Brand is: {self.brand}, Price is: {self.price}'

    


phone1 = Phone("Iphone", 100)
phone1.call()
phone1.sayMyname("Ibrahim Musa Suleiman")

#This displays due to def __str__(self) -> str:...
print(phone1)

