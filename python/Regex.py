import re

#NB: .findall does not work with patterns containing groups. i.e: ()

#CREATING PATTERNS AND USING SEARCH & FINDALL METHOD IN re
regex1 = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
text = 'My number are 415-555-6543 as well as 657-321-6643.'
mo = regex1.search(text) #Returns only the first item of the pattern. i.e 415-555-6543
print('Phone number found is: ' + mo.group())
print('\n')
mo2 = regex1.findall(text)
print('Phone number found is: ', mo2) #Returns the list of all items that match the pattern


#GROUPING WITH PARENTHESIS
regex1 = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')
text = 'My number are 415-555-6543 as well as 657-321-6643.'
mo = regex1.search(text)
print('Phone number found is: ' + mo.group())
print('Phone number found is: ' + mo.group(0))
print('Phone items in 1st parenthesis are: ' + mo.group(1))
print('Phone items in 2nd parenthesis are: ' + mo.group(2))
print('The groups are:', mo.groups())

#MATCHING MULTIPLE GROUPS WITH PIPE
regex2 = re.compile(r'Ibrahim|Musa')
text = "I am Musa, but you can call me Ibrahim"
mo = regex2.search(text)
mo2 = regex2.findall(text)
print('THE OUTPUT IS:', mo2)
print('\n')

#OPTIONAL MATCHING WITH THE QUESTION MARK. (Zero or One)
regex3 = re.compile(r'Bat(wo)?man')
mo1 = regex3.search('The Adventures of Batman and Batwoman')
mo2 = regex3.findall('The Adventures of Batman and Batwoman') #? Doesn't seem to work well with .findall because of group. ().
print(mo1.group())
print(mo2)
print('\n')

#MATCHING ZERO OR MORE WITH THE STAR (*)
regex4 = re.compile(r'Bat(wo)*man')
text = 'This is Batwowowowowoman'
mo1 = regex4.search(text)
mo2 = regex4.findall(text)          #* Doesn't seem to work well with .findall because of group. ().
print("THE OUTPUT:", mo1.group())
print("THE OUTPUT:", mo2)
print("\n")

#MATCHING ONE OR MORE WITH THE PLUS (+)
regex5 = re.compile(r'Bat(wo)+man')
text = 'This is a Batwoman and Batwowoman'
mo1 = regex5.search(text)
mo2 = regex5.findall(text)
print("Mo1:", mo1.group())
print("Mo2:", mo2)
print("\n")

#MATCHING SPECIFIC REPETIONS WITH CURLY BRACKETS
regex6 = re.compile(r'(wo){2}')
text = 'This a Batwowoman and Somwowowo'
mo1 = regex6.search(text)
mo2 = regex6.findall(text)
print('CURLY:', mo1.group())
print('CURLY:', mo2)
print('\n')

#(wo){2,5} -> 2 or 3 or 4 0r 5 times wo
#GREEDY AND NONGREEDY MATCHING
#GREEDY implies in (wo){2,5}, regext will match the longest first. i.e wo*5. this is DEFAULT
#TO make into non-greedy. Syntax; (wo){2,5}?


#CHARACTER CLASSES
# \d                Any numeric digit from 0 to 9
# \D                Any character that is not a numeric digit from 0 to 9
# \w                Any letter, numeric digit, or the underscore character
# \W                Any character that is not a letter, numeric digit, or the underscore character
# \s                Any space, tab, or newline character.
# \S                Any character that is not a space, tab, or newline character.

#The character class [0-5] will match only the numbers 0 to 5; this is much shorter than typing (0|1|2|3|4|5).


#MAKING YOUR OWN CHARACTER CLASS
#the character class [aeiouAEIOU] will match any vowel, both lowercase and uppercase.
#the character class [a-zA-Z0-9] will match all lowercase letters, uppercase letters, and numbers.

#By placing a caret character (^) just after the character class’s opening bracket, you can make a
# negative character class. A negative character class will match all the characters that are not in
# the character class.

#THE CARET(^) AND DOLLAR($) SIGN CHARACTERS
# ^ at the start of a regex to indicate that  a match must occur at the beginning of the searched text.
# $ at the end of the regex to indicate the string must end with this regex pattern.

#THE WILDCARD CHARACTER (.)
# will match any character except for a newline.

#MATCHING EVERYTHING WITH DOT-STAR (.*)

#MATCHING NEWLINES WITH THE DOT CHARACTER BY PASSING re.DOTALL as the second argument to re.compile('')
#E.g: newlineRegex = re.compile('.*', re.DOTALL)


#CASE INSENSITIVE MATCHING BY PASSING re.I or re.IGNORECASE
#E.g: robocop = re.compile(r'robocop', re.I)


#SUBSTITUTING STRINGS WITH THE sub METHOD. Check reference

#FORMAT THE REGEX ON MULTILINE ignoring white space and comments. Check reference.