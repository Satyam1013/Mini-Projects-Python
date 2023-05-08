import time
import os
from plyer import notification

time_hour = float(input('Set the hours after you want to drink water: '))
while(True):
    time.sleep(time_hour)
    command = f'''PowerShell -Command "Add-Type –AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('Please Drink Water');"'''
    os.system(command)
    notification.notify(title='Water', message='You should drink water now', timeout=2)
    



   

