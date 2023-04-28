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

# --------for 1 line only ---------- #

# if(select == 1): 
#   def coder(v):
#     if(len(v)>3):
#       print(result1+v[1:]+v[0]+result2)
#     else:
#       print(v[::-1])
#   coder(input('Enter encrypt code: '))
  
    
# if(select == 2): 
#   def decoder(v):
#     if(len(v)>3):
#       print(v[-4]+v[3:len(v)-4])
#     else:
#       print(v[::-1])
#   decoder(input('Enter decrypt code: '))



#-------- for multiple lines -------------#


if(select == 1): 
  st = input('Enter encrypt code: ')
  inp = st.split(" ")
  arr = []
  for i in inp:
    if(len(i)>=3):
      str = result1+i[1:]+i[0]+result2
      arr.append(str)
    else:
      arr.append(i[::-1])
  print(" ".join(arr)) 
  
    
if(select == 2):   
  st = input('Enter decrypt code: ')
  inp = st.split(" ")
  arr = []
  for i in inp:
    if(len(i)>=3):
      str = i[3:-3]
      str = str[-1] + str[:-1]
      arr.append(str)
    else:
      arr.append(i[::-1])
  print(" ".join(arr))    