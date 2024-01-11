
#NB: Windows defender may prevent running, hence, turn it off
#Make sure pip and pyinstaller are installed/updated


#Copy the python file (and all relevant files, if any) to a new folder
#Access CMD, with directory being the folder

#Using pyinstaller, Note these commands:
'''
    -F              (Make all in 1 file)
    -w              (Remove terminal window, in programs where it is not needed)
    -i iconName.ico (Adds custom icon, must be a .ico)
    -scriptName.py  ()
    E.g; C:\Users....\New Folder >pyinstaller -F -w -i iconName.ico scriptName.py

    Locate exe file with 'dist' folder
    NB: Move the .exe from the 'dist' folder before you can see the icon reflect instead of the default
'''