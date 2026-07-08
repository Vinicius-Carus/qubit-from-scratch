import pytest

from functions.quantum import validate_dimensions
from functions.constants import X_GATE


IDENTITY_4X4 = [
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 1],
]

INVALID_3X3_GATE = [
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1],
]

INVALID_NOT_SQUARE_GATE = [
    [1, 0],
    [0, 1],
    [0, 0],
]


def test_accepts_one_qubit_state():
    state = [1, 0]

    validate_dimensions(state)


def test_accepts_two_qubit_state():
    state = [1, 0, 0, 0]

    validate_dimensions(state)


def test_accepts_complex_amplitudes():
    state = [0j, 1j]

    validate_dimensions(state)


def test_rejects_empty_state():
    state = []

    with pytest.raises(ValueError):
        validate_dimensions(state)


def test_rejects_state_with_non_power_of_two_length():
    state = [1, 0, 0]

    with pytest.raises(ValueError):
        validate_dimensions(state)


def test_rejects_state_with_length_five():
    state = [1, 0, 0, 0, 0]

    with pytest.raises(ValueError):
        validate_dimensions(state)


def test_accepts_2x2_gate_for_one_qubit_state():
    state = [1, 0]

    validate_dimensions(state, X_GATE)


def test_rejects_2x2_gate_for_two_qubit_state():
    state = [1, 0, 0, 0]

    with pytest.raises(ValueError):
        validate_dimensions(state, X_GATE)


def test_accepts_4x4_gate_for_two_qubit_state():
    state = [1, 0, 0, 0]

    validate_dimensions(state, IDENTITY_4X4)


def test_rejects_3x3_gate_for_two_qubit_state():
    state = [1, 0, 0, 0]

    with pytest.raises(ValueError):
        validate_dimensions(state, INVALID_3X3_GATE)


def test_rejects_non_square_gate():
    state = [1, 0]

    with pytest.raises(ValueError):
        validate_dimensions(state, INVALID_NOT_SQUARE_GATE)


def test_rejects_gate_with_wrong_row_size():
    state = [1, 0, 0, 0]

    invalid_gate = [
        [1, 0, 0, 0],
        [0, 1],
        [0, 0, 1, 0],
        [0, 0, 0, 1],
    ]

    with pytest.raises(ValueError):
        validate_dimensions(state, invalid_gate)