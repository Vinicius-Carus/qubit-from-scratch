import math

import pytest

from functions.quantum import calculate_probabilities, is_normalized, print_state


def test_calculate_probabilities_for_zero_state():
    result = calculate_probabilities([1, 0])

    assert result == [100, 0]


def test_calculate_probabilities_for_balanced_superposition():
    state = [1 / math.sqrt(2), 1 / math.sqrt(2)]

    result = calculate_probabilities(state)

    assert result == [50, 50]


def test_calculate_probabilities_for_two_qubit_state():
    state = [0, 0, 1j, 0]

    result = calculate_probabilities(state)

    assert result == [0, 0, 100, 0]


def test_calculate_probabilities_rejects_invalid_state_dimension():
    with pytest.raises(ValueError):
        calculate_probabilities([1, 0, 0])


def test_is_normalized_accepts_normalized_state():
    state = [1 / math.sqrt(2), 1 / math.sqrt(2)]

    result = is_normalized(state)

    assert result is True


def test_is_normalized_rejects_non_normalized_state():
    state = [1, 1]

    result = is_normalized(state)

    assert result is False


def test_is_normalized_accepts_complex_normalized_state():
    state = [0, 1j]

    result = is_normalized(state)

    assert result is True


def test_print_state_outputs_basis_probabilities(capsys):
    print_state("Initial state:", [0, 1, 0, 0])

    output = capsys.readouterr().out

    assert "Initial state:" in output
    assert "State: [0, 1, 0, 0]" in output
    assert "Probabilities:" in output
    assert "|00⟩ = 0%" in output
    assert "|01⟩ = 100%" in output
    assert "|10⟩ = 0%" in output
    assert "|11⟩ = 0%" in output
    assert "State is normalized." in output


def test_print_state_outputs_not_normalized_message(capsys):
    print_state("Invalid state:", [1, 1])

    output = capsys.readouterr().out

    assert "Invalid state:" in output
    assert "State is not normalized." in output
