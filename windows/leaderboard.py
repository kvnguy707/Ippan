import json

# Example leaderboard
leaderboard = {
  "P001": {
    "username": "Alice",
    "points": 1500,
    "games_played": 25,
    "wins": 15,
    "rank": 1
  },
  "P002": {
    "username": "Bob",
    "points": 1200,
    "games_played": 30,
    "wins": 10,
    "rank": 2
  }
}

def save_data(data):
  with open("players.json", "w") as file:
    json.dump(data, file, indent=4)

def load_data():
  try:
    with open("players.json", "r") as file:
      return json.load(file)
  except FileNotFoundError:
    return []

class Leaderboard:
  def __init__(self):
    self.entries = load_data() 

  def add_entry(self, player_id, name, points, wins=0, games=0):
    if not isinstance(points, int) or points < 0:
      raise ValueError("Invalid points value")
          
    for player in self.entries:
      if player.get("player_id") == player_id:
        player["points"] = max(player.get("points", 0), points)
        player["wins"] = player.get("wins", 0) + wins
        player["games"] = player.get("games", 0) + games
        self.update_rankings()
        save_data(self.entries)
        return
              
    self.entries.append({
      "player_id": player_id,
      "name": name,
      "points": points, 
      "wins": wins,
      "games": games,
      "rank": 0,
      "reward": "None",
      "inventory": []
    })
    self.update_rankings()
    save_data(self.entries)

  def update_rankings(self):
    self.entries.sort(key=lambda x: x.get("points", 0), reverse=True)
    for i, player in enumerate(self.entries):
      player["rank"] = i + 1
    self.assign_rewards()

  def assign_rewards(self):
    rewards = {1: "card_counter", 2: "theme_gold", 3: "theme_silver"}
    for player in self.entries:
      rank = player.get("rank")
      if rank in rewards:
        player["reward"] = rewards[rank]
