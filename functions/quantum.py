import math
import random

def validate_dimensions(state, gate=None):
    state_len = len(state)

    if state_len <= 1:
        raise ValueError("State must have at least 2 amplitudes.")

    num_qubits  = math.log2(state_len)

    if isinstance(num_qubits , float) and (not num_qubits .is_integer()):
        raise ValueError("State length must be a power of 2.")

    if gate is not None:
        if len(gate) != state_len:
            raise ValueError(f"Gate must be a {state_len}x{state_len} matrix.")

        for gate_line in gate:
            if len(gate_line) != state_len:
                raise ValueError(f"Gate must be a {state_len}x{state_len} matrix.")


def apply_gate(gate, state):
    validate_dimensions(state=state, gate=gate)
    result = []

    for gate_line in gate:
        amplitude = 0
        for index in range(len(gate_line)):
            amplitude += gate_line[index] * state[index]

        result.append(amplitude)
    
    return result


def calculate_probabilities(state):
    validate_dimensions(state=state)

    probabilities = []

    for value in state:
        probabilities.append(round((abs(value) ** 2) * 100))

    return probabilities


def is_normalized(state):
    validate_dimensions(state=state)
    probability_sum = 0

    for value in state:
        probability_sum += abs(value) ** 2

    return math.isclose(probability_sum, 1.0, abs_tol=1e-9)


def print_state(label, state):
    validate_dimensions(state)
    probabilities = calculate_probabilities(state)
    num_qubits = int(math.log2(len(state)))

    print(label)
    print("State:", state)
    print("Probabilities:")

    for state_index in range(len(state)):
        basis_state = format(state_index, f"0{num_qubits}b")
        print(f"|{basis_state}⟩ = {probabilities[state_index]}%")

    if is_normalized(state):
        print("State is normalized.")
    else:
        print("State is not normalized.")

    print()


def format_qubits_label(qubits):
    if len(qubits) < 1:
        raise ValueError("Must have at least one qubit.")

    labels = []

    for qubit in qubits:
        validate_dimensions(qubit)

        if qubit == [1, 0]:
            labels.append("0")
        elif qubit == [0, 1]:
            labels.append("1")
        else:
            labels.append("Q")

    return f"|{''.join(labels)}⟩"


def format_circuit(initial_state_label, circuit):
    steps = []

    for step in circuit:
        gate_names = []

        for gate in step:
            gate_names.append(gate[0])

        steps.append(" ⊗ ".join(gate_names))

    return f"{initial_state_label} -> " + " -> ".join(steps)

def tensor_product_matrix(matrix_a, matrix_b):
    result = []

    for row_a in matrix_a:
        for row_b in matrix_b:
            new_row = []
            for value_a in row_a:
                for value_b in row_b:
                    new_row.append(value_a * value_b)
            result.append(new_row)

    return result

def tensor_product_vector(vector_a, vector_b):
    result = []
    for value_a in vector_a:
        for value_b in vector_b:
            new_value = value_a * value_b
            result.append(new_value)

    return result

def use_tensor_in_qubits(qubits):
    if len(qubits) == 1:
        return qubits[0]

    if len(qubits) < 1:
        raise ValueError("Must have at least one qubit.")

    validate_dimensions(qubits[0])
    actual_qubits = qubits[0]

    for qubit_index in range(len(qubits)):
        if qubit_index == 0:
            continue

        validate_dimensions(qubits[qubit_index])
        validate_dimensions(actual_qubits)

        actual_qubits = tensor_product_vector(actual_qubits, qubits[qubit_index])

    return actual_qubits

def use_tensor_in_gates(gates):
    if len(gates) == 1:
        return gates[0]

    if len(gates) < 1:
        raise ValueError("Must have at least one gate.")

    actual_gates = gates[0]

    for gate_index in range(len(gates)):
        if gate_index == 0:
            continue

        actual_gates = tensor_product_matrix(actual_gates, gates[gate_index])

    return actual_gates

def generate_state_labels(state_len):
    if state_len <= 1:
        raise ValueError("State must have at least 2 amplitudes.")

    num_qubits = math.log2(state_len)

    if isinstance(num_qubits, float) and (not num_qubits.is_integer()):
        raise ValueError("State length must be a power of 2.")

    labels = []
    label_size = int(num_qubits)

    for state_index in range(state_len):
        basis_state = format(state_index, f"0{label_size}b")
        labels.append(f"|{basis_state}⟩")

    return labels

def measure_state(state):
    validate_dimensions(state)

    probabilities = calculate_probabilities(state)
    labels = generate_state_labels(len(state))

    random_value = random.random() * 100

    cumulative_probability = 0
    
    for label, probability in zip(labels, probabilities):
        cumulative_probability += probability

        if random_value < cumulative_probability:
            return label
   
    return labels[-1]


def run_measurements(state, shots):
    validate_dimensions(state)

    if shots <= 0:
        raise ValueError("Shots must be greater than 0.")

    labels = generate_state_labels(len(state))

    counts = {}

    for label in labels:
        counts[label] = 0

    for _ in range(shots):
        measured_label = measure_state(state)
        counts[measured_label] += 1

    return counts

if __name__ == '__main__':
    result = run_measurements([0.5, 0.5, 0.5, 0.5], 100)
    print(result)