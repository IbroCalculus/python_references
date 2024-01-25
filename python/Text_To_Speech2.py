
import  pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
rate = engine.getProperty('rate')
print(rate)
engine.setProperty('rate', 190)

pyttsx3.speak(f'Hello Ibrahim Calculus, you are welcome to this segment of python')