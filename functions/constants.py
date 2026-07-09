import math

SQRT_HALF = 1 / math.sqrt(2)

ZERO_STATE = [1, 0]
ONE_STATE = [0, 1]

INPUT = []

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
    [1j, 0]
]

I_GATE = [
    [1, 0],
    [0, 1]
]

CNOT_GATE_2_QUBITS = [
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 0, 1],
    [0, 0, 1, 0]
]

H = ("H", H_GATE)
Z = ("Z", Z_GATE)
X = ("X", X_GATE)
Y = ("Y", Y_GATE)
I = ("I", I_GATE)