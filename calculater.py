#calculater
import subprocess
while 1:
	cal=input()
  	if cal[0].isdigit():
		subprocess.call('C:\Windows\system32\WindowsPowerShell\\v1.0\\powershell.exe '+cal+,shell=True)
	else:
		print("enter valid expression")
    
