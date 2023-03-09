# created by blacknomb33r  
# first "bigger" project
import random

#declare variables
userscore = 0
sysscore = 0

name = input('Enter your name: ')
while True:
    try: 
        rounds = int(input('How many rounds? '))
        break
    except:
        print('That is not a number!')

def startEnd():
    print('=======================')

print('Starting Match...')

for i in range(rounds):  
    sys = ['rock', 'paper', 'scissor']
    sys = random.choice(sys)
    while True:
           print('Enter your choice (rock, paper, scissor): ')
           user = input().lower()
           if user in ['rock', 'paper', 'scissor']:
               break
           else:
            print('That is not a weapon. ;)')
    
    #if condition
    if sys == user:
        print('Me:',sys,'| You:', user,' - We pick the same')
        userscore += 1
        sysscore += 1
    elif sys == 'rock' and user == 'paper' or sys == 'paper' and user == 'scissor' or sys == 'scissor' and user == 'rock':
        print('Me:',sys,'| You:',user,' - you win...')
        userscore += 1
    else:
        print('Me:',sys,'| You:',user,'I win.')
        sysscore += 1
    rounds -= 1
    startEnd()
    print('Current Score:','Computer:',sysscore,':','You:',userscore)
    
if rounds == 0:
    startEnd()
    print('Finalscore:','Computer:',sysscore,':','You:',userscore)
    if sysscore == userscore:
        print('We are both machines.')
    elif sysscore > userscore: 
        print('I beat you up.')
    else: 
        print('You beat me... - Try again.')
    print('Thank you',name,'for playing')
    
else:
    print('Error')

