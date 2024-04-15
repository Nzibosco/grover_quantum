# Grover's Algorithm Simulation

This project implements Grover's Algorithm using Google's Cirq framework to demonstrate the quantum search algorithm's capability and efficiency compared to classical search algorithms. This README provides instructions on how to set up the environment and run the simulations.

## Project Structure

- `grover_utils.py`: Contains utility functions such as the oracle and Grover iteration which are central to Grover's algorithm.
- `grover_search.py`: Contains the function to run Grover's search for a specified number of elements and a target index.
- `grover_simulation.py`: Runs multiple simulations of Grover's Algorithm across various search space sizes and plots the results.

## Prerequisites

- Python 3.6 or later
- [Cirq](https://quantumai.google/cirq): Google's quantum computing libraries and simulator
- [Matplotlib](https://matplotlib.org/): A plotting library for Python
- [NumPy](https://numpy.org/): A library for large, multi-dimensional arrays and matrices

## Environment Setup

1. **Install Python**: Make sure Python 3.6 or later is installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).

2. **Install Required Libraries**:
   You can install the necessary Python libraries using pip. Run the following command:

   ```bash
   pip install cirq matplotlib numpy

## Running the Code

1. **Unzip the source code**: Download the zip file containing the source code and unzip it in your desired directory, or clone it directly from the repository if available.

2. **Navigate to the Project Directory**: Change directory to the folder containing the project files (folder name is currently named as **grover**).

3. **Run the Simulation**:
   - To run a single instance of Grover's search, execute:
     ```bash
     python grover_search.py
     ```
   - To run the simulation script that includes plotting, execute:
     ```bash
     python grover_simulation.py
     ```
   These scripts will output the results of Grover's Algorithm and generate plots showing the success rate across different search space sizes.

## Troubleshooting

- Ensure all libraries are installed correctly as mentioned in the Environment Setup.
- Check Python's version if you encounter syntax errors.
- If the plots do not display, ensure Matplotlib is installed correctly and your environment supports GUI operations.
- As best practice, you can create a virtual environment for this project to ensure dependencies don't interfere with your local python packages.

## Contact

For any queries or issues, you can contact me at ***jean.bosco.nzeyimana@vanderbilt.edu***.
