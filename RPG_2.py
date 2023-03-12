import random

# Define the player's initial stats
player_stats = {
    "name": "Player",
    "health": 100,
    "attack": 10,
    "defense": 5,
    "level": 1,
    "experience": 0,
    "gold": 0,
    "inventory": []
}

# Define the boss monster's stats
boss_stats = {
    "name": "Boss",
    "health": 200,
    "attack": 20,
    "defense": 10
}

# Define the different enemy types
enemy_types = {
    "Goblin": {"health": 20, "attack": 5, "defense": 2},
    "Skeleton": {"health": 30, "attack": 10, "defense": 5},
    "Orc": {"health": 40, "attack": 15, "defense": 8},
    "Dragon": {"health": 100, "attack": 25, "defense": 15}
}

# Define the different items
item_types = {
    "Potion": {"health": 20},
    "Sword": {"attack": 5},
    "Shield": {"defense": 5}
}

# Define the different levels and the enemies that appear on each level
levels = {
    1: ["Goblin", "Skeleton"],
    2: ["Orc", "Skeleton"],
    3: ["Dragon", "Orc"]
}

# Define a function to display the player's stats
def display_stats(stats):
    print("Name:", stats["name"])
    print("Level:", stats["level"])
    print("Health:", stats["health"])
    print("Attack:", stats["attack"])
    print("Defense:", stats["defense"])
    print("Experience:", stats["experience"])
    print("Gold:", stats["gold"])
    print("Inventory:", stats["inventory"])

# Define a function to fight an enemy
def fight_enemy(enemy_type):
    enemy_stats = enemy_types[enemy_type]
    print("You are fighting a", enemy_type)
    while player_stats["health"] > 0 and enemy_stats["health"] > 0:
        # Player attacks first
        enemy_stats["health"] -= player_stats["attack"] - enemy_stats["defense"]
        if enemy_stats["health"] <= 0:
            print("You defeated the", enemy_type)
            player_stats["experience"] += 10
            player_stats["gold"] += 5
            # Chance to drop an item
            if random.randint(1, 10) <= 3:
                item_type = random.choice(list(item_types.keys()))
                item_stats = item_types[item_type]
                player_stats["inventory"].append(item_type)
                for stat, value in item_stats.items():
                    player_stats[stat] += value
                print("The", enemy_type, "dropped a", item_type)
            break
        # Enemy attacks next
        player_stats["health"] -= enemy_stats["attack"] - player_stats["defense"]
        if player_stats["health"] <= 0:
            print("You were defeated by the", enemy_type)
            return False
    return True

# Define a function to display the items in the player's inventory
def display_inventory():
    print("Inventory:")
    for item in player_stats["inventory"]:
        print(item)

# Define the game loop
while player_stats["health"] > 0 and boss_stats["health"] > 0:
    # Check if the player has reached the boss level
    if player_stats["level"] == len(levels):
        print("You have reached the final level!")
        print("Prepare to face the boss", boss_stats["name"])
        input("Press Enter to continue...")
        # Fight the boss
        while player_stats["health"] > 0 and boss_stats["health"] > 0:
            # Player attacks first
            boss_stats["health"] -= player_stats["attack"] - boss_stats["defense"]
            if boss_stats["health"] <= 0:
                print("Congratulations! You have defeated the boss and completed the game!")
                break
            # Boss attacks next
            player_stats["health"] -= boss_stats["attack"] - player_stats["defense"]
            if player_stats["health"] <= 0:
                print("You were defeated by the boss")
                break
    else:
        # Get the list of enemies for the current level
        level_enemies = levels[player_stats["level"]]
        # Fight each enemy in the level
        for enemy in level_enemies:
            if not fight_enemy(enemy):
                # Player was defeated
                break
        else:
            # Player defeated all enemies in the level
            print("You have completed level", player_stats["level"])
            player_stats["level"] += 1
            player_stats["experience"] += 20
            player_stats["gold"] += 10
            # Chance to get a random item
            if random.randint(1, 10) <= 5:
                item_type = random.choice(list(item_types.keys()))
                item_stats = item_types[item_type]
                player_stats["inventory"].append(item_type)
                for stat, value in item_stats.items():
                    player_stats[stat] += value
                print("You found a", item_type)
    # Display the player's stats and inventory
    display_stats(player_stats)
    display_inventory()
    input("Press Enter to continue...")

