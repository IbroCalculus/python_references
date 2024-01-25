
import os

#CHECK PDFs to learn how to work with pdf files
#CHECK OS Module for more on working with files and directories

#DELETE FILES / DIRECTORIES:    Check: Send2Trash.py


#Check if file exists in a directory
statement = "This file exists" if os.path.isfile("thisfile.csv") else "This file does not exist"
print(statement)

#f.seek(5) -> Moves the file cursor to the 5th character, hence can override
#f.tell()   -> Tells the current position within the file

#Reading (r), writing (w), reading and writing (r+) and appending (a) a file or binary file (rb, wb, ab)
#myFileObj = open("myFile.txt", 'r')
#myFileObj.close()

#If second argument is not present, it defaults to a read file. i.e myFileObj = open('myFile.txt') == open('myFile.txt', 'r')


#CREATE AND WRITE TO A FILE
myFileObjWrite = open("FileTextFile.txt", 'w')
myFileObjWrite.write("This is the first text")
myFileObjWrite.write("\nThis is the second text")
myFileObjWrite.close()


#READ FROM A FILE
myFileObjRead = open("FileTextFile.txt", 'r')
print(myFileObjRead.name)
print(myFileObjRead.mode)
'''for i in myFileObjRead:
    print(i.strip())
'''
content = myFileObjRead.read()  #.read(100) -> Read the first 100 Characters
print("CONTENT", content)
myFileObjRead.close()

print('\n')


#USING CONTEXT MANAGER
with open('FileTextFile.txt') as f:
    contents = f.read()     #Good for small file, DON'T OVERLOAD the memory with large file, instead check below
                            # .read(100) -> Read the first 100 Characters
    print('CONTENTS:', contents)

print('\n\n')


with open('FileTextFile2.txt', 'w') as f:
    f.write('This is another first line')
    f.write('\nThis is another second line')
    f.write('\nThis is another third line')

print('CONTENT2:')
with open('FileTextFile2.txt', 'r') as f:
    x = f.readlines()   #Returns list of String by lines
    for content in x:
        print(content.rstrip())


print('\n\nCONTENT3:')
with open('FileTextFile2.txt', 'r') as f:
    x = f.readline()   #Returns first list Item
    print(x, end='')

#Efficient way
print('\n\nCONTENT4:')
with open('FileTextFile2.txt', 'r') as f:
    for i in f:
        print(i, end='')


#Copying file
with open('FileTextFile.txt', 'r') as rf:
    with open('FileTextFile_Copy.txt', 'w') as wf:
        for line in rf:
            wf.write(line) 