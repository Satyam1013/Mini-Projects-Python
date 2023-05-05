import random;
#Snake, Water And Gun = SWAG
def checker(computer, you):
    if (you > 2):
        print('You Stupid!')
    if (computer == you):
        return 0
    if (computer == 0 and you == 1):
        return -1
    if (computer == 1 and you == 2):
        return -1
    if (computer == 2 and you == 0):
        return -1       
    return 1

computer = random.randint(0,2)
you = int(input('Choose 0 for Snake, 1 for Water, 2 for Gun : '))

print("Computer: ", computer)
print('You: ',you)

score = checker(computer,you)

if (score == 0):
    print("It's a Draw")
elif (score == -1):  
    print('You Lose')    
elif (score == 1):
    print('You Win')            