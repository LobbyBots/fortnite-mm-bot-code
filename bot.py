import json
import time
import random

# Load the JSON configuration from the config.json file
with open('config.json', 'r') as config_file:
    config = json.load(config_file)

def simulate_error():
    error_types = [
        "Invalid auth code",
        "Incorrect device auths",
        "Config variable not set"
    ]
    error = random.choice(error_types)
    
    if error == "Config variable not set":
        # Remove a random config variable and its contents
        variable = random.choice(list(config.keys()))
        if config[variable] is not None:
            config[variable] = None
            print(f"[BOT-LOBBIES] Error: {error} - Removed '{variable}' from the config")
    else:
        print(f"[BOT-LOBBIES] Error: {error}")
    
    exit(1)

print("[BOT-LOBBIES] Starting fortnite bot!")

total_items = len(config)
progress = 0

for key, value in config.items():
    # Calculate the percentage progress
    progress += 1
    percentage = (progress / total_items) * 100

    # Print "Starting up" messages with percentages
    if progress >= 3 and random.random() < 0.1:
        simulate_error()  # Simulate errors after loading a few variables
    else:
        print(f"[BOT-LOBBIES] Starting up... {percentage:.0f}%")
        print(f"[BOT-LOBBIES] {key} set to {value}. {percentage:.0f}%/{total_items}")

    # Pause for a moment to simulate the bot configuration process
    time.sleep(1)

print("[BOT-LOBBIES] Process failed! API is down!")
