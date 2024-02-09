import time

import winsound


def play_alarm_sound():
    frequency = 2500  # Set the frequency (Hz)
    duration = 500  # Set the duration (milliseconds)
    winsound.Beep(frequency, duration)

for i in range(3):
    time.sleep(1)
    print("Iteration: " + str(i))
    play_alarm_sound()