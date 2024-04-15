import cirq


def build_oracle(qubits, target_index):
    """
    Constructs the oracle for Grover's algorithm.

    The oracle function in Grover's algorithm marks the target state by applying a phase
    shift. This specific implementation uses a phase kick-back mechanism where the phase
    shift is applied using a multi-controlled Z gate.

    Args:
        qubits (List[cirq.Qubit]): The list of qubits that the oracle operates on.
        target_index (int): The index of the target element, represented in binary. The index
            should correspond to the bit representation that the qubits will recognize as the
            target state.

    Returns:
        cirq.Circuit: A circuit representing the oracle for Grover's algorithm.

    Example:
        If the target index is 3, and we have 3 qubits, this corresponds to the binary
        representation '011'. The oracle will apply an X gate to the qubits not involved in
        the '011' state (to flip them to match the '1's in the binary representation), then
        apply a multi-controlled Z gate, and finally uncompute the X gates.
    """
    oracle_circuit = cirq.Circuit()
    for i, qubit in enumerate(qubits):
        if not (target_index >> i) & 1:
            oracle_circuit.append(cirq.X(qubit))
    oracle_circuit.append(cirq.Z(qubits[0]).controlled_by(*qubits[1:]))
    for i, qubit in enumerate(qubits):
        if not (target_index >> i) & 1:
            oracle_circuit.append(cirq.X(qubit))
    return oracle_circuit


def grover_iteration(circuit, qubits, oracle):
    """
    Performs one iteration of Grover's algorithm, appending it to the provided circuit.

    A Grover iteration consists of several steps designed to amplify the probability amplitude
    of the target state. The steps include a series of Hadamard gates to all qubits, application
    of the oracle, another series of Hadamard gates, application of the diffusion operator
    (composed of Pauli-X and multi-controlled-Z gates), and a final set of Hadamard gates.

    Args:
        circuit (cirq.Circuit): The quantum circuit to which the Grover iteration will be appended.
        qubits (List[cirq.Qubit]): The qubits that the Grover iteration operates on.
        oracle (cirq.Circuit): The oracle circuit as defined by `build_oracle`.

    Returns:
        None: The function modifies the circuit in-place by adding Grover iteration steps.

    Notes:
        - The Grover iteration is critical in increasing the likelihood of measuring the
          target state by selectively inverting the phases of the target state and then
          amplifying it relative to other states.
    """
    # Apply Hadamard gates to all qubits to bring them into superposition
    circuit.append(cirq.H.on_each(qubits))
    # Apply the oracle circuit
    circuit.append(oracle)
    # Apply Hadamard gates again to all qubits
    circuit.append(cirq.H.on_each(qubits))
    # Apply Pauli-X gates to prepare for the diffusion operation
    circuit.append(cirq.X.on_each(qubits))
    # Apply a multi-controlled Z gate to implement the diffusion operator
    circuit.append(cirq.Z(qubits[0]).controlled_by(*qubits[1:]))
    # Apply Pauli-X gates to reverse the previous X gate application
    circuit.append(cirq.X.on_each(qubits))
    # Final Hadamard gates to complete the iteration
    circuit.append(cirq.H.on_each(qubits))
