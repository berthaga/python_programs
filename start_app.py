import subprocess

def programs():
	subprocess.call('C:\Program Files\Microsoft Office\Office15\winword')
	subprocess.call('C:\Program Files\Microsoft Office\Office15\excel')
	subprocess.call('notepad')
# save the file in C:\Documents and Settings\All Users\Start Menu\Programs\StartUp. 
# the program will start automatically during startup.

programs()