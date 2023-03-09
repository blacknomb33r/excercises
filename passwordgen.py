#created by blacknomb33r
#second project

import random
import string

s = list(string.ascii_letters + string.ascii_lowercase + string.ascii_uppercase + string.digits + "!@#$%=?!^&*()")
s2 = list(string.digits)

#choice for the user between only numbers (code) and full password with characters/special characters/numbers
def costumerchoice():
    c = int(input('Enter 1 or 2 (1 - password, 2 - passcode):'))

    if c == 1 :
        generatePassword()
    elif c == 2: 
        generatePassword2()


def generatePassword ():  
    length = int(input("Enter Length:"))

    random.shuffle(s)
    random.shuffle(s2)

    password = []
    for i in range(length):
        password.append(random.choice(s))

    random.shuffle(s)

    print("".join(password))



def generatePassword2 ():

    length = int(input("Enter character-length:"))

    random.shuffle(s2)

    password2 = []
    for i in range(length):
        password2.append(random.choice(s2))

    random.shuffle(s2)

    print("".join(password2))



costumerchoice()