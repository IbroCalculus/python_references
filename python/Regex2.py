import re

#REGULAR EXPRESSIONS QUICK GUIDE
'''
 ^  - Matches the beginning of a line
 $  - Matches the end of a line
 .  - Matches any character
 \s - Matches whitespace
 \S - Matches any non-whitespace character
 *  - Repeats a character zero or more times
 *? - Repeats a character zero or more times (non-greedy)
 +  - Repeats a character one or more times.
 +? - Repeats a character one or more times (non-greedy)
 [aeiou]  - Matches a single character in the listed set
 [^XYZ]   - Matches a single character not in the listed set
 [a-z0-9] - The set of characters can include a range
 (  - Indicates where string extraction is to start
 )  - Indicates where String extraction is to end
'''

st = "This is a string statement, this is a this is which is a this. Just for testing regex"

#USING re.find and re.search
if re.search("is", st):
    print("Match found")
print(f'{re.search("is", st)}')
