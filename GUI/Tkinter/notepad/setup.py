import cx_Freeze
import sys
import os.path

base = None

if sys.platform == 'win32':
    base = "Win32GUI"

PYTHON_INSTALL_DIR = os.path.dirname(os.path.dirname(os.__file__))
os.environ['TCL_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tcl8.6')
os.environ['TK_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tk8.6')



executables = [cx_Freeze.Executable("custom_notepad.py", base=base,
                                    shortcutName= "Ibrahim Editor",
                                    shortcutDir="DesktopFolder")]

cx_Freeze.setup(
    name = "Personal-Notepad",
    options = {"build_exe":{"packages":["tkinter"],
            'include_files':[
            os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tk86t.dll'),
            os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tcl86t.dll'),
            "images/"
         ]
                            }},
    version = "1.0",
    description = "Your Personal text editor",
    executables = executables
    )
