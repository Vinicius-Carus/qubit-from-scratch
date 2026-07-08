import math
import pytest

from functions.quantum import tensor_product_matrix


SQRT_HALF = 1 / math.sqrt(2)

I_GATE = [
    [1, 0],
    [0, 1],
]

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


def assert_matrix_close(result, expected):
    assert len(result) == len(expected)

    for result_row, expected_row in zip(result, expected):
        assert len(result_row) == len(expected_row)

        for result_value, expected_value in zip(result_row, expected_row):
            assert result_value == pytest.approx(expected_value)


def test_tensor_product_matrix_with_generic_matrices():
    matrix_a = [
        [2, 0],
        [0, 3],
    ]

    matrix_b = [
        [1, 4],
        [5, 2],
    ]

    result = tensor_product_matrix(matrix_a, matrix_b)

    expected = [
        [2, 8, 0, 0],
        [10, 4, 0, 0],
        [0, 0, 3, 12],
        [0, 0, 15, 6],
    ]

    assert result == expected


def test_x_tensor_i():
    result = tensor_product_matrix(X_GATE, I_GATE)

    expected = [
        [0, 0, 1, 0],
        [0, 0, 0, 1],
        [1, 0, 0, 0],
        [0, 1, 0, 0],
    ]

    assert result == expected


def test_i_tensor_x():
    result = tensor_product_matrix(I_GATE, X_GATE)

    expected = [
        [0, 1, 0, 0],
        [1, 0, 0, 0],
        [0, 0, 0, 1],
        [0, 0, 1, 0],
    ]

    assert result == expected


def test_z_tensor_i():
    result = tensor_product_matrix(Z_GATE, I_GATE)

    expected = [
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, -1, 0],
        [0, 0, 0, -1],
    ]

    assert result == expected


def test_i_tensor_z():
    result = tensor_product_matrix(I_GATE, Z_GATE)

    expected = [
        [1, 0, 0, 0],
        [0, -1, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, -1],
    ]

    assert result == expected


def test_h_tensor_i():
    result = tensor_product_matrix(H_GATE, I_GATE)

    expected = [
        [SQRT_HALF, 0, SQRT_HALF, 0],
        [0, SQRT_HALF, 0, SQRT_HALF],
        [SQRT_HALF, 0, -SQRT_HALF, 0],
        [0, SQRT_HALF, 0, -SQRT_HALF],
    ]

    assert_matrix_close(result, expected)


def test_i_tensor_h():
    result = tensor_product_matrix(I_GATE, H_GATE)

    expected = [
        [SQRT_HALF, SQRT_HALF, 0, 0],
        [SQRT_HALF, -SQRT_HALF, 0, 0],
        [0, 0, SQRT_HALF, SQRT_HALF],
        [0, 0, SQRT_HALF, -SQRT_HALF],
    ]

    assert_matrix_close(result, expected)


def test_tensor_product_matrix_result_size():
    result = tensor_product_matrix(X_GATE, H_GATE)

    assert len(result) == 4

    for row in result:
        assert len(row) == 4


def test_three_gate_tensor_product_size():
    x_tensor_x = tensor_product_matrix(X_GATE, X_GATE)
    x_tensor_x_tensor_h = tensor_product_matrix(x_tensor_x, H_GATE)

    assert len(x_tensor_x_tensor_h) == 8

    for row in x_tensor_x_tensor_h:
        assert len(row) == 8