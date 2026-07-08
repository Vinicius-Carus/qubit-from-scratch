from math import sqrt
import pytest

from functions.quantum import tensor_product_vector

ZERO_STATE = [1, 0]
ONE_STATE = [0, 1]


def test_tensor_zero_zero_returns_00():
    result = tensor_product_vector(ZERO_STATE, ZERO_STATE)

    assert result == [1, 0, 0, 0]


def test_tensor_zero_one_returns_01():
    result = tensor_product_vector(ZERO_STATE, ONE_STATE)

    assert result == [0, 1, 0, 0]


def test_tensor_one_zero_returns_10():
    result = tensor_product_vector(ONE_STATE, ZERO_STATE)

    assert result == [0, 0, 1, 0]


def test_tensor_one_one_returns_11():
    result = tensor_product_vector(ONE_STATE, ONE_STATE)

    assert result == [0, 0, 0, 1]


def test_tensor_plus_zero():
    plus_state = [1 / sqrt(2), 1 / sqrt(2)]

    result = tensor_product_vector(plus_state, ZERO_STATE)

    expected = [
        1 / sqrt(2),
        0,
        1 / sqrt(2),
        0,
    ]

    assert result == pytest.approx(expected)


def test_tensor_zero_plus():
    plus_state = [1 / sqrt(2), 1 / sqrt(2)]

    result = tensor_product_vector(ZERO_STATE, plus_state)

    expected = [
        1 / sqrt(2),
        1 / sqrt(2),
        0,
        0,
    ]

    assert result == pytest.approx(expected)


def test_tensor_minus_state_with_one():
    minus_state = [1 / sqrt(2), -1 / sqrt(2)]

    result = tensor_product_vector(minus_state, ONE_STATE)

    expected = [
        0,
        1 / sqrt(2),
        0,
        -1 / sqrt(2),
    ]

    assert result == pytest.approx(expected)


def test_tensor_with_complex_values():
    state_a = [1, 1j]
    state_b = [1, -1j]

    result = tensor_product_vector(state_a, state_b)

    expected = [
        1,
        -1j,
        1j,
        1,
    ]

    assert result == pytest.approx(expected)


def test_tensor_three_qubits_zero_one_zero():
    first_two = tensor_product_vector(ZERO_STATE, ONE_STATE)
    result = tensor_product_vector(first_two, ZERO_STATE)

    expected = [
        0, 0,
        1, 0,
        0, 0,
        0, 0,
    ]

    assert result == expected


def test_tensor_three_qubits_plus_zero_one():
    plus_state = [1 / sqrt(2), 1 / sqrt(2)]

    first_two = tensor_product_vector(plus_state, ZERO_STATE)
    result = tensor_product_vector(first_two, ONE_STATE)

    expected = [
        0,
        1 / sqrt(2),
        0,
        0,
        0,
        1 / sqrt(2),
        0,
        0,
    ]

    assert result == pytest.approx(expected)