import random
import string

letters1 = random.choices(string.ascii_lowercase, k=3)
letters2 = random.choices(string.ascii_lowercase, k=3)

sample1 = random.sample(letters1, 3)
sample2 = random.sample(letters2, 3)

result1 = ''.join(sample1)
result2 = ''.join(sample2)


position = ['coder','decoder']

print(f'a. {position[0]}    b. {position[1]}')
select = int(input('Select Position: '))

if(select == 1): 
  def coder(v):
    if(len(v)>3):
      print(result1+v[1:]+v[0]+result2)
    else:
      print(v[::-1])
  coder(input('Enter encrypt code: '))
  
    
if(select == 2): 
  def decoder(v):
    if(len(v)>3):
      print(v[-4]+v[3:len(v)-4])
    else:
      print(v[::-1])
  decoder(input('Enter decrypt code: '))