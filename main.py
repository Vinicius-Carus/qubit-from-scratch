import math

ZERO_STATE = [1, 0]
ONE_STATE = [0, 1]

SQRT_HALF = 1 / math.sqrt(2)

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

H = ("H", H_GATE)
Z = ("Z", Z_GATE)
X = ("X", X_GATE)
Y = ("Y", Y_GATE)

def validate_dimensions(state, gate=None):
    if len(state) != 2:
        raise ValueError("State must have exactly 2 amplitudes.")

    if gate is not None:
        if len(gate) != 2 or len(gate[0]) != 2 or len(gate[1]) != 2:
            raise ValueError("Gate must be a 2x2 matrix.")


def apply_gate(gate, state):
    validate_dimensions(state=state, gate=gate)

    return [
        gate[0][0] * state[0] + gate[0][1] * state[1],
        gate[1][0] * state[0] + gate[1][1] * state[1],
    ]

def calculate_probabilities(state):
    validate_dimensions(state=state)

    probability_zero = round((abs(state[0]) ** 2) * 100)
    probability_one = round((abs(state[1]) ** 2) * 100)

    return f"|0⟩ = {probability_zero}%\n|1⟩ = {probability_one}%"


def is_normalized(state):
    validate_dimensions(state=state)

    probability_sum = abs(state[0]) ** 2 + abs(state[1]) ** 2

    return math.isclose(probability_sum, 1.0, abs_tol=1e-9)


def print_state(label, state):
    print(label)
    print("State:", state)
    print("Probabilities:")
    print(calculate_probabilities(state))

    if is_normalized(state):
        print("State is normalized.")
    else:
        print("State is not normalized.")

    print()


def format_circuit(initial_state_label, circuit):
    gate_names = []

    for gate in circuit:
        gate_names.append(gate[0])

    return f"{initial_state_label} -> " + " -> ".join(gate_names)

def main():

    circuit = [Y, Y]

    print(f"Circuit: {format_circuit("|0⟩", circuit)}")
    print()

    initial_state = ZERO_STATE
    previous_state = initial_state

    print_state("Initial state:", initial_state)

    for step in circuit:
        previous_state = apply_gate(step[1], previous_state)
        print_state(f"After {step[0]} gate:", previous_state)


main()