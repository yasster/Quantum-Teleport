import sys
if sys.version_info < (3,5):
	raise Exception('Please Use Python Version 3.5 or greater.')

import numpy as np

#Imporing QISKit
from qiskit import QuantumCircuit, QuantumProgram
import Qconfig

#Import basic plotting tools 

from qiskit.tools.visualization import plot_histogram

#Quantum program setup
Q_program = QuantumProgram()
Q_program.set_api(Qconfig.APItoken, Qconfig.config['url']) #set APIToken and API Url


#Creating Quantum Registers
q  = Q_program.create_quantum_register('q',3)
c0 = Q_program.create_classical_register('c0',1)
c1 = Q_program.create_classical_register('c1',1)
c2 = Q_program.create_classical_register('c2',1)


#Quantum circuit to make the shared entangled state
teleport = Q_program.create_circuit('teleport',[q],[c0,c1,c2])
teleport.h(q[1])
teleport.cx(q[1],q[2])

#Applying a rotation around the Y axis to prepare quantum state to be teleported
teleport.ry(np.pi/4,q[0])

#Applying CNOT gate and Hadmard Gate
teleport.cx(q[0], q[1])
teleport.h(q[0])
teleport.barrier()

#Measuring Quantum States
teleport.measure(q[0], c0[0])
teleport.measure(q[1], c1[0])

circuits = ['teleport']
print(Q_program.get_qasms(circuits)[0])

#Applying X or Z or both, to the Quantum State
teleport.z(q[2]).c_if(c0,1)
teleport.x(q[2]).c_if(c1,1)

#State should be the same, Now checking through measurment
teleport.measure(q[2],c2[0])

#Excuting the changes on the Simulator
circuits = ['teleport']
print(Q_program.get_qasms(circuits)[0])

#Back-end on IBM Quantum Computer
#backend = 'ibmqx4'
backend = 'local_qasm_simulator'


#The Number of shots in the experiment
shots = 1024


result = Q_program.execute(circuits, backend=backend, shots=shots, max_credits=3, wait=10, timeout=240)



