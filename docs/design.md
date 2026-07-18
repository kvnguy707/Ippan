# GUI Design and 
## U-Choose Shop Design
The shop interface utilises a centralised `ctk.CTkFrame` structure. At the top, a prominent balance banner displays the active player's profile ID and their live wallet balance. Individual inventory items are rendered dynamically inside separate horizontal row frames (`fill="x"`). Each row showcases the item title, a categorised utility badge, a brief descriptive text string, and an aligned checkout button. Below is a flowchart of the shop's navigation.
```mermaid
graph TD
A[Main Menu] --> |Click 'U-Choose Shop'| B(Open Shop Window)
B --> C{Check Balance}
C --> |Points >= Cost| D[Process Purchase]
C --> |Points < Cost| E[Insufficient Uju Points]
```

### U-Choose Shop GUI Design
The interface is structured in a panel-based layout, consisting of three main sections:
* Player Information Panel: Displays the current player's ID and available points. 
* This is dynamically updated whenever a purchase is made, ensuring real-time feedback.
* Item Display Panel: Presents a list or grid of purchasable items. Each item includes:
  * name
  * cost
  * description (e.g. "Card Counter: tracks played cards in Daifugo")
  * Interaction Controls
* Includes buttons such as "Buy" and "Back", allowing the user to purchase items or return to the main menu.
---
* Tkinter will be used as the core GUI framework, responsible for creating the main application window, handling user input events, and managing widgets such as labels, buttons, and frames. 
  * For example, the shop screen will be constructed using Tkinter frames to separate different sections of the interface, including the player information panel, item display area, and navigation controls. 
  * Labels will display dynamic data such as the player's current points, while buttons will allow the user to purchase items or return to the main menu.

* CustomTkinter extends Tkinter by providing modern styling and enhanced widgets, allowing the shop interface to be more visually appealing and user-friendly. 
  * This is particularly useful for implementing features such as themed buttons, rounded panels, and colour schemes that can reflect purchased aesthetic items (e.g. a gold theme).
  * As a result, CustomTkinter improves the overall user experience without requiring complex graphical programming.
---
The shop GUI is directly controlled by the MainWindow class, which manages navigation through the current_screen variable. When the user selects the shop option from the main menu, the main window updates this variable to "shop" and renders the corresponding GUI components.

Tkinter event handling is used to connect user actions to program logic. For example:
* Clicking a "Buy" button triggers a function
* This function calls methods from the Player class
* The result (success or failure) is then reflected in the GUI

This demonstrates how Tkinter acts as the interface layer, while the MainWindow acts as the control layer, coordinating interactions between the GUI and underlying data structures.

When the shop GUI is displayed:
* The player's points are retrieved using player_id
* Displayed using a Tkinter label
* Updated dynamically after purchases
---
The reason I used of Tkinter and CustomTkinter is because:
* Separation of concerns
* GUI handles display
* Classes handle logic
* ERD defines structure
* Event-driven programming
* Efficient handling of user interactions
* Scalability
* New shop items or features can be added easily
* Consistency with OOP design
* GUI interacts with objects rather than raw data

Compared to alternatives such as Pygame, Tkinter is more suitable for this component because it provides built-in GUI elements like buttons and labels, which are essential for menu-based systems like the shop.

---
Overall, Tkinter and CustomTkinter provide the necessary tools to implement a responsive and visually appealing shop GUI. Their integration with the MainWindow class ensures smooth navigation, while their interaction with the Player entity and shop data structures demonstrates a clear link to the ERD. This layered approach (GUI → control → data) results in a well-structured, maintainable, and scalable system.
The GUI retrieves player data from the leaderboard structure and item data from a predefined dictionary. When a purchase is attempted, the system validates whether the player has sufficient points. If valid, the transaction is processed, updating both the player’s points and their owned items



## Leaderboard Design
The leaderboard UI presents an arcade-style standings dashboard. The interface reads local JSON entry collections and populates a vertical stack of rank labels. The Top 3 ranking podium rows feature bold typography treatments and custom hex colour codes (#FFD700, #C0C0C0, #CD7F32) to establish a clear visual hierarchy.
