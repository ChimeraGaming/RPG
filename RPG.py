# I want to make an RPG Game based sorta like Legend of Zelda but, with levels
# I also want to make a map but how? alt codes maybe ???

# Inventory System Referance - David Lunt
# https://stackoverflow.com/questions/32486754/i-want-to-make-an-inventory-system-for-my-game-in-python-v-3-4-3

# Imports
import sys, time, os, random

# Login
print('\nWelcome to the Text RPG login screen') 
username_create = input('Please set a username: ')
password_create = input('Please set a password: ')

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

'''
# Items: 
health_potion = 0 # Multiple types?
mana_potion = 0 # ??? Maybe

# Weapons
sword = 0 # Different Tiers with Different Attack Values 1-3, 4-6, 6-9, etc
'''
def sword_1(RollingPin):
    name = 'Rolling Pin'
    value = 5
    damage =10

def sword_2(WoodenSword):
    name = 'Wooden Sword'
    value = 10
    damage = 25
'''
bow = 0 # Different Arrows with Different Effects

sheild = 0 # Different Defence Values

# Level up Feature - Increase stats in certain areas of choice..
level = 1
lvl = level

# Stats
health_points = 20
hp = health_points

mana_points = 20
mp= mana_points

attack = 1 # Chance to deal more damage (also increased by sword)-(Rate of 0.25 for each point - Needs 4 points to choose)

defence = 0 # Chance to block (also increased by sheild)-(Rate of 0.25 for each point - Needs 4 points to choose)
'''

# Slow Text Referance
'''
typing_speed = 50 #wpm
def slow_type(t):
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(random.random()*10.0/typing_speed)
    print ('')
'''

# Sprint Text Referance
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
print('\n')

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
A hero is born!''' (time.sleep(3)),
'''The Hero goes about his normal day to day life training to
be a baker. One day his life is uprooted when his little 
sisted interviens by throwing some raw dough (flour) at him.

The young hero was furious... he unleashed a godly laughter as
he chased his sister around with the {sword_1}!''' (time.sleep(1.5)))
