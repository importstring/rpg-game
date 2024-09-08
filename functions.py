from navigation import get_user_input
from edge_cases import special_keys
import csv
def cycle_through_options(question, options, data):
    a = 0
    num_options = len(options)

    while True:
        # Clear the screen and display the prompt and options
        print("\033c", end='')  # ANSI escape sequence to clear the screen
        for i, option in enumerate(options):
            prefix = '-> ' if i == a else '   '
            print(f'{prefix}{option}')

        # Get user input
        raw_input = get_user_input(f'{question}?\n> ')
        command = special_keys(raw_input)  # Filter input as needed

        # Debug prints
        print(f"Raw input: {raw_input}")
        print(f"Command: {command}")

        # Update the cursor position based on command
        if command == 'Arrow Up':
            a -= 1
            if a < 0:
                a = num_options - 1  # Wrap around to the last option
        elif command == 'Arrow Down':
            a += 1
            if a >= num_options:
                a = 0  # Wrap around to the first option
        elif command == 'Enter':
            print('Success')
            return data[a]  # Return the selected option
        else:
            continue


def read_csv(filename):
    data = []
    with open(filename, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)  # Use csv.reader
        next(reader)  # Skip the header row
        for row in reader:
            data.append(row)  # Append each row as a list
    return data

        
def write_player_data(Player_name, Player_class, Attack_strength, Health, Type):
    with open('players.csv', mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([Player_name, Player_class, Attack_strength, Health, Type])    

