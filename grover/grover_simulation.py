import matplotlib.pyplot as plt
import numpy as np
from grover_search import grover_search


def run_simulations():
    """
    Runs multiple simulations of Grover's Algorithm across different search space sizes.

    This function systematically increases the size of the search space, executes Grover's Algorithm
    for each size, and records the success rate and the number of iterations used. The purpose is to
    empirically demonstrate Grover's quadratic speedup and efficiency in a quantum search context.

    Returns:
        results (list of tuples): Each tuple contains the search space size, target index used,
                                  success rate, and number of iterations. This data is used for
                                  further analysis and visualization.
    """
    # Define a range of search space sizes to test
    sizes = [4, 8, 16, 32, 64]  # Example sizes for demonstration
    results = []

    # Perform Grover's search for each size
    for size in sizes:
        target = np.random.randint(size)  # Randomly select a target index for the search
        success, iterations_used = grover_search(size, target)
        results.append((size, target, success, iterations_used))

    return results


def plot_results(results):
    """
    Plots the results of multiple Grover's Algorithm simulations.

    This function takes the results of the simulations and plots them to show how the success rate
    and the number of iterations vary with the size of the search space. The visualization helps
    in understanding the scaling and efficiency of Grover's Algorithm.

    Args:
        results (list of tuples): Data from the simulations which includes sizes, targets,
                                  success rates, and iterations.

    Returns:
        None: This function only generates plots and does not return any value.
    """
    # Unpack the results into separate lists for plotting
    sizes, targets, successes, iterations_used = zip(*results)

    # Plotting the success rate across search space sizes
    plt.figure(figsize=(10, 5))
    plt.plot(sizes, successes, 'o-', label='Success Count')
    plt.xticks(sizes)
    plt.xlabel('Search Space Size')
    plt.ylabel('Success Count')
    plt.title('Grover Algorithm Success Rate')
    plt.legend()
    plt.grid(True)
    plt.show()

    # Plotting the number of iterations used for each search space size
    plt.figure(figsize=(10, 5))
    plt.plot(sizes, iterations_used, 's-', label='Iterations Used')
    plt.xticks(sizes)
    plt.xlabel('Search Space Size')
    plt.ylabel('Iterations Used')
    plt.title('Number of Iterations by Search Space Size')
    plt.legend()
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    # Run the simulations and plot the results
    results = run_simulations()
    plot_results(results)
