import os

imgs = os.listdir('files')

i=int(input('Enter the name of jpg: '))
j=int(input('Enter the name of jpeg: '))
for img in imgs:
    if (img.endswith('.jpg')):  
        print(img) 
        os.rename(f"files/{img}", f"files/{i}.jpg")
        i = i+1
for img in imgs:
    if (img.endswith('.jpeg')):  
        print(img) 
        os.rename(f"files/{img}", f"files/{j}.jpeg")
        j = j+1
