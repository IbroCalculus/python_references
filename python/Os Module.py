import os
import shutil
from datetime import datetime


# print(f"OS MODULE ATTRIBUTES AND METHODS: {dir(os)}")   # List of attributes and methods of the OS module
print(f"CURRENT WORKING DIRECTORY: {os.getcwd()}")      # Get current working directory

pathToFile = r'python/NewDir/innerOne/innerTwo/innerThree/myFile.txt'
print(f"ABSOLUTE PATH: {os.path.abspath(pathToFile)}")
print(f"DIRECTORY NAME: {os.path.dirname(pathToFile)}")
print(f"BASE NAME: {os.path.basename(pathToFile)}")      # Get the basename from the path. ie: myFile.txt
print(f"Both splitted: {os.path.split(pathToFile)}")

# Change working directory
# os.chdir(path)
# print(f"CURRENT WORKING DIRECTORY: {os.getcwd()}")

# Create new directory
# try:
#     os.makedirs('NewDir/innerOne/innerTwo/innerThree', exist_ok=True)  # Can create nested directories
#     # os.mkdir('NewDir')      #Create just a single directory unlike os.makedirs()
#
#     with open('NewDir/innerOne/innerTwo/innerThree/myFile.txt', 'a') as f:
#         f.write('This is the first line\n')
#         f.write('And this is the second line')
#     print('directory created')
# except:
#     print('Cannot create directory of the same name')

# Delete directories
# os.rmdir('NewDir/innerOne/innerTwo/innerThree')       #Remove a single directory. i.e innerThree
# os.removedirs('NewDir/innerOne/innerTwo/innerThree')  # Remove directory with nested directories

# Delete files
# os.remove('file1.txt')

# Rename file or folder
# os.rename('NewDir', 'NewRanamedDir')

# List file and folder in a directory
print(f"FILES AND FOLDER IN CURRENT DIRECTORY: {os.listdir()}")
# print(os.listdir(r'C:\Users\Ibrahim Suleiman\Desktop'))

# Check if directory or file exists
path = r'C:\Users\ibrahimsuleiman\Documents'  # ...\AndroidStudio\Project1.txt
print(f"Does the directory; Ibrahim Suleiman exists?: ANS: {os.path.exists(path)}")

# Check if file exists in a directory or if location is a file
statement = "This file exists" if os.path.isfile("thisfile.csv") else "This file does not exist"
print(statement)

# Check if directory exists if location is a directory
statement = "This is a folder" if os.path.isdir("thisfile.csv") else "This folder does not exist"
print(statement)


# Move files or replace files
# file_name = 'PracticeABC.py'
# destination_folder = 'NewDir'
#
# source = os.path.join(os.getcwd(), file_name)
# destination = os.path.join(os.getcwd(), destination_folder, file_name)
#
# if not os.path.exists(destination_folder):
#     os.makedirs(destination_folder)
# try:
#     shutil.move(source, destination)
#     print(f'Successfully moved {file_name} to {destination_folder}')
# except Exception as e:
#     print(f'Error: {e}')



# # GETTING INFO ABOUT A FILE
print(os.stat(r'test.py'))
print(f"The size of the file is: {os.stat(r'test.py').st_size} bytes")
last_mode_time = os.stat(r'test.py').st_mtime
formatted_last_mode_time = datetime.fromtimestamp(last_mode_time)
print(f"The time last modified is: {formatted_last_mode_time}")
print(datetime.fromtimestamp(os.stat('NewDir').st_mtime))

# VIEW DIRECTORY TREE
# print(os.walk('NewDir'))
# for i, j, k in os.walk('NewDir'):
#     print(f'CURRENT PATH {i} \nDIRECTORIES {j} \nFILES{k}')
#     print('\n')

# Get current user logged in to this PC
print(f"CURRENT LOGIN: {os.getlogin()}")




