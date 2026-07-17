# Ippan: Universal Multi-Game Card Engine
An interactive card game platform built with Python and Tkinkter/CustomTkinter featuring an immutable transactional economy, dynamic inventory system, and persistent algorithmic leaderboard. All with the help of architectures and concepts like: OOPs, JSON files, Dictionaries, and many more!


## U-Choose Shop
The game features a fully persistent transaction layer that allows players to spend points earned in matches on profile enhancements.

### Architecture & Validation Layers
* *Decoupled Architecture:* The backend processing layer (`shop.py`) is completely separated from the rendering interface (`main.py`) to preserve clean state boundaries.
* *Fail-Safe Checks:*  The transaction engine runs three structural validations prior to modifying state records:
  * Catalogue Verification: Validates whether the requested item ID exists.
  * Financial Balance Check: Rejects transactions if player points fall below the item cost.
  * Duplicate Purchase Blocking: References item attributes (`"one_time": True`) to prevent double-spending on owned aesthetics or privileges.

### Catalog Schema Matrix
| Item ID | Display Name | Cost | Category | Structural Utility |
| :--- | :--- | :--- | :--- | :--- |
| `card_counter` | Card Counter | 500 pts | Privilege | Tracks played cards during active matches |
| `gold_theme` | Gold Theme | 300 pts | Aesthetic | Alters UI colour elements to a custom gold hex palette |


## Algorithmic Leaderboard
The Global Leaderboard tracks system configurations and active performance scaling across local JSON records.

### Features
* *Dynamic Sorting:* Utilises Python's sorting algorithms with optimised `lambda` extraction keys to sort player arrays in descending order based on score metrics.
* *Rank Shifting:* Automatically calculates adjustments across rank indexes whenever new point adjustments are written to disc storage.
* *Automated Reward Allocation:* Hooks into a milestone mapping dictionary (`{1: "card_counter", 2: "theme_gold"}`) to automatically inject inventory unlocks into player profiles when climbing ranks.



