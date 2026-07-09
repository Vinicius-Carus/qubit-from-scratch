from functions.constants import H, I, ZERO_STATE, ONE_STATE, CNOT_GATE_2_QUBITS
from functions.quantum import apply_gate, format_circuit, format_qubits_label, print_state, use_tensor_in_gates, use_tensor_in_qubits

def main():

    qubits = [ZERO_STATE, ZERO_STATE] 

    circuit = [[H, I]]
    initial_state_label = format_qubits_label(qubits)

    print(f"Circuit: {format_circuit(initial_state_label, circuit)}")
    print()

    initial_state = use_tensor_in_qubits(qubits)

    previous_state = initial_state

    print_state("Initial state:", initial_state)
    for step in circuit:
        gate_matrixes = [gate[1] for gate in step]
        gate_formated = use_tensor_in_gates(gate_matrixes)
        gate_name = " ⊗ ".join(gate[0] for gate in step)

        previous_state = apply_gate(gate_formated, previous_state)
        print_state(f"After {gate_name} gate:", previous_state)
    
    # if len(qubits) == 2:
    #     apply_cnot = apply_gate(state=previous_state, gate=CNOT_GATE_2_QUBITS)
    #     print_state("After CNOT:", apply_cnot)


main()