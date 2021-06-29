# I want to make an RPG Game based sorta like Legend of Zelda but, with levels
# I also want to make a map but how? alt codes maybe ???

# Inventory System - David Lunt
# https://stackoverflow.com/questions/32486754/i-want-to-make-an-inventory-system-for-my-game-in-python-v-3-4-3

# Imports
import sys, time, os, random, pickle, items
import os.path
# Check if the file to save has been created.
file_exists = os.path.isfile("loadfile.txt")

# Load the text file
def load():
    if file_exists:
        file = open("loadfile.txt", "r")
        room = file.read()
        file.close()
    else:
        room = "Start Room"

    roomchooser(room)

# Save the file
def save(s):
    file = open ("loadfile.txt", "w")
    file.write(s)
    file.close()
    
'''
# Set the correct starting room
def Tutorial(room):
    if room == "Tutorial":
        startroom()


def startroom():
    s = "Tuturial"
    save(s)
    print("You are in a hallway, you could go left or right"
    direction = input()
    if direction == "right":
        secondroom()
    quit()
'''




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

# Level Selection
# Tutorial 
# Story 1
# Story 2
# Story 3


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

slow_type(f'''Phobotane is a world of peace and prosperity. It is a 
land in which all races live together in harmony. 
The gnomes build their machines and live among
the humans. Elves run the academies in which
people come to learn. Ogres have no qualms
living in the same town as humans or gnomes.
Yet, all is not well.

You are {username_create}, a human alchemist in the
kingdom of Kuzos. You've lived in the town of
Gerzona your entire life. You've been training in
the local alchemist guild and have come to be a 
respected member of the guild. The town is small,
but it's enough to keep you busy. The town is
surrounded by a wall to protect it from enemy
attack. ''')