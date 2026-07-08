# Qubit From Scratch

Educational quantum computing project built with plain Python.

The goal is to understand the fundamentals without using a quantum framework:

```text
qubit = vector
gate = matrix
multi-qubit state = tensor product of vectors
multi-qubit gate = tensor product of matrices
applying a gate = matrix-vector multiplication
probability = squared magnitude of the amplitude
```

## What It Does

* Represents qubits as vectors, like `[1, 0]` for `|0⟩` and `[0, 1]` for `|1⟩`.
* Supports real and complex amplitudes, including states like `[0, 1j]`.
* Applies quantum gates through matrix-vector multiplication.
* Builds multi-qubit states with tensor products.
* Builds multi-qubit gates with tensor products.
* Calculates measurement probabilities for every computational basis state.
* Checks if a state is normalized.
* Formats and prints circuits step by step.

## Project Structure

```text
functions/
  constants.py  # Quantum states and gate constants.
  quantum.py    # Core simulation functions.
test/
  test_apply_gate.py
  test_formatting.py
  test_state_output.py
  test_tensor_helpers.py
  test_tensor_product_matrix.py
  test_tensor_product_vector.py
  test_validate_dimensions.py
main.py         # Example circuit execution.
```

## Gates Implemented

### I Gate

Identity gate. Keeps the qubit unchanged.

```text
I|0⟩ = |0⟩
I|1⟩ = |1⟩
```

### X Gate

Swaps the amplitudes of `|0⟩` and `|1⟩`.

```text
X|0⟩ = |1⟩
X|1⟩ = |0⟩
```

### Y Gate

Swaps the amplitudes of `|0⟩` and `|1⟩`, adding an imaginary phase.

```text
Y|0⟩ = i|1⟩
Y|1⟩ = -i|0⟩
```

### Z Gate

Flips the sign of the `|1⟩` amplitude.

```text
Z(a, b) = (a, -b)
```

### H Gate

Creates or removes superposition.

```text
H|0⟩ = 1/√2 (|0⟩ + |1⟩)
H|1⟩ = 1/√2 (|0⟩ - |1⟩)
```

## Example Circuit

Circuits are represented as a list of steps. Each step contains one gate per qubit:

```python
qubits = [ZERO_STATE, ONE_STATE, ZERO_STATE]

circuit = [
    [I, X, I],
    [X, X, X],
]
```

The circuit formatter displays each step using tensor product notation:

```text
|010⟩ -> I ⊗ X ⊗ I -> X ⊗ X ⊗ X
```

For qubits that are valid but not exactly `|0⟩` or `|1⟩`, the label formatter uses `Q`:

```text
|0Q1⟩
```

## How To Run

Install dependencies:

```bash
poetry install
```

Run the example:

```bash
poetry run python main.py
```

Run tests:

```bash
poetry run pytest
```

## Core Functions

* `validate_dimensions(state, gate=None)` validates state and gate dimensions.
* `apply_gate(gate, state)` applies a gate matrix to a state vector.
* `calculate_probabilities(state)` returns measurement probabilities.
* `is_normalized(state)` checks if probability amplitudes sum to `1`.
* `tensor_product_vector(vector_a, vector_b)` combines state vectors.
* `tensor_product_matrix(matrix_a, matrix_b)` combines gate matrices.
* `use_tensor_in_qubits(qubits)` builds a multi-qubit state.
* `use_tensor_in_gates(gates)` builds a multi-qubit gate.
* `format_qubits_label(qubits)` formats labels like `|010⟩`.
* `format_circuit(initial_state_label, circuit)` formats the circuit flow.

## Tests

The project uses `pytest` and includes unit tests for:

* dimension validation;
* gate application;
* vector tensor products;
* matrix tensor products;
* state probabilities and normalization;
* circuit and qubit label formatting;
* helper functions that build multi-qubit states and gates.

## Limitations

This is still an educational simulator. It does not currently implement measurement collapse, entangling gates like CNOT, controlled gates, circuit optimization, noise models or real quantum hardware integration.
