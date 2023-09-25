# INC Machine Learning Project

Welcome to the INC (Impetus and Concepts) Machine Learning Project repository!
In this project, we have implemented the NEAT (NeuroEvolution of Augmenting Topologies)
algorithm from scratch, using the official research paper as our primary guide.
Our goal was to explore and demonstrate the power of NEAT in evolving neural networks for tasks like playing games.

## Project Overview

### NEAT Algorithm

NEAT is a powerful evolutionary algorithm for evolving artificial neural networks.
It is especially well-suited for problems where the network's architecture itself needs to evolve,
making it a valuable tool in reinforcement learning tasks, like game playing.
Our implementation closely follows the principles outlined in the original NEAT paper:

- [Original NEAT Paper](https://nn.cs.utexas.edu/downloads/papers/stanley.ec02.pdf)

### Flappy Bird Clone

To test the capabilities of our NEAT implementation,
we created a Flappy Bird clone using the Pygame library.
Flappy Bird is a simple yet challenging game where a bird must navigate through pipes by jumping.
Our goal was to evolve neural networks capable of playing the game and achieving high scores autonomously.

## Repository Structure

- `neat` folder: Implementation of the NEAT algorithm.
- `Bird.py`: The Flappy Bird class.
- `__main__.py`: The main script to run NEAT on the Flappy Bird game.
- `README.md`: You're reading it right now!

## Getting Started

To get started with this project, follow these steps:

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/kshitijaucharmal/FlappyNEAT.git
   ```

2. Install the necessary dependencies. You can use `pip` to install them:

   ```bash
   pip install pygame
   ```

3. Run the NEAT algorithm on the Flappy Bird game:

   ```bash
   python .
   ```

   This will start the training process and display the progress of the evolving neural networks as they learn to play the game.

## Configuration

> !!! Not implemented yet !!!

You can fine-tune the NEAT algorithm by modifying the parameters in the `config.txt` file.
These parameters include population size, mutation rates, and various other settings that can influence the evolution process.

## Contributors

- [Kshitij Aucharmal](https://github.com/kshitijaucharmal) - Algorithm Implementation
- [Alisha Shaikh](https://github.com/alisha971) - Game Development
- [Tanish Chaudhari](https://github.com/Cratan228) - Project Management

## Contributing

Contributions are always welcome!!

Just fork the repository and create a pull request with your desired changes, we'll be sure to review them as soon as possible!

## Acknowledgments

We would like to express our gratitude to the creators of the NEAT algorithm for their pioneering work in neuroevolution.
This project wouldn't have been possible without their research.

## License

This project is licensed under the GPL 3.0 License - see the [LICENSE](LICENSE) file for details.

---

Feel free to explore the code, experiment with the NEAT parameters,
and enjoy watching neural networks learn to play Flappy Bird!
If you have any questions or suggestions,
please don't hesitate to [open an issue](https://github.com/kshitijaucharmal/FlappyNEAT/issues)
or [reach out to us](mailto:kshitijaucharmal21@gmail.com).
Happy coding!
