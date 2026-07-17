import os
import json
from leaderboard import load_data, save_data

# Exemplar catalogs and player data
default_shop_data = {
  "shop_items": {
    "card_counter": {
      "name": "Card Counter",
      "price": 500,
      "type": "privilege",
      "description": "Tracks played cards in Daifugo"
    },
    "gold_theme": {
      "name": "Gold Theme",
      "price": 300,
      "type": "aesthetic",
      "description": "Changes UI colour scheme"
    }
  },
  "current_player": "P001",
  "player_points": 1000,
  "player_inventory": []
}

def initialize_database():
  # Ensures players.json exists with a valid default structure on startup.
  file_path = "players.json"
  
  # Only create the file if it doesn't already exist
  if not os.path.exists(file_path):
    default_data = [
      {
        "player_id": "P001",
        "name": "Ace",
        "score": 1200,
        "wins": 5,
        "games": 10,
        "rank": 1,
        "reward": "card_counter",
        "inventory": ["card_counter"]
      },
      {
        "player_id": "CPU_Easy",
        "name": "Charly Bot",
        "score": 450,
        "wins": 1,
        "games": 8,
        "rank": 2,
        "reward": "None",
        "inventory": []
      }
    ]
    with open(file_path, "w") as file:
      json.dump(default_data, file, indent=4)
    print("[System] Database initialized successfully with default records.")

def purchase_item(player_id, item_id):
  # Safely retrieve local database records from the disk file
  players = load_data()
  player = None
  
  # Locate current player record mapping
  for p in players:
    if p.get("player_id") == player_id:
      player = p
      break
          
  if not player:
    return "Error: Player profile not found"
      
  # Enforce schema structure health properties if missing from database
  if "points" not in player:
    player["points"] = default_shop_data["player_points"]
  if "inventory" not in player or not isinstance(player["inventory"], list):
    player["inventory"] = default_shop_data["player_inventory"]

  # Extract target configuration map from configuration items
  catalog = default_shop_data["shop_items"]

  # Validation Phase 1: Verify item existence in dictionary
  if item_id not in catalog:
    return "Invalid item selection"

  item = catalog[item_id]

  # Validation Phase 2: Check financial balance constraints
  if player["points"] < item["price"]:
    return "Not enough points"

  # Validation Phase 3: Enforce ownership limits (Privileges/Aesthetics are typically one-time items)
  if item_id in player["inventory"]:
    return "Item already owned"

  # Execution Phase: Update data structures
  player["points"] -= item["price"]
  player["inventory"].append(item_id)
  
  # Save the updated matrix state dynamically back to disk records
  save_data(players)
  return "Purchase successful"
