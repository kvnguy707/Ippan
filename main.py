import customtkinter as ctkfrom core_engine 
import Card, Deck, Player 
from data_handler import load_leaderboard, save_points
import daifugo
import blackjack

menu_options = {
  "1": "daifugo",
  "2": "blackjack",
  "3": "switch",
  "4": "liars_cards",
  "5": "leaderboard",
  "6": "shop",
  "7": "exit"
}

screen_routes = {
  "menu": ["game", "leaderboard", "shop"],
  "leaderboard": ["menu"],
  "shop": ["menu"],
  "game": ["menu"]
}

class MainApplication(ctk.CTk):
  # The main application class that acts as the window and coordinates screen states.
  def __init__(self, player_data=None):
    super().__init__()
    
    # initialise player data (fall back to default if none)
    if player_data:
      self.player_data = player_data 
    else:
      self.player_data = {"player_id": "P001", "points": 100}
    self.validate_player_data()
    
    # navigation & window state configurations
    self.current_screen = "menu"
    self.screen_history = []
    self.window_width = 800
    self.window_height = 600
    
    self.setup_window()
    self.render_current_screen()  # Upgraded from direct static call

  def setup_window(self):
    self.title("Card Game Hub")
    self.geometry(f"{self.window_width}x{self.window_height}")

  def clear_window(self):
    #Helper method to completely clear the UI before drawing a new view.
    for widget in self.winfo_children():
      widget.destroy()

  def render_current_screen(self):
    # Dynamic routing hub that decides which interface to render visually.
    self.clear_window()
    
    if self.current_screen == "menu":
      self.create_menu_widgets()
    elif self.current_screen == "game":
      self.create_game_selection_widgets()
    elif self.current_screen == "leaderboard":
      self.create_leaderboard_widgets()
    elif self.current_screen == "shop":
      self.create_shop_widgets()

  def create_menu_widgets(self):
    # Renders the primary Main Menu screen view.
    self.title_label = ctk.CTkLabel(self, text="Main Menu", font=("Arial", 24))
    self.title_label.pack(pady=20)
    
    self.play_button = ctk.CTkButton(self, text="Play Game", command=self.go_to_games)
    self.play_button.pack(pady=10)
    
    self.leaderboard_button = ctk.CTkButton(self, text="Leaderboard", command=self.go_to_leaderboard)
    self.leaderboard_button.pack(pady=10)
    
    self.shop_button = ctk.CTkButton(self, text="Shop", command=self.go_to_shop)
    self.shop_button.pack(pady=10)

  def create_game_selection_widgets(self):
    # Renders the interface showcasing your 4 core available card games.
    self.title_label = ctk.CTkLabel(self, text="Select a Card Game", font=("Arial", 24))
    self.title_label.pack(pady=20)

    # Creating buttons for your structural game components
    for game_key, game_name in menu_options.items():
      if game_key in ["1", "2", "3", "4"]: # Filter only actual gameplay types
        btn = ctk.CTkButton(
            self, 
            text=game_name.capitalise(), 
            command=lambda g=game_name: start_game(g, self.player_data["player_id"], "CPU")
        )
        btn.pack(pady=8)

    self.back_button = ctk.CTkButton(self, text="← Back to Menu", fg_color="gray", command=self.go_back)
    self.back_button.pack(pady=20)

def create_leaderboard_widgets(self):
  # Import inside the method to keep main load times lightweight
  from leaderboard import Leaderboard
  lb = Leaderboard()
  # Renders data layer records
  self.title_label = ctk.CTkLabel(self, text="Global Leaderboard", font=("Arial", 24))
  self.title_label.pack(pady=20)
  # Loop through entries and cleanly display top rows dynamically
  for player in lb.entries[:5]: 
    lbl = ctk.CTkLabel(self, text=f"Rank {player.get('rank', '-')}: {player.get('name', 'Unknown')} — {player.get('score', 0)} pts")
    lbl.pack(pady=4)
  # Back button goes cleanly at the bottom
  self.back_button = ctk.CTkButton(self, text="← Back to Menu", fg_color="gray", command=self.go_back)
  self.back_button.pack(pady=20)

  def create_shop_widgets(self):
    # Renders transactional interface layer details.
    self.title_label = ctk.CTkLabel(self, text="U-Choose Custom Shop", font=("Arial", 24))
    self.title_label.pack(pady=20)
    
    self.balance_label = ctk.CTkLabel(self, text=f"Your Balance: {self.player_data['points']} Points", font=("Arial", 16))
    self.balance_label.pack(pady=10)

    self.back_button = ctk.CTkButton(self, text="← Back to Menu", fg_color="gray", command=self.go_back)
    self.back_button.pack(pady=20)

  def change_screen(self, new_screen):
    if self.current_screen != new_screen:
      self.screen_history.append(self.current_screen)
      self.current_screen = new_screen
      self.render_current_screen() # Refreshes display interface instantly

  def go_back(self):
    if len(self.screen_history) > 0:
      self.current_screen = self.screen_history.pop()
    else:
      self.current_screen = "menu"
    self.render_current_screen() # Refreshes display interface instantly

  def go_to_games(self):
    self.change_screen("game")
    print("navigating to games menu")
      
  def go_to_leaderboard(self):
    self.change_screen("leaderboard")
    print("navigating to leaderboard")
      
  def go_to_shop(self):
    self.change_screen("shop")
    print("navigating to shop")

  def validate_player_data(self):
    if not isinstance(self.player_data, dict):
      raise ValueError("invalid player data")
    if "points" in self.player_data and self.player_data["points"] < 0:
      raise ValueError("invalid points value")


def start_game(game_id, player_id, mode):
  # game initialisation wrapper function
  print(f"initialising {game_id} for {player_id} in mode: {mode}")
  # Realising OOP components during initialisations:
  # game_deck = Deck()
  # active_player = Player(player_id)


if __name__ == "__main__":
  # ensure customtkinter styling is set correctly
  ctk.set_appearance_mode("system")
  ctk.set_default_color_theme("blue")
  
  # instantiate and launch the functional application
  app = MainApplication()
  app.mainloop()
