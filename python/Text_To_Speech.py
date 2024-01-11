
import pyttsx3
import time

#Works offline


#1. Basic Usage
def basicUsage():
    msg1 = "Good day ibrahim, Press Enter to proceed with the launch sequence?"
    print(msg1)
    pyttsx3.speak(msg1)
    input()

    pyttsx3.speak("Ready to launch in...")
    for i in range(10, 0, -1):
        print(i)
        pyttsx3.speak(i)
        time.sleep(0.01)

    msg2 = "Launch carried out successfully"
    print(msg2)
    pyttsx3.speak(msg2)

#basicUsage()

#2. More
def advanceUsage():
    #Speak
    engine = pyttsx3.init() # object creation
    engine.say("Hello Ibrahim, what may I do for you today?")
    engine.runAndWait()

    #Changing voice, Rate and Volume

    """ RATE. ie: How fast the voice sound, normal about 200"""
    rate = engine.getProperty('rate')  # getting details of current speaking rate
    print(f'RATE1: {rate}')  # printing current voice rate
    engine.setProperty('rate', 325)  # setting up new voice rate
    print(f'RATE2: {rate}')  # printing current voice rate
    engine.say("Hello Ibrahim, what may I do for you today?")
    engine.runAndWait()

    """VOLUME"""
    volume = engine.getProperty('volume')  # getting to know current volume level (min=0 and max=1)
    print(volume)  # printing current volume level
    engine.setProperty('volume', 0.3)  # setting up volume level  between 0 and 1
    engine.say("Hello Ibrahim, Welcome to python text to speech.")
    engine.runAndWait()

    """VOICE"""
    engine.setProperty('volume', 1.0)  # setting up volume level  between 0 and 1
    engine.setProperty('rate', 150)  # setting up new voice rate
    rate1 = engine.getProperty('rate')  # getting details of current speaking rate
    print(f'RATE3: {rate}')
    voices = engine.getProperty('voices')  # getting details of current voice
    # engine.setProperty('voice', voices[0].id)  #changing index, changes voices. 0 for male
    engine.setProperty('voice', voices[1].id)  # changing index, changes voices. 1 for female

    engine.say("Hello Ibrahim, Welcome to python text to speech.")
    engine.say('My current speaking rate is ' + str(rate1))
    engine.runAndWait()
    engine.stop()


    """Saving Voice to a file"""

    print("Do you want to save a voice recording?, if yes, press enter to proceed")
    engine.say("Do you want to save a voice recording?, if yes, press enter to proceed")
    engine.runAndWait()
    input()

    # On linux make sure that 'espeak' and 'ffmpeg' are installed
    engine.save_to_file('Hello World, I am Ibrahim Suleiman', 'testTTS.mp3')
    time.sleep(1)
    engine.say("File saved successfully")
    engine.runAndWait()


advanceUsage()

