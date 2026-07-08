# Changelog

All notable changes to this project will be documented in this file.

## [2.0.0] - Current State

### Added

* Multi-qubit support through tensor products between state vectors.
* Multi-qubit gate support through tensor products between matrices.
* `I` gate as the identity gate for composing multi-qubit circuits.
* `tensor_product_vector(vector_a, vector_b)` to combine state vectors.
* `tensor_product_matrix(matrix_a, matrix_b)` to combine gate matrices.
* `use_tensor_in_qubits(qubits)` to build a full multi-qubit state.
* `use_tensor_in_gates(gates)` to build a composed multi-qubit gate.
* `format_qubits_label(qubits)` to generate labels such as `|010⟩`.
* `Q` label support when a qubit is valid but not exactly `|0⟩` or `|1⟩`.
* `format_circuit(initial_state_label, circuit)` to display circuits step by step.
* Probability output for all computational basis states, such as `|00⟩`, `|01⟩`, `|10⟩` and `|11⟩`.
* Unit tests for formatting, probabilities, normalization, tensor products and multi-qubit helpers.
* Updated README with project structure, commands, core functions and current limitations.

### Changed

* `calculate_probabilities(state)` now returns probabilities for all state amplitudes, not only one-qubit states.
* `is_normalized(state)` now validates normalization across all state amplitudes.
* `print_state(label, state)` now prints probabilities per computational basis state.
* `main.py` now runs circuits with multiple qubits and multiple steps.
* Error messages were updated to be clearer and more consistent.

### Fixed

* Fixed gate application in `apply_gate`, avoiding invalid result-list access and shifted indexes.
* Fixed circuit formatting so each step is treated as a list of gates.
* Fixed the `format_circuit` call in `main.py` to avoid a hardcoded initial-state label.
* Fixed printing of the applied circuit step name.

### Tests

* Added tests for `apply_gate`.
* Added tests for `validate_dimensions`.
* Added tests for `tensor_product_vector`.
* Added tests for `tensor_product_matrix`.
* Added tests for `calculate_probabilities`, `is_normalized` and `print_state`.
* Added tests for `format_qubits_label` and `format_circuit`.
* Added tests for `use_tensor_in_qubits` and `use_tensor_in_gates`.

## [1.0.0] - Initial Base

### Added

* Basic qubit representation as vectors.
* Gate representation as matrices.
* Basic `X`, `Y`, `Z` and `H` gates.
* Gate application through matrix-vector multiplication.
* Initial probability calculation.
* Initial normalization check.
* Simple execution example in `main.py`.
