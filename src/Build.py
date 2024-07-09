import subprocess
import os
import sys

PATH = os.path.dirname(__file__)

command = (f"pyinstaller "
           f"--onefile "
           f"--noconsole "
           f"--icon={PATH}/television.ico "
           f'--add-data="{PATH}/television.ico;." '
           f"Television_Tray.py")

subprocess.run(command, shell=True)
