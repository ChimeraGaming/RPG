import random
import time

# Define adventurer stats and backstory
adventurer = {'name': 'Arin', 'health': 100, 'attack': 10, 'defense': 5,
              'backstory': "In the ancient world, there was a belief that the gods occasionally descended from their heavenly abode to walk among mortals and bestow blessings upon them. \n\nOne such descendant was a young adventurer named Arin. Arin's lineage could be traced back to one of the most powerful deities in the pantheon. \n\nHis great-great-great-grandmother was said to have been impregnated by the god himself, and from that union, Arin's family was born. \n\nFrom a young age, Arin showed signs of his divine heritage. He was faster, stronger, and more agile than the other children in his village. He also had an uncanny ability to sense danger and a remarkable talent for strategy and planning. \n\nAs he grew older, Arin became restless. He knew that he was destined for greatness and was determined to prove himself worthy of his divine heritage. He left his village and set out on a journey to explore the world and make a name for himself.\n"}

# Define enemy stats
enemy = {'name': 'Goblin', 'health': 50, 'attack': 5, 'defense': 2}

# Define a function to simulate a battle between adventurer and enemy
def battle(adventurer, enemy):
    backstory_lines = adventurer['backstory'].split('\n\n')
    for line in backstory_lines:
        print(line)
        time.sleep(2)
    
    print('A', enemy['name'], 'has appeared!')
    time.sleep(2)
    
    # Loop until either adventurer or enemy's health reaches zero
    while adventurer['health'] > 0 and enemy['health'] > 0:
        # Calculate adventurer's attack and enemy's defense
        adventurer_attack = random.randint(1, adventurer['attack'])
        enemy_defense = random.randint(1, enemy['defense'])
        damage = adventurer_attack - enemy_defense
        
        # If adventurer's attack is successful, subtract damage from enemy's health
        if damage > 0:
            enemy['health'] -= damage
            print(adventurer['name'], 'hits', enemy['name'], 'for', damage, 'damage!')
            time.sleep(2)
        
        # If enemy's health reaches zero, adventurer wins
        if enemy['health'] <= 0:
            print('\n', adventurer['name'], 'defeats', enemy['name'], 'and wins the battle!')
            time.sleep(2)
            break
        
        # Calculate enemy's attack and adventurer's defense
        enemy_attack = random.randint(1, enemy['attack'])
        adventurer_defense = random.randint(1, adventurer['defense'])
        damage = enemy_attack - adventurer_defense
        
        # If enemy's attack is successful, subtract damage from adventurer's health
        if damage > 0:
            adventurer['health'] -= damage
            print(enemy['name'], 'hits', adventurer['name'], 'for', damage, 'damage!')
            time.sleep(2)
        
        # If adventurer's health reaches zero, enemy wins
        if adventurer['health'] <= 0:
            print('\n', enemy['name'], 'defeats', adventurer['name'], 'and wins the battle!\n\n')
            time.sleep(2)
            break

# Call the battle function
battle(adventurer, enemy)

# Print
print()