import math
import cirq
from grover_utils import build_oracle, grover_iteration

def grover_search(num_elements, target_index):
    """
    Executes Grover's search algorithm to find a specific target index within a given search space.

    This function sets up and runs Grover's Algorithm using a quantum simulator, specifically tailored
    to find a target index in a unstructured search space represented by a binary number. The number of
    iterations performed is approximately the square root of the number of elements, which is optimal
    for Grover's Algorithm.

    Args:
        num_elements (int): The total number of elements in the search space. This determines the size
            of the search space and hence the number of qubits needed.
        target_index (int): The index of the target element within the search space. This index should
            be within the range [0, num_elements - 1].

    Returns:
        int: The number of successful searches out of a predetermined number of repetitions. This
            indicates how many times the target index was correctly found across multiple trials.

    Example:
        If the search space has 8 elements and the target index is 3, this function will setup a quantum
        simulation to find the index '3' using Grover's algorithm.
    """
    # Calculate the number of qubits needed based on the number of elements
    num_qubits = int(math.ceil(math.log2(num_elements)))
    qubits = [cirq.GridQubit(i, 0) for i in range(num_qubits)]
    circuit = cirq.Circuit()

    # Build the oracle using the utility function from grover_utils
    oracle = build_oracle(qubits, target_index)

    # Calculate the optimal number of Grover iterations
    iterations = int(math.pi / 4 * math.sqrt(num_elements))

    # Append Grover iterations to the circuit
    for _ in range(iterations):
        grover_iteration(circuit, qubits, oracle)

    # Append a measurement operation to all qubits at the end of the circuit
    circuit.append(cirq.measure(*qubits, key='result'))

    # Setup the simulator and run the circuit
    simulator = cirq.Simulator()
    result = simulator.run(circuit, repetitions=18)

    # Analyze the results to count how many times the correct target index was found
    success_count = sum(1 for r in result.measurements['result']
                        if all(x == ((target_index >> i) & 1) for i, x in enumerate(r)))
    return success_count, iterations

if __name__ == "__main__":
    # Example usage with a predefined number of elements and a target index
    num_elements = 8  # This should be a power of 2
    target_index = 3  # Index of the target in binary form

    # Run Grover's search and print the results
    success_count = grover_search(num_elements, target_index)
    print(f"Found the target element index '{target_index}' {success_count} times out of 18 simulations.")
