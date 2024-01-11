import time
import math
import string

#TYPING Duration
print("Enter any text in: ")
for i in range(3, 0, -1):
    print(i)
    time.sleep(1)
("Press Enter and start typing: ")
input()
start_time = time.time()
text = input("Type\n")
end_time = time.time()
elapsted_time = end_time - start_time
elapsted_time = round(elapsted_time,2)
print(f"ELAPSED TIME: {elapsted_time} seconds")

alphabets = string.ascii_letters
vowels = 'aeiouAEIOU'
consonants = ""
for i in alphabets:
    if i not in vowels:
        consonants += i
print(f'STRING OF CONSONANTS ARE: {consonants} of length {len(consonants)}')

vowelCount = 0
consonantCount = 0
characterCount = 0
wordCount = 0

for i in text:
    if i in vowels:
        vowelCount += 1
    if i in consonants:
        consonantCount += 1
    characterCount += 1

print("VOWELS = {}\nCHARACTERS = {}\nCONSONANTS = {}".format(vowelCount, characterCount, consonantCount))


#WORD COUNTER
y = text.split(" ")
print(y)
print(f'NUMBER OF WORDS: {len(y)}')

typing_speed = len(y)/ elapsted_time
typing_speed_Minutes = 60*(typing_speed)
print(f'Your typing speed is: {typing_speed} WPS or {typing_speed_Minutes} WPM ')