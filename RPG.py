# I want to make an RPG Game based sorta like Legend of Zelda but, with levels
# I also want to make a map but how? alt codes maybe ???

# Inventory System - David Lunt
# https://stackoverflow.com/questions/32486754/i-want-to-make-an-inventory-system-for-my-game-in-python-v-3-4-3

# Imports
import sys, time, os, random

# Login
print(f'\n{"-"*36}\nWelcome to the Text RPG login screen\n{"-"*36}\n') 
username_create = input('Please set a username: ')
password_create = input('Please set a password: ')
print (f'User Creation Successful.\n')


user_login = input('Enter Username: ')
if user_login == username_create:
    print(f'Initiating Login for {username_create}')
    time.sleep(1.5)
if user_login != username_create:
    print('User is not registered.')

count = 0
while count < 3:
    user_login_pw = input('Enter Password: ')
    if user_login_pw == password_create:
        print ('Password Accepted')
        break
    if user_login_pw != password_create:
        print('Incorrect Password, Try Again.')
        count += 1
    if count == 3:
        exit()

print (f'WELCOME {username_create} TO TEXT RPG V 1.1\n') 
os.system("start F:\Python\Adventure.mp3")

'''
# Items: 
health_potion = 0 # Multiple types?
mana_potion = 0 # ??? Maybe

# Weapons
sword = 0 # Different Tiers with Different Attack Values 1-3, 4-6, 6-9, etc
'''
class Weapon:
    # A simple class
    # attribute
    attr1 = 'Wooden'
    attr2 = 'Bronze'
    attr3 = 'Iron'
    attr4 = 'Emerald'
    attr5 = 'Steel'
    attr6 = 'Sapphire'
    attr7 = 'Diamond'
    attr8 = 'Dragon Slayer'
    attr9 = 'Enchanted'


# Driver code
# Object instantiation
weapon = Weapon()

# Accessing class attributes
# and method through objects
#print (f'{Sword_1.attr1} Sword')

'''
bow = 0 # Different Arrows with Different Effects

shield = 0 # Different Defence Values

# Level up Feature - Increase stats in certain areas of choice..
level = 1
lvl = level

# Stats
health_points = 20
hp = health_points

mana_points = 20
mp= mana_points

attack = 1 # Chance to deal more damage (also increased by sword)-(Rate of 0.25 for each point - Needs 4 points to choose)

defence = 0 # Chance to block (also increased by shield)-(Rate of 0.25 for each point - Needs 4 points to choose)
'''

# Slow Text Reference
'''
typing_speed = 50 #wpm
def slow_type(t):
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(random.random()*10.0/typing_speed)
    print ('')
'''

# Sprint Text Reference
'''
def sprint(t):
    for c in str + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(3./90)
    print('')
sprint()
'''

############################
##                        ##
##        Chapter 1       ##
##        Prologue        ##
##                        ##
############################

# Start Gap
print(f'{"-"*36}\nPrologue\n{"-"*36}\n')

# Actual Start
typing_speed = 50 #wpm
def slow_type(text):
    for letter in text:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(random.random()*10.0/typing_speed)
    print('')

slow_type(f'''In a world not so far away from ours...
But vastely different in terms of survival...
A hero is born!
The Hero goes about his normal day to day life training to
be a baker. One day his life is uprooted when his little 
sister interveins by throwing some raw dough (flour) at him.

The young hero was furious... he unleashed a godly laughter as
he chased his sister around with the {weapon.attr1} Rolling Pin!''')