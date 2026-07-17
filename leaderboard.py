import json
import customtkinter as ctk

def save_data(data):
  # Safely write updated database records to the disk file
  with open("players.json", "w") as file:
    json.dump(data, file, indent=4)

def load_data():
  # Safely retrieve local database records from the disk file
  try:
    with open("players.json", "r") as file:
      return json.load(file)
  except FileNotFoundError:
    # Fallback to prevent crash if players.json hasn't been created yet
    return []

class Leaderboard:
  def __init__(self):
    # Dynamically pull the live file data on instantiation
    self.entries = load_data() 

  def add_entry(self, player_id, name, score):
    # Validation checks to enforce system requirements
    if not isinstance(score, int) or score < 0:
      raise ValueError("Invalid score value")
      
    # Check if the player already exists to avoid duplication
    for player in self.entries:
      if player.get("player_id") == player_id:
        player["score"] = max(player["score"], score)
        self.update_rankings()
        save_data(self.entries)
        return
        
    # Append new entry if no duplicate ID was discovered
    self.entries.append({
      "player_id": player_id,
      "name": name,
      "score": score,
      "rank": 0,
      "reward": "None"
    })
    self.update_rankings()
    save_data(self.entries)

  def update_rankings(self):
    # Algorithmic sorting based on player performance metrics
    self.entries.sort(key=lambda x: x.get("score", 0), reverse=True)
    for i, player in enumerate(self.entries):
      player["rank"] = i + 1
    self.assign_rewards()

  def assign_rewards(self):
    # Transaction state dictionary mapping milestones to specific store inventory items
    rewards = {1: "card_counter", 2: "theme_gold", 3: "theme_silver"}
    for player in self.entries:
      rank = player.get("rank")
      if rank in rewards:
        player["reward"] = rewards[rank]
