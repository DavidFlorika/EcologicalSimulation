# EcologicalSimulation
EcologicalSimulation is a visual ecosystem simulation built with Python and Pygame. It models a simple food chain consisting of three main entities: Food, Consumer, and Predator.

## Program Structure

The simulation runs through a main game loop that continually updates the state of all entities. In each frame:
1. **Interaction & State Updates**: Consumers seek out and eat Food. Predators hunt Consumers. Entities reproduce if they have eaten enough, or die if their hunger reaches zero. Food passively reproduces over time.
2. **Rendering**: The Pygame screen is cleared and all living entities are redrawn at their updated positions.
3. **Statistics**: Real-time counts of the remaining Food, Consumers, and Predators are displayed in the bottom left corner.

## Class Structure

* **`Food` (`Food.py`)**: Represents the base of the food chain. Displayed as a green circle. It does not prey on anything and passively duplicates after a set amount of time.
* **`Consumer` (`Consumer.py`)**: Represents herbivores. Displayed as a red circle. Consumers actively seek and prey on Food. They duplicate after satisfying an inner hunger counter, and die if this counter drops to zero.
* **`Predator` (`Predator.py`)**: Represents carnivores. Displayed as a purple circle. Predators hunt and prey on Consumers. Their life cycle and reproduction mechanics are similar to Consumers, but they move faster.
* **`main` (`main.py`)**: The core engine of the simulation. It prompts the user for initial population parameters, initializes the Pygame window, and contains the main while-loop that governs the passage of time, entity interactions, and screen rendering.

## Contributors

* David
* Lifan

## Requirements

* pygame

### Installation

Install the required dependencies by running:
```bash
pip install -r requirements.txt
```
