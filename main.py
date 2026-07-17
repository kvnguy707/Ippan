def start_game(game_id, player_id, mode):
  if not validate_player(player_id):
    return error
    settings = game_settings[game_id]
    deck = create_deck(settings)
    players_session = init_players(player_id, settings)
    if mode == "CPU": 
      assign_CPU_behaviour(players_session, CPU_weights)
      save_session_temp(players_session)
      open_game_window(game_id, players_session, deck)

main_window = {
    "current_screen": "menu",
    "selected_option": None,
    "player_id": "P001",
    "running": True,
    "screen_history": [],
    "window_width": 800,
    "window_height": 600
}

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

if selected_option in menu_options:
    current_screen = menu_options[selected_option]
