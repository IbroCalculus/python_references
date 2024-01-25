
import  pyttsx3
import time_ref
import winsound

#Ternary if statement.  Use with only one if statement

time.sleep(1)
winsound.Beep(1000, 500)

print("Enter your firstname here:")
pyttsx3.speak("Enter your firstname here:")
fname = input()
response = pyttsx3.speak("Access granted") if fname == "Ibrahim" else pyttsx3.speak("Access Denied")

#
# print("Type in the statement you will like to be read for you:\n")
# pyttsx3.speak("Type in the statement you will like to be read for you:\n")
# statement = input()
#
# print("Type in the statement you will like to be read for you:\n")
# pyttsx3.speak("Machine will read the statement after the beep")
# time.sleep(1)
# winsound.Beep(3000, 500)
#
# pyttsx3.speak(statement)
