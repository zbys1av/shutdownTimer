import os

print("SHUTDOWN COMPUTER IN ____ MINUTES. \n ~~~ or type '0' to stop it ~~~")

shutdownMinutes = int(input())*60

if shutdownMinutes == 0:
    os.system('shutdown -a')
else: 
    os.system(f'shutdown /s /t {shutdownMinutes}')

os.system("exit /b")