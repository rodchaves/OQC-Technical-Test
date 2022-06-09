from source.gates import Gate
import re

class Circuit:
    """
    Class defined to create the circuit associated to a list of with gates. 

    Attributes
    -----------
    gates: Gate

    Methods
    -------


    """
    def __init__(self, gates: list):
            self.gates = gates

    @classmethod
    def from_string(cls, list_of_gates: list):
        """
        Method that transforms a list of gates into a Circuit.

        Parameters
        ----------
        list_of_gates: list

        Returns
        -------
        Circuit: Circuit

        """
        splitted_gates = re.split(',', list_of_gates)

        gates = []

        for gates_string in splitted_gates:
            gates.append(Gate.from_string(gates_string))

        return cls(gates = gates)
    
    def _sum_rotations_same_axis(self):
        """
        Private function to sum gates with the same axis that will be
        used in the optimization of the whole circuit.

        Parameters
        ----------
        circuit: Circuit

        Returns
        --------
        circuit: Circuit

        """
        list_of_gates = self.gates
        final_circuit = []
        temp_gate = list_of_gates[0]
        list_of_gates.pop(0)

        for gate in list_of_gates:
            if temp_gate.axis == gate.axis:
                temp_gate = temp_gate + gate
            else:
                if temp_gate.angle != 0:
                    final_circuit.append(temp_gate)
                temp_gate = gate

        final_circuit.append(temp_gate)
        
        return Circuit(gates = final_circuit)

    def _check_reflections(self):
        list_of_gates = self.gates
        final_circuit = []
        temp_gate = list_of_gates[0]
        list_of_gates = list_of_gates.pop(0)

        for gate in list_of_gates:
            if temp_gate.axis != gate.axis and gate.angle == 180:
                final_circuit.append(gate)
                temp_gate = Gate(axis = gate.axis, angle = -gate.angle)
            else:
                final_circuit.append(temp_gate)
                temp_gate = gate
        
        return Circuit(gates = final_circuit)

    def optimizationXY(self):
        """
        Method to optimize the circuit that will add sequential gates with
        the same axis of rotation and do reflections when Y(180) or X(180)
        are present.

        Parameters
        ----------
        circuit: Circuit

        Returns
        -------
        circuit: Circuit

        """
        #self.gates = _check_reflections(self).gates
        self = self._sum_rotations_same_axis()
        
        return self





    