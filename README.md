# Flappy Bird Automation Using Neuroevolution of Augmented Topologies (NEAT) - AI LAB MINI PROJECT

## Overview
This project showcases an AI system that automates the **Flappy Bird** game using the **NeuroEvolution of Augmented Topologies (NEAT)** algorithm combined with a genetic algorithm. The goal is to evolve a neural network capable of playing the game autonomously, improving its performance over generations.

## Key Concepts
- **NeuroEvolution of Augmented Topologies (NEAT):** NEAT is a method for evolving neural networks using genetic algorithms. It starts with simple networks and gradually evolves them, adding nodes and connections as needed to improve performance. This allows the AI to optimize both the weights and the structure of the neural network.
  
- **Genetic Algorithm:** A genetic algorithm is used to evolve the population of neural networks. The fittest networks (those that perform best in the game) are selected to reproduce, passing on their characteristics to the next generation.

## Project Details
- **Language:** Python
- **Libraries:** 
  - **NEAT-Python:** An implementation of the NEAT algorithm in Python.
  - **Pygame:** Used to simulate the Flappy Bird game environment.
  - **Numpy:** For numerical operations and handling neural network data.
  
- **Functionality:**
  - The neural network starts with a simple topology and evolves as it learns to play Flappy Bird.
  - The fitness function is based on the score (i.e., how far the bird flies without hitting obstacles).
  - Over several generations, the algorithm produces increasingly sophisticated networks capable of better performance in the game.

## Installation
To run the project locally, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/flappy-bird-neat.git
    ```
2. Navigate to the project directory:
    ```bash
    cd flappy-bird-neat
    ```
3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```
4. Start the simulation:
    ```bash
    python flappy_bird_neat.py
    ```

## How It Works
- **Initialization:** The simulation starts with a population of randomly generated neural networks.
- **Evaluation:** Each network controls a bird in the Flappy Bird game. The network's fitness is determined by how far the bird travels without crashing.
- **Selection and Reproduction:** The top-performing networks are selected to create offspring through crossover and mutation, producing the next generation.
- **Evolution:** Over many generations, the neural networks evolve, becoming better at playing the game.

## Results
As the algorithm progresses, you should observe the AI-controlled birds getting better at avoiding obstacles and achieving higher scores. The NEAT algorithm allows for complex strategies to emerge as the networks evolve.

## Contributing
Contributions are welcome! If you have any ideas for improving the AI or extending the project, feel free to submit a pull request.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements
- **NEAT-Python** for the NEAT implementation in Python.
- **Pygame** for providing the game simulation environment.
- The community for their resources and tutorials on AI and game automation.
