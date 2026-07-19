# Ippan: Universal Multi-Game Card Engine
An interactive card game platform built with Python and Tkinkter/CustomTkinter featuring an immutable transactional economy, dynamic inventory system, and persistent algorithmic leaderboard. All with the help of architectures and concepts like: OOPs, JSON files, Dictionaries, and many more!

## Introduction
Ippan is a digital card game application that aims to bring together a collection of popular card games from all over the world into an engaging platform. It will focus on an array of card games that the player can choose from and Ippan’s multicultural approach to card games allows for diverse gameplay for audiences and its flexible rule set and additional cards also allow for unique gameplay to suit everyone's play style. 

I designed Ippan to unify several global card games into one cohesive platform. The name “Ippan” comes from the Japanese word for “general” or “universal”, reflecting my goal of creating a flexible, all-purpose card-game system. The project includes four games: Daifugō, Blackjack, Switch, and Liar’s Cards, each with its own rules, strategies, and playstyle. My intention was to create a system where players could seamlessly switch between games without feeling like they were leaving the core application.

From the beginning, I realised this project was well‑suited to computational methods because card games rely heavily on structured data, logical rules, and predictable state changes. The turn‑based nature of the games also made them ideal for computational modelling. I originally tried tracking game state using several separate Boolean variables, but this became confusing and error-prone, especially in Daifugō, where different game states can overlap. 

There will also be a self-sorting ranking system, where each player can view their standing against other players. To access and keep track of all players’ ranks, Uju Points are used (deriving from the Korean word for Universe)  to determine their rank, and depending on their rank, players may win certain prizes and/or privileges. However, Uju Points can be lost with certain losses in certain games. This also can be handled with computational methods, such as file handling and saved game data. Uju Points can also be exchanged at the ‘U-Choose’ Shop. Here, players can exchange their Uju Points for certain in-game perks and also buy certain aesthetic items that can be used to customise their avatars, profiles, cards, etc.

The rules, structure, and decision-making processes within Ippan can all be expressed as algorithms and data manipulations. This makes the project highly amenable to a computational solution and demonstrates how programming can effectively simulate complex, rule-based games in a clear and logical way.

From a technical perspective, the project will be developed using Python, making use of object-oriented programming principles to ensure the program is modular, reusable, and easy to maintain. Core components such as the deck, cards, players, and game engine will be implemented as classes, allowing all four games to share the same foundational structures. Control flow, data structures (such as lists and dictionaries), and algorithms will be used to manage shuffling, dealing, turn order, scoring, and computer decision making. The program will also incorporate file handling to store scores or game data within text files.

For the general GUI, I will use a combination of Tkinter and CustomTkinter to adapt the game’s Python-based user interface into a more stylish and modern interface that the player can customise. Tkinter is an open source, standard GUI library that is included in Python. 

All these games come from real-life card games, as well as some digital renditions. For instance, Daifugō is popularised in Japan for its elaborate and flexible ruleset, and exists in some minigames, like Persona 5, namely translated to Tycoon. As well as Liar’s Bar in which the game Liar’s Cards draws inspiration from. These games helped draw my focus on a stylistic and well-rounded game that draws card games from multiple cultures, helping draw Ippan’s cohesive nature as a flexible, and well-rounded general card game.

Overall, Ippan demonstrates how multiple games can be integrated into a single coherent application through careful program design, abstraction, and code reuse, while showcasing key computational thinking skills such as decomposition, modularity, and algorithm design. Ippan demonstrates how multiple card games can be integrated into a single coherent application through modular design, abstraction, and code reuse. The project allowed me to apply computational thinking skills such as decomposition, algorithm design, and object‑oriented programming while also responding to real user feedback and debugging challenges.

## Game Descriptions
Ippan features the following four games:

### Daifugō (Tycoon): 2-4 players
Daifugō is a popular Japanese card game where the objective is to become the "Daifugō" (the tycoon) by playing cards in ascending order. Each player gets the mean number of cards (Uses standard deck plus 2 (optional), so e.g. For 3 players, each get 543=18 cards) distributed to them and aim to get rid of all their cards first by playing strictly stronger cards than their opponents, with the weakest card being 3 and going consecutively to 2, the strongest (3,4,5,6,7, ... , J,Q,K,A,2). The game has strategic elements such as the ability to pass their turn or play multiple cards of the same value (up to four cards).

Some cards have special actions, for instance:
* (Optional rule set) Eight: Skips everyone's turn and returns back to the player's turn, which is called an 'Eight Stop'. This card follows the general strength system. E.g. If three cards are placed down, three eights also have to be placed down which are stronger than the previous ones.
* Three of Spades: If a single Joker is placed down, then the three of spades is able to be placed down. This skips everyone's turn and returns the turn to the player. This is called a 'Three of Spades Reversal'. Follows general strength system.
* Joker: This is a wildcard that can be any value. This card can be played along any other cards of the same value, counting as a pair, triple, or quadruple. If played by itself, the only cards that can beat it are the three of spades or the Wonder card. In the strength system, this is the strongest card (above the 2).
* (Optional additional card) Wonder: There are only two of these in the deck. This can be played on any card(s), regardless of the amount or strength played. Once played, it skips everyone's turn and goes back to the player. Unlike the Joker card, however, the Wonder can only be played by itself, not with other cards. In the strength system, the Wonder has no strength nor weakness, and is therefore classed as a neutral card. If these cards are disabled, the cards are distributed unevenly, where the Beggar and/or Poor get the least amount.

If a player plays four cards of the same value, then it will trigger a Revolution by which the strength system will be reversed (3 becomes the strongest and 2 becomes the weakest). This allows for some strategic play, especially if a player initially has low cards in their hand. And if a player plays another four-of-a-kind during a revolution, it will trigger a Counter Revolution by which the strength system is put back to normal.

Players can also choose the rule set, Sequence, meaning that consecutive cards can be played, with a minimum of three cards, and a maximum six cards (where the player is able to modify this range). E.g. Players can put down a 4,5,6,7; or Q,K,A etc. They can also trigger a Sequence Revolution, where if  four consecutive cards of the same suit are played, it will trigger a Revolution. Similarly, playing four consecutive cards of the same suit during a Revolution will trigger a Counter Sequence Revolution, putting the strength system back to normal.

After each round (where the player can pick the number of rounds they wish to play), the ranks are tallied and trading occurs:

* Commoner: This is the initial rank that all players begin with.
* Beggar: Player in last rank who didn't play all their cards. They have to trade their two strongest cards (not including the Wonder card) to the Tycoon and receive 0 points.
* Poor: The player in third rank. They must trade one of their strongest cards (not including the Wonder card) to the Rich, and receive 10 points.
* Rich: The player in second rank. They must trade one card of their choice to the Poor, and receive 20 points.
* Tycoon: The player ranked first. They must trade two cards of their choice to the Beggar, and receive 30 points. Additionally, if they do not win first in the next round, they become 'bankrupt' and automatically become the Beggar.

These ranks apply for four players. If there are three, there is no Poor rank, each player must trade two cards in the direction of play. If there are two, then there is only the Beggar and Tycoon rank.

All these rules stated are set rules, whilst some other rules may be added or removed, allowing flexible gameplay.

### Blackjack Poker: 2+ players
Blackjack is a fast-paced, classic casino card game, usually based in America and/or Britain where the objective is to accumulate cards that total as close to 21 as possible, without going over. Players make an initial bet of Uju Points into the pot and after each round, players win the total amount of points in the pot. The game pits the player against the dealer (a CPU), and players can choose to ‘hit’ (draw another card) or ‘stand’ (keep their current hand) in a bid to have a higher total than the dealer, without busting. 

Number cards add their respective amounts to the total hand. Face cards add 10 and Aces add 1 or 11, depending if the addition causes a bust or not. Players start with two cards that only they can see. As such 52 cards are used in total with the standard rules. 

Players can add Jokers to the deck. Jokers can subtract 2 or add 12 to the total, again, depending if it will cause a bust or not. 

A hand that perfectly adds to 21 is called a Blackjack, and the player who has it automatically wins if nobody else has one. If more than one player has a Blackjack, they all will win a share of points that are put into the pot.

### Switch: 2+ players
Switch is a shedding-type card game (and is similar to Uno) where the goal is to be the first player to get rid of all your cards. Each player gets seven cards and the remaining deck is placed  in the center as the draw pile. Then place the top card of the draw pile face up to start the discard pile. The turn always initially starts clockwise, and players must place one card down that matches the suit or the rank. If they can't play, they must pick a card from the draw pile. If the card can be played, the player must play it, if not, their turn ends. Before a player plays their second to last card, they must call "Last Card". If they don't, other players can call them out, which makes them pick up two cards as a penalty.

Switch has special cards and rules:

* 2: The next player must draw 2 cards and skips their turn 

* (Optional) Stacking: When a player plays a 2, the next player can also play a 2, increasing the cards drawn by two. This keeps stacking until a player cannot play a 2, by which they must pick up the accumulated cards drawn.

* 8: Skips the next player's turn

* Jack: Reverses the direction of play

* King: Can be played on any card; the player chooses the suit that continues.

* Ace: Can be played on any card. Next player must draw four cards and the player who played it gets to change the suit that continues 

  * (Optional) Challenging: If a player has an Ace played on them, they can challenge the Ace to make the player pick up cards instead. When a player challenges, if the player who placed the Ace could have played a card before they placed the Ace, then the challenger wins and the person who played the Ace draws four cards and the challenger continues their turn. But if the player who placed the Ace could not have played a card before they placed the Ace, then the challenger loses and they must pick up six cards instead and their turn is skipped. 

Along with stacking, players can also stack Aces. When this happens, a player can still challenge. If the challenger wins, they receive only four cards (the first Ace in the stack) and the person challenged draws the remaining stacked cards (the other stacked Aces, not including the one the challenger got), then the challenger continues their turn. If they lose, then the challenger must draw all stacked cards plus an additional two and their turn is skipped.
  * E.g. Say three people put down an Ace (12 total cards to draw). The person who cannot stack another Ace challenges. If they are correct then they get 4 cards and the player who they challenged gets the remaining 8 cards. If they get it wrong, they must draw 14 cards.

* (Optional) Jokers: Can be placed on any card. When played, the player must say a suit of their choosing. The next player must draw cards face up until they draw a card of that suit that the player just chose (Jokers do not count). All cards drawn are added to their hand and their turn is skipped.

* (Optional) 7-Q Switch: Playing a Queen card swaps everyone's hands in the direction of play. When a 7 is played, the player can choose whose hand they want to swap with. 

* (Optional) 10-Burn: Playing a 10 'burns' the pile. The whole discard pile is cleared and the player takes another turn to put down whatever card they want. 

* (Optional) Switch: When two or more players are in a 'Last Card' state, one player can call 'Switch'. If more than one person calls 'Switch', then the first person who grabs a card from the draw pile gets the 'Switch'. During 'Switch', the player who called it must choose one of the people with one card left. If the person they chose has a playable card (not including non-number cards) then they must draw the card the caller picked. If they don't, then the caller must draw five cards, plus the one they picked. The person called on then places their card at the bottom of the draw pile and they draw another card.

### Liars Cards: 2-6 players
This is like a twist on the game Cheat, only with higher stakes. It plays with the same rules as Cheat, but only includes face cards, including the Aces and Jokers. The deck consists of six of Jacks, Queens, Kings, and Aces, with only two Jokers. Each player is given six cards. 

* A 'Table' will be randomly made, this determines the cards that can be played that round. E.g. if a 'Queens Table" is declared, only Queens can be played.
* Each player plays cards face down under the rules of the Table. Players can play multiple cards of the 'same value'.
* Jokers can be any card, so can be played alongside other cards.
* A player can claim they put down the appropriate card, but it is ultimately up to them if the decide to lie or not.
* If a player calls a lie, and it was indeed a lie, the player who was called on must play a minigame of Russian Roulette.
  * For the Russian Roulette minigame, a selection of six buttons will be present for the player to choose, one of which is rigged with an explosive. Choosing the wrong one leads to an 'Explosive Exit'. Players can choose how many buttons are rigged ranging from 1-5.
  * If they are eliminated, everyone's hands are reset, a new Table is picked, and the player is out of the game.
  * If they are not, everyone's hands are reset, a new Table is picked, and the player who did the Russian Roulette starts the round.

Like Cheat, the goal of the game is to discard all cards. If a player discards all before the others, they are safe from entering the Russian Roulette minigame. The overall goal is to be the last one standing.





## U-Choose Shop
The game features a fully persistent transaction layer that allows players to spend points earned in matches on profile enhancements.

### Features 
* *Decoupled Architecture:* The backend processing layer (`shop.py`) is completely separated from the rendering interface (`main.py`) to preserve clean state boundaries.
* *Fail-Safe Checks:*  The transaction engine runs three structural validations prior to modifying state records:
  * Catalogue Verification: Validates whether the requested item ID exists.
  * Financial Balance Check: Rejects transactions if player points fall below the item cost.
  * Duplicate Purchase Blocking: References item attributes (`"one_time": True`) to prevent double-spending on owned aesthetics or privileges.

### Validation Table
|Field / Variable|Validation Rule|Example Valid Input|Example Invalid Input|Validation Method|Justification|
| :--- | :--- | :--- | :--- | :--- | :--- |
|shop_items|Must be a non-empty nested dictionary with required fields name; price; type|`{"card_counter":{"price":500,"name":"Card Counter","type":"privilege"}}`|`{}` missing keys|Structure + key existence check|Ensures all items are properly defined and usable|
|selected_item|Must exist as a key in shop_items or be None|"card_counter"|"invalid_item"|Check selected_item in shop_items or selected_item is None|Prevents invalid item selection|
|current_player|Must exist in player/leaderboard data|"P001"|"P999"|Dictionary lookup current_player in players|Ensures valid player context for purchases|
|points|Must be a non-negative integer|1000|-200; "abc"|Type check (is an int) and range check >= 0|Prevents logical errors and invalid calculations|
|points vs price|Must be >= selected item price when purchasing|1000 >= 500|200 < 500|Conditional comparison player_points >= item_price|Prevents purchases without sufficient points|
|player_inventory|Must be a list of valid item IDs|["card_counter"]|"card_counter"(string)|Type check  and membership check for each item|Ensures correct storage of purchased items|
|Duplicate items (privileges)|Unique privilege items cannot be purchased twice|Item not in inventory|Already owned item|Check item not in inventory before purchase|Prevents unfair gameplay advantages|
|Duplicate items (aesthetic)|Optional: allow or restrict duplicates based on design|Multiple themes allowed|Duplicate restricted item|Conditional rule based on item type|Maintains design consistency|
|message|Must be a string and reflect valid system feedback|"Purchase successful"|None; 123|Type check (is a str)|Ensures clear communication to user|
|active_screen|Must be a valid screen value from allowed list|"shop"|"unknown_screen"|Check against allowed list {"menu","shop","game","leaderboard"}|Prevents invalid navigation states|
|Purchase action|Must only occur if all validation checks pass|Valid transaction|Invalid transaction|Combined validation pipeline before commit|Ensures system integrity|
|Item price|Must be a positive integer (> 0)|500|0; -100|Type (is an int) and range check and > 0|Prevents invalid or unintended free items|
|Item type|Must be "aesthetic" or "privilege"|"privilege"|"powerup"(undefined)|Value check against allowed types|Ensures correct in-game behaviour|
|Inventory update|Item must be added after successful purchase|Added to list|Not added|Post-condition check after transaction|Ensures transaction completes correctly|
|Points update|Points must decrease correctly after purchase|1000 → 500|1000 → 1200|Arithmetic check and persistence verification|Prevents incorrect calculations|
|GUI selection|Must not allow purchase if no item selected|Item selected|None selected|Null check selected_item is not None|Prevents unintended actions|
|Data persistence|Updated points and inventory must be saved to storage|Saved to JSON/database|Data lost after restart|File write verification and read-back|Ensures long-term progress retention|
---
The validation system for the shop ensures that all interactions between the user, GUI, and underlying data structures are accurate, secure, and logically consistent. Each variable plays a specific role within the system, and validation ensures that these roles are not violated.

* Dictionaries such as `shop_items` are validated to ensure structural integrity, as missing fields could cause runtime errors when accessing item attributes.

* Similarly, validating `selected_item` ensures that only legitimate items can be processed, preventing invalid lookups.

* Numerical validation, particularly for `points` and item prices, ensures that all calculations remain valid and prevents issues such as negative balances.

* Logical validation (e.g. checking affordability and preventing duplicate purchases) ensures fairness within the game and maintains consistent gameplay mechanics.

* Validating GUI-related variables such as `active_screen` and message ensures that the user interface remains stable and provides meaningful feedback.

* Important in an event-driven system using Tkinter, where invalid states could lead to broken navigation or unclear user experience.

Overall, this validation framework ensures that the shop system is robust, user-friendly, and resistant to errors, supporting both correct functionality and maintainability within the wider Ippan application

### Catalogue Schema Matrix
| Item ID | Display Name | Cost | Category | Structural Utility |
| :--- | :--- | :--- | :--- | :--- |
| `card_counter` | Card Counter | 500 pts | Privilege | Tracks played cards during active matches |
| `gold_theme` | Gold Theme | 300 pts | Aesthetic | Alters UI colour elements to a custom gold hex palette |


## Leaderboard
The leaderboard tracks system configurations and active performance scaling across local JSON records.

### Features
* *Dynamic Sorting:* Utilises Python's sorting algorithms with optimised `lambda` extraction keys to sort player arrays in descending order based on score metrics.
* *Rank Shifting:* Automatically calculates adjustments across rank indexes whenever new point adjustments are written to disc storage.
* *Automated Reward Allocation:* Hooks into a milestone mapping dictionary (`{1: "card_counter", 2: "theme_gold"}`) to automatically inject inventory unlocks into player profiles when climbing ranks.

### Validation Table
|Field / Variable|Validation Rule|Example Valid Input|Example Invalid Input|Validation Method|Justification|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Player ID|Must be unique and exist in system|P001|Duplicate P001; P999 (non-existent)|Check key in dictionary / set|Prevents duplicate or invalid player records|
|Points|Must be a non-negative integer|1200|-50; "abc"|Type and range check (>= 0)|Ensures valid scoring and prevents logical errors|
|Wins|Must be a non-negative integer|15|-1; "ten"|Type and range check|Maintains consistency of statistics|
|Games Played|Must be >= Wins and non-negative|20 (with wins=15)|10 (if wins=15); -5|Logical validation|Prevents impossible game data|
|Leaderboard Sorting|Must be sorted by points (descending)|[1200, 950, 800]|[800, 1200, 950]|Apply sorting algorithm before display|Ensures correct ranking order|
|Player Data Structure|Must contain all required fields (points, wins, games_played)|`{"points":1200,"wins":10,"games_played":15}`|Missing fields|Key existence check|Prevents runtime errors when accessing data|
|Data Type (Player Stats)|Must match expected types (int)|1200|"1200"|Type checking|Prevents calculation and sorting errors|
|Leaderboard Size|Must handle multiple players without overflow|=< system limit|Extremely large dataset causing lag|Limit check / pagination|Ensures GUI remains responsive|
|Current Player Highlight|Player must exist in leaderboard|P001|P999|Lookup in dictionary|Prevents GUI errors when highlighting|
|Data Persistence|Data must save correctly after update|Updated JSON/database|Data not saved|File write verification|Ensures progress is not lost|
|Duplicate Entries|No duplicate player records allowed|Unique IDs|Same ID repeated|Use set/dictionary keys|Maintains data integrity|
|Null / Empty Data|No empty player records|Valid dictionary entry|{} or None|Null check|Prevents crashes during display|

