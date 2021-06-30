# I want to make an RPG Game based sorta like Legend of Zelda but, with levels
# I also want to make a map but how? alt codes maybe ???

# Inventory System - David Lunt
# https://stackoverflow.com/questions/32486754/i-want-to-make-an-inventory-system-for-my-game-in-python-v-3-4-3

# Imports
import sys, time, os, random, pickle, items
import os.path

# Check if the file to save has been created.
file_exists = os.path.isfile("loadfile.txt")

# Load the text file (Bring down to save below us once working ...)
def load():
    if file_exists:
        file = open("loadfile.txt", "r")
        room = file.read()
        file.close()
    else:
        room = "Start Room"

#===================================================================#
# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = #
#===================================================================#

# Save the file
def save(s):
    file = open ("loadfile.txt", "w")
    file.write(s)
    file.close()

#===================================================================#
# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = #
#===================================================================#

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

#===================================================================#
# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = #
#===================================================================#

############################
##                        ##
##         Welcome        ##
##                        ##
############################


print (f'WELCOME {username_create} TO TEXT RPG V 1.1\n') 
os.system("start F:\Python\Adventure.mp3")

#===================================================================#
# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = #
#===================================================================#

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

#===================================================================#
# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = #
#===================================================================#

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

Levels = ['Tutorial, Main Story, Veillantif']
Tutorial = "Tutorial"
Story_1 = "Phobotane"
Story_2 = "Veillantif"

# Typing Speeds

typing_speed = 50 #wpm
def slow(text):
    for letter in text:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(random.random()*10.0/typing_speed)
    print('')

def normal(text):
    for letter in text:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(random.random()*6.0/typing_speed)
    print('')

def sprint(text):
    for letter in text:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(random.random()*3.0/typing_speed)
    print('')

#===================================================================#
# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = #
#===================================================================#

Game_Start = input(f"Please choose a Level - {Levels}: ")
print('\n')
while True:
    if Game_Start == Tutorial:
        slow(f'''
Welcome to the Tutorial!
Here you will understand the in and out of the game.''')
        break

    # Start Gap
    if Game_Start == Story_1:
        print(f'{"-"*36}\nPrologue\n{"-"*36}\n')

        slow(f'''
        Phobotane is a world of peace and prosperity. It is a 
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
        break
    
    if Game_Start == Story_2:
        print(f'{"-"*36}\nPrologue\n{"-"*36}\n')

        slow(f'''
For Zelani the Dragon, the ancient world of Veillantif is a 
dangerous one. Her friends, Marque the Cavernstrike and Sinon 
the Werewolf, fair no better. Creatures like them are hunted 
ceaselessly, leaving orphans and ghost towns in the human's wake.

Like her father, she wishes to change the human's mind about 
Varelsians. To fix what went wrong in the past. Though, it's tough 
when humans only see you as a blood bag.
''')
        normal(f'''
In eras past,testing speed testing speed testing speed...''')
        break

    else:
        print("Incorrect Selection")