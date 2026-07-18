# Ippan: Universal Multi-Game Card Engine
An interactive card game platform built with Python and Tkinkter/CustomTkinter featuring an immutable transactional economy, dynamic inventory system, and persistent algorithmic leaderboard. All with the help of architectures and concepts like: OOPs, JSON files, Dictionaries, and many more!

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

