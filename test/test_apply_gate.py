import math
import pytest

from functions.quantum import apply_gate


SQRT_HALF = 1 / math.sqrt(2)

ZERO_STATE = [1, 0]
ONE_STATE = [0, 1]

X_GATE = [
    [0, 1],
    [1, 0],
]

Z_GATE = [
    [1, 0],
    [0, -1],
]

H_GATE = [
    [SQRT_HALF, SQRT_HALF],
    [SQRT_HALF, -SQRT_HALF],
]

Y_GATE = [
    [0, -1j],
    [1j, 0],
]


def assert_state_close(result, expected):
    assert len(result) == len(expected)

    for result_value, expected_value in zip(result, expected):
        assert result_value == pytest.approx(expected_value)


def test_apply_x_gate_to_zero_state():
    result = apply_gate(X_GATE, ZERO_STATE)

    assert result == [0, 1]


def test_apply_x_gate_to_one_state():
    result = apply_gate(X_GATE, ONE_STATE)

    assert result == [1, 0]


def test_apply_z_gate_to_superposition_changes_phase():
    state = [SQRT_HALF, SQRT_HALF]

    result = apply_gate(Z_GATE, state)

    assert_state_close(result, [SQRT_HALF, -SQRT_HALF])


def test_apply_h_gate_to_zero_state_creates_superposition():
    result = apply_gate(H_GATE, ZERO_STATE)

    assert_state_close(result, [SQRT_HALF, SQRT_HALF])


def test_apply_h_gate_twice_returns_to_zero_state():
    first_result = apply_gate(H_GATE, ZERO_STATE)
    second_result = apply_gate(H_GATE, first_result)

    assert_state_close(second_result, ZERO_STATE)


def test_apply_y_gate_to_zero_state():
    result = apply_gate(Y_GATE, ZERO_STATE)

    assert result == [0, 1j]


def test_apply_y_gate_to_one_state():
    result = apply_gate(Y_GATE, ONE_STATE)

    assert result == [-1j, 0]


def test_apply_y_gate_to_real_amplitudes():
    state = [0.6, 0.8]

    result = apply_gate(Y_GATE, state)

    assert_state_close(result, [-0.8j, 0.6j])


def test_rejects_gate_with_wrong_number_of_rows():
    state = [1, 0]

    invalid_gate = [
        [1, 0],
        [0, 1],
        [0, 0],
    ]

    with pytest.raises(ValueError):
        apply_gate(invalid_gate, state)


def test_rejects_gate_with_wrong_number_of_columns():
    state = [1, 0]

    invalid_gate = [
        [1, 0, 0],
        [0, 1, 0],
    ]

    with pytest.raises(ValueError):
        apply_gate(invalid_gate, state)


def test_rejects_two_by_two_gate_for_two_qubit_state():
    state = [1, 0, 0, 0]

    with pytest.raises(ValueError):
        apply_gate(X_GATE, state)

def test_apply_i_tensor_x_to_zero_zero():
    state = [1, 0, 0, 0]  # |00⟩

    i_tensor_x = [
        [0, 1, 0, 0],
        [1, 0, 0, 0],
        [0, 0, 0, 1],
        [0, 0, 1, 0],
    ]

    result = apply_gate(i_tensor_x, state)

    assert result == [0, 1, 0, 0]  # |01⟩


def test_apply_x_tensor_i_to_zero_zero():
    state = [1, 0, 0, 0]  # |00⟩

    x_tensor_i = [
        [0, 0, 1, 0],
        [0, 0, 0, 1],
        [1, 0, 0, 0],
        [0, 1, 0, 0],
    ]

    result = apply_gate(x_tensor_i, state)

    assert result == [0, 0, 1, 0]  # |10⟩


def test_apply_i_tensor_x_to_one_zero():
    state = [0, 0, 1, 0]  # |10⟩

    i_tensor_x = [
        [0, 1, 0, 0],
        [1, 0, 0, 0],
        [0, 0, 0, 1],
        [0, 0, 1, 0],
    ]

    result = apply_gate(i_tensor_x, state)

    assert result == [0, 0, 0, 1]  # |11⟩