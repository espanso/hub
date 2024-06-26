import random
import os
import string

def check_pass(password):
    cont = 0
    if password.lower() == password or password.upper() == password:
        return False
    else:
        cont += 1

    for character in password:
        if character in characters[1]:
            cont += 1
            break
    
    for character in password:
        if character in characters[2]:
            cont += 1
            break

    if cont == 3:
        return True
    else:
        return False
    
def generate(n):
    password = ''
    for i in range(n):
        password += random.choice(random.choice(characters))
    if check_pass(password):
        return password
    else:
       return generate(n)

try:
    myvar = os.environ['ESPANSO_MYVAR']
    mybarbool = True
except:
    mybarbool = False

characters = [list(string.ascii_letters), list(string.punctuation), list(string.digits)]

try:
    import pyperclip
    if mybarbool:
        try:
            myvar = int(myvar)
            password = generate(myvar)
            pyperclip.copy(f'{password}')
            spam = pyperclip.paste()
            print(password)
        except:
            password = generate(12)
            pyperclip.copy(f'{password}')
            spam = pyperclip.paste()
            print(password)
    else:
        password = generate(12)
        pyperclip.copy(f'{password}')
        spam = pyperclip.paste()
        print(password)

except:
    if mybarbool:
        try:
            myvar = int(myvar)
            password = generate(myvar)
            print(password)
        except:
            password = generate(12)
            print(password)
    else:
        password = generate(12)
        print(password)


