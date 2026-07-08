import pytest

from functions.constants import I_GATE, ONE_STATE, X_GATE, ZERO_STATE
from functions.quantum import use_tensor_in_gates, use_tensor_in_qubits


def test_use_tensor_in_qubits_returns_single_qubit():
    result = use_tensor_in_qubits([ZERO_STATE])

    assert result == ZERO_STATE


def test_use_tensor_in_qubits_rejects_empty_list():
    with pytest.raises(ValueError, match="Must have at least one qubit."):
        use_tensor_in_qubits([])


def test_use_tensor_in_qubits_with_two_qubits():
    result = use_tensor_in_qubits([ZERO_STATE, ONE_STATE])

    assert result == [0, 1, 0, 0]


def test_use_tensor_in_qubits_with_three_qubits():
    result = use_tensor_in_qubits([ZERO_STATE, ONE_STATE, ZERO_STATE])

    assert result == [0, 0, 1, 0, 0, 0, 0, 0]


def test_use_tensor_in_qubits_rejects_invalid_qubit_dimension():
    with pytest.raises(ValueError):
        use_tensor_in_qubits([ZERO_STATE, [1, 0, 0]])


def test_use_tensor_in_gates_returns_single_gate():
    result = use_tensor_in_gates([X_GATE])

    assert result == X_GATE


def test_use_tensor_in_gates_rejects_empty_list():
    with pytest.raises(ValueError, match="Must have at least one gate."):
        use_tensor_in_gates([])


def test_use_tensor_in_gates_with_two_gates():
    result = use_tensor_in_gates([I_GATE, X_GATE])

    expected = [
        [0, 1, 0, 0],
        [1, 0, 0, 0],
        [0, 0, 0, 1],
        [0, 0, 1, 0],
    ]

    assert result == expected


def test_use_tensor_in_gates_with_three_gates_has_expected_size():
    result = use_tensor_in_gates([I_GATE, X_GATE, I_GATE])

    assert len(result) == 8

    for row in result:
        assert len(row) == 8
