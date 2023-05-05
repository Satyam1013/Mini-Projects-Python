import os

def speak(x):
    command = f'''PowerShell -Command "Add-Type –AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('{x}');"'''
    os.system(command)

list = ['Rahul','Nishant', 'Harry', 'Kunal']

for i in list:
    speak(f'Shoutout to {i}')
 