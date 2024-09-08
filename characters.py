#Imports
import json
import csv
#Functions
def update_player():
    characters = {
    'wizard': {'emoji': '🧙‍♂️', 'attack_strength': 10, 'health': 100, 'type': 'enemy'},
    'vampire': {'emoji': '🧛', 'attack_strength': 30, 'health': 80, 'type': 'enemy'},
    'dragon': {'emoji': '🐉', 'attack_strength': 50, 'health': 150, 'type': 'enemy'},
    'goblin': {'emoji': '👹', 'attack_strength': 5, 'health': 20, 'type': 'enemy'},
    'troll': {'emoji': '👹', 'attack_strength': 40, 'health': 120, 'type': 'enemy'},
    'necromancer': {'emoji': '🧟', 'attack_strength': 25, 'health': 70, 'type': 'enemy'},
    'assassin': {'emoji': '🗡️', 'attack_strength': 40, 'health': 30, 'type': 'enemy'},
    'behemoth': {'emoji': '🦍', 'attack_strength': 60, 'health': 200, 'type': 'enemy'},
    'phantom': {'emoji': '👻', 'attack_strength': 20, 'health': 40, 'type': 'enemy'},
    'mimic': {'emoji': '🪙', 'attack_strength': 20, 'health': 50, 'type': 'enemy'},
    'sorcerer': {'emoji': '🧙', 'attack_strength': 15, 'health': 60, 'type': 'enemy', 'spell': 'fireball'},
    'golem': {'emoji': '🪨', 'attack_strength': 10, 'health': 200, 'type': 'enemy'},
    'healer': {'emoji': '💉', 'amount': 100, 'type': 'ally'},
    'warrior': {'emoji': '🗡️', 'attack_strength_boost': 10, 'type': 'ally'},
    'rogue': {'emoji': '🗝️', 'type': 'ally'},
    'sage': {'emoji': '🧙', 'type': 'ally'},
    'alchemist': {'emoji': '⚗️', 'type': 'ally'},
    'merchant': {'emoji': '🛒', 'type': 'ally'},
    'treasure': {'emoji': '💰', 'gold': 100, 'type': 'item'},
    'magic_wand': {'emoji': '✨', 'type': 'item', 'spell': 'lightning'},
    'scroll_of_wisdom': {'emoji': '📜', 'type': 'item'},
    'bag_of_gold': {'emoji': '💰', 'gold': 50, 'type': 'item'},
    'elixir': {'amount': 50, 'attack_strength_boost': 5, 'emoji': '🧪', 'type': 'potion'},
    'shield': {'amount': 20, 'emoji': '🛡️', 'type': 'item'},
    'cursed_object': {'amount': -20, 'emoji': '👁️', 'type': 'item'},
    'trap': {'damage': 10, 'emoji': '⚠️', 'type': 'trap'}
    }


def game_data(player):
    try:
        # Open a file in write mode
        with open('player_data.json', 'w') as file:
            # Serialize the player dictionary to a JSON formatted string and write it to the file
            json.dump(player, file, indent=4)
        print("Data saved successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")
        
def formatting(data):
    # Define the column widths
    widths = {
        'Class': 19,
        'Emoji': 1,
        'Attack_Strength': 3,
        'Health': 3,
        'Type': 10
    }

    # Create the header row
    header = f"""| {'Class'.ljust(widths['Class'])} | {'Emoji'.ljust(widths['Emoji'])} | {'Attack_Strength'.ljust(widths['Attack_Strength'])} | {'Health'.ljust(widths['Health'])} | {'Type'.ljust(widths['Type'])} |"""
    
    # Create a separator row based on column widths
    separator = f"""|{'-'*widths['Class']}|{'-'*widths['Emoji']}|{'-'*widths['Attack_Strength']}|{'-'*widths['Health']}|{'-'*widths['Type']}|"""
    
    string_list = [header, separator]  # Start with header and separator

    for row in data:
        Class = row[0]
        Emoji = row[1]
        Attack_Strength = row[2]
        Health = row[3]
        Type = row[4]

        # Create the formatted row
        string_list.append(
            f"""| {Class.ljust(widths['Class'])} | {Emoji.ljust(widths['Emoji'])} | {str(Attack_Strength).ljust(widths['Attack_Strength'])} | {str(Health).ljust(widths['Health'])} | {Type.ljust(widths['Type'])} |"""
        )

    return string_list  # Return the list of strings
