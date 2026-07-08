import math

import pytest

from functions.constants import H, I, ONE_STATE, X, ZERO_STATE
from functions.quantum import format_circuit, format_qubits_label


def test_format_qubits_label_with_computational_basis_states():
    qubits = [ZERO_STATE, ONE_STATE, ZERO_STATE]

    result = format_qubits_label(qubits)

    assert result == "|010⟩"


def test_format_qubits_label_uses_q_for_superposition_state():
    plus_state = [1 / math.sqrt(2), 1 / math.sqrt(2)]
    qubits = [ZERO_STATE, plus_state, ONE_STATE]

    result = format_qubits_label(qubits)

    assert result == "|0Q1⟩"


def test_format_qubits_label_rejects_empty_qubit_list():
    with pytest.raises(ValueError, match="Must have at least one qubit."):
        format_qubits_label([])


def test_format_qubits_label_rejects_invalid_qubit_dimension():
    invalid_qubit = [1, 0, 0]

    with pytest.raises(ValueError, match="State length must be a power of 2."):
        format_qubits_label([invalid_qubit])


def test_format_circuit_with_single_step():
    circuit = [[I, X, I]]

    result = format_circuit("|010⟩", circuit)

    assert result == "|010⟩ -> I ⊗ X ⊗ I"


def test_format_circuit_with_multiple_steps():
    circuit = [[I, X, I], [X, H, X]]

    result = format_circuit("|010⟩", circuit)

    assert result == "|010⟩ -> I ⊗ X ⊗ I -> X ⊗ H ⊗ X"
