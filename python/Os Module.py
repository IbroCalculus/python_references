import os

for i in dir(os):
    print(i, end=' ')
print('\n')

#Get current working directory
print(os.getcwd())

#Check if directory or file exists
path = r'C:\Users\Public\AndroidStudio'     #...\AndroidStudio\Project1.txt
print(f"Does the directory; Ibrahim Suleiman exists?: ANS: {os.path.exists(path)}")

#Change working directory
#os.chdir('Users/...')

#List file and folder in a directory
print(os.listdir())
print(os.listdir(r'C:\Users\Ibrahim Suleiman\Desktop'))
Number_of_items = len(os.listdir(r'C:\Users\Ibrahim Suleiman\Desktop'))
print(f'The number of items in the directory are {Number_of_items}')

#Check if file exists in a directory or if location is a file
statement = "This file exists" if os.path.isfile("thisfile.csv") else "This file does not exist"
print(statement)

#Check if directory exists if location is a directory
statement = "This is a folder" if os.path.isdir("thisfile.csv") else "This is not a folder"
print(statement)

#Move files or replace files
'''
source = text.txt
destination = r'C:\Desktop\text.txt
os.replace(source, destination)
'''

#Move folder or replace folder
'''
source = folder1
destination = r'C:\Desktop\folder1
os.replace(source, destination)
'''

#Create new directory
try:
    os.makedirs('NewDir/innerOne/innerTwo/innerThree') #Can create nested directories
    #os.mkdir('NewDir')      #Create just a single directory unlike os.makedirs()

    with open('NewDir/innerOne/innerTwo/innerThree/myFile.txt', 'w') as f:
        f.write('This is the first line\n')
        f.write('And this is the second line')
    print('directory created')
except:
    print('Cannot create directory of the same name')

#Deleting files
'''
os.remove('file1.txt')
'''

#Deleting directories
def delete_dir():
    #os.rmdir('NewDir/innerOne/innerTwo/innerThree')    #Remove a single directory. i.e innerThree
    #print('Directory removed')
    os.removedirs('NewDir/innerOne/innerTwo/innerThree')       #Remove directory with nested directories
    print('All directories removed')

#delete_dir()

#RENAMING FILE OR FOLDER
#os.rename('NewDir', 'NewRanamedDir')

#GETTING INFO ABOUT A FILE
print(os.stat('NewRanamedDir'))
for i in os.stat('NewRanamedDir'):
    print(i)

print('\n')


#VIEW DIRECTORY TREE
print(os.walk('NewDir'))
for i,j,k in os.walk('NewDir'):
    print(f'CURRENT PATH {i} \nDIRECTORIES {j} \nFILES{k}')
    print('\n')