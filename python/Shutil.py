import shutil

#This is used to copy and move files files e.g .txt, .png etc or make duplicates

#Check also; pyperclip
#in the shutil module, there are 3 basic functions to copying a file: ie
'''
1. copyfile() - Copies content of a file
2. copy() - copyfile() + permission mode + destination can be a directory
3. copy2() - copy() + copy metadata (file's creation and modification times)
shutil.move()   - This moves the file. CHECK Os Module.py for usage example
'''

#============= 1. copyfile() ============
# NB: Clear shutil2 before running this code to observe the change

input("Press enter to copy the contents of Shutil1.txt into Shutil2.txt: ")

shutil.copyfile('Shutil1.txt', 'Shutil2.txt')  #src, des
shutil.copyfile('QR_Title.png', 'QR_Title2.png')
print('DONE!')

#NB: For both copy and copy2, the arguments are same as that for copyfile
