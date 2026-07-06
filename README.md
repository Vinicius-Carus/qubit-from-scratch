# Qubit From Scratch

A small educational project to understand the basics of quantum computing using plain Python.

This project represents a single qubit as a vector and applies basic quantum gates as matrices.

## What it does

* Represents qubit states like `[1, 0]`, `[0, 1]` and complex amplitudes like `[0j, 1j]`
* Applies basic gates: X, Y, Z and H
* Calculates measurement probabilities using squared magnitudes
* Checks if a state is normalized
* Runs a simple sequence of gates as a circuit

## Gates implemented

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

## Example

Circuit:

```text
|0⟩ -> H -> Z -> H
```

Result:

```text
|0⟩ = 0%
|1⟩ = 100%
```

## How to run

```bash
python main.py
```

## Purpose

I built this project to learn the basics of linear algebra and quantum computing from scratch, without using a quantum framework.

The goal is to understand the core idea:

```text
qubit = vector
gate = matrix
applying a gate = matrix-vector multiplication
probability = squared magnitude of the amplitude
```

## Limitations

This is not a full quantum simulator. It only supports one-qubit circuits and the basic X, Y, Z and H gates.

It does not support multiple qubits, tensor products, entanglement, CNOT gates or real quantum hardware.
