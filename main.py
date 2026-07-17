import customtkinter as ctk
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
  # The main application class that acts as the window and coordinates screen states
  def __init__(self, player_data=None):
    super().__init__()
    
    # Initialise player data (fall back to default if none)
    if player_data:
      self.player_data = player_data 
    else:
      self.player_data = {"player_id": "P001", "points": 100}
    self.validate_player_data()
    
    # Navigation & window state configurations
    self.current_screen = "menu"
    self.screen_history = []
    self.window_width = 800
    self.window_height = 600
    
    self.setup_window()
    self.render_current_screen()

  def setup_window(self):
    self.title("Card Game Hub")
    self.geometry(f"{self.window_width}x{self.window_height}")

  def clear_window(self):
    # Helper method to completely clear the UI before drawing a new view
    for widget in self.winfo_children():
      widget.destroy()

  def render_current_screen(self):
    # Dynamic routing hub that decides which interface to render visually
    self.clear_window()
    
    if self.current_screen == "menu":
      self.create_menu_widgets()
    elif self.current_screen == "game":
      self.create_game_selection_widgets()
    elif self.current_screen == "leaderboard":
      self.create_leaderboard_widgets()
    elif self.current_screen == "shop":
      self.create_shop_widgets()

  # ––– Main Menu Screen –––
  
  def create_menu_widgets(self):
    # Renders the primary Main Menu screen view
    self.title_label = ctk.CTkLabel(self, text="Main Menu", font=("Arial", 24))
    self.title_label.pack(pady=20)
    
    self.play_button = ctk.CTkButton(self, text="Play Game", command=self.go_to_games)
    self.play_button.pack(pady=10)
    
    self.leaderboard_button = ctk.CTkButton(self, text="Leaderboard", command=self.go_to_leaderboard)
    self.leaderboard_button.pack(pady=10)
    
    self.shop_button = ctk.CTkButton(self, text="Shop", command=self.go_to_shop)
    self.shop_button.pack(pady=10)

  # ––– Game Selection –––
  
  def create_game_selection_widgets(self):
    # Renders the interface showcasing your 4 core available card games
    self.title_label = ctk.CTkLabel(self, text="Select a Card Game", font=("Arial", 24))
    self.title_label.pack(pady=20)

    # Creating buttons for structural game components
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

  # ––– Leaderboard GUI –––
  
  def create_leaderboard_widgets(self):
    from leaderboard import Leaderboard
    lb = Leaderboard()
    self.title_label = ctk.CTkLabel(self, text="Global Leaderboard", font=("Arial", 24, "bold"))
    self.title_label.pack(pady=20)
    # Dictionary mapping top ranks to custom podium colors
    podium_colors = {1: "#FFD700", 2: "#C0C0C0", 3: "#CD7F32"}
    # Loop through entries and cleanly display top rows dynamically
    for player in lb.entries[:5]: 
      rank = player.get("rank", "-")
      name = player.get("name", "Unknown")
      points = player.get("points", 0)
      text_display = f"Rank {rank}: {name} — {points} pts"
      # Add-on: Dynamic color selection for the podium rankings
      text_color = podium_colors.get(rank, "white")
      font_style = ("Arial", 14, "bold") if rank in podium_colors else ("Arial", 14)
      
      lbl = ctk.CTkLabel(self, text=text_display, font=font_style, text_color=text_color)
      lbl.pack(pady=6)

    self.back_button = ctk.CTkButton(self, text="← Back to Menu", fg_color="gray", command=self.go_back)
    self.back_button.pack(pady=25)

  # ––– Shop GUI –––
  
  def create_shop_widgets(self):
    from shop import default_shop_data
    self.title_label = ctk.CTkLabel(self, text="U-Choose Custom Shop", font=("Arial", 24))
    self.title_label.pack(pady=20)
    self.balance_label = ctk.CTkLabel(self, text=f"Your Balance: {self.player_data['points']} Points", font=("Arial", 16))
    self.balance_label.pack(pady=10)
    self.status_label = ctk.CTkLabel(self, text="", font=("Arial", 12), text_color="green")
    self.status_label.pack(pady=5)
    
    # Dynamic GUI generation 
    for item_id, item in default_shop_data["shop_items"].items():
      frame = ctk.CTkFrame(self)
      frame.pack(pady=8, fill="x", padx=40)
      # Displaying Item name, type, price, and description line items
      text_info = f"{item['name']} ({item['type'].capitalize()})\n— {item['description']} —"
      lbl = ctk.CTkLabel(frame, text=text_info, font=("Arial", 13), justify="left")
      lbl.pack(side="left", padx=20, pady=10)
      # Price tag badge element display helper
      price_lbl = ctk.CTkLabel(frame, text=f"{item['price']} pts", font=("Arial", 13, "bold"))
      price_lbl.pack(side="right", padx=10)
      # GUI button for purchases
      btn = ctk.CTkButton(frame, text="Buy", width=80, command=lambda target_item=item_id: self.execute_shop_purchase(i))
      btn.pack(side="right", padx=10, pady=10)

    self.back_button = ctk.CTkButton(self, text="← Back to Menu", fg_color="gray", command=self.go_back)
    self.back_button.pack(pady=20)

  # GUI for showing successful purchases and shop GUI
  def execute_shop_purchase(self, target_id):
    from shop import default_shop_data, purchase_item
    result = purchase_item(self.player_data["player_id"], target_id)
    # Change status color to red if purchase fails 
    if "successful" in result:
      self.status_label.configure(text=result, text_color="green")
      self.player_data["points"] -= default_shop_data["shop_items"][target_id]["price"]
      self.balance_label.configure(text=f"Your Balance: {self.player_data['points']} Points")
    else:
      self.status_label.configure(text=result, text_color="red") 
  
    if __name__ == "__main__":
      from shop import initialise_database
      # Run the database check first to ensure safety
      initialise_database()
      # Boot up the window application loop
      app = MainApplication()
      app.mainloop()

  # ––– Window Management –––
  
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
    # Game initialisation wrapper function
    print(f"initialising {game_id} for {player_id} in mode: {mode}")
    # Realising OOP components during initialisations:
      # game_deck = Deck()
      # active_player = Player(player_id)


if __name__ == "__main__":
  # Ensure customtkinter styling is set correctly
  ctk.set_appearance_mode("system")
  ctk.set_default_color_theme("blue")
  
  # Instantiate and launch the functional application
  app = MainApplication()
  app.mainloop()
