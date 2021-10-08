import numpy as np
from qiskit import *

# Create a Quantum Circuit acting on a quantum register of three qubits
circ = QuantumCircuit(4)

# Add a H gate on qubit 0, putting this qubit in superposition.
circ.h(0)
# Add a CX (CNOT) gate on control qubit 0 and target qubit 1, putting
# the qubits in a Bell state.
circ.cx(0, 1)
# Add a CX (CNOT) gate on control qubit 1 and target qubit 2
circ.cx(1, 2)
# Add a CX (CNOT) gate on control qubit 2 and target qubit 3
circ.cx(2, 3)

# visualize the circuit
circ.draw()
