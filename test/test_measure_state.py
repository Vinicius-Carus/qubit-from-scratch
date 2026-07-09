import pytest

from functions import quantum


def test_generate_state_labels_for_one_qubit():
    result = quantum.generate_state_labels(2)

    assert result == ["|0⟩", "|1⟩"]


def test_generate_state_labels_for_two_qubits():
    result = quantum.generate_state_labels(4)

    assert result == ["|00⟩", "|01⟩", "|10⟩", "|11⟩"]


def test_generate_state_labels_rejects_invalid_state_length():
    with pytest.raises(ValueError, match="State length must be a power of 2."):
        quantum.generate_state_labels(3)


def test_measure_state_returns_only_possible_basis_state(monkeypatch):
    monkeypatch.setattr(quantum.random, "random", lambda: 0)

    result = quantum.measure_state([0, 1])

    assert result == "|1⟩"


def test_measure_state_uses_first_probability_range(monkeypatch):
    monkeypatch.setattr(quantum.random, "random", lambda: 0.24)

    result = quantum.measure_state([0.5, 0.5, 0.5, 0.5])

    assert result == "|00⟩"


def test_measure_state_uses_later_probability_range(monkeypatch):
    monkeypatch.setattr(quantum.random, "random", lambda: 0.76)

    result = quantum.measure_state([0.5, 0.5, 0.5, 0.5])

    assert result == "|11⟩"

def test_measure_state_uses_second_probability_range(monkeypatch):
    monkeypatch.setattr(quantum.random, "random", lambda: 0.30)

    result = quantum.measure_state([0.5, 0.5, 0.5, 0.5])

    assert result == "|01⟩"


def test_measure_state_uses_third_probability_range(monkeypatch):
    monkeypatch.setattr(quantum.random, "random", lambda: 0.60)

    result = quantum.measure_state([0.5, 0.5, 0.5, 0.5])

    assert result == "|10⟩"