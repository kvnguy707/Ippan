# System Architecture & Data Design

## Graphical User Interface (GUI) Flows
The interface uses CustomTkinter widgets organised reactively. Below is the layout state transition map for the Shop transaction flow:

### U-Choose Shop

```mermaid
graph TD
A[Main Menu] --> |Click 'U-Choose Shop'| B(Open Shop Window)
B --> C{Check Balance}
C --> |Points >= Cost| D[Process Purchase]
C --> |Points < Cost| E[Insufficient Uju Points]
