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
    from_string(string_of_gates = str):
        Input a string with sequential rotations with axis and angles, then
        transforms them in a circuit which is a list of gates.

    optimizationXY(self = Circuit):
        Input a Circuit that will be optimized by summing rotations with the same
        axis and applying reflections when applicable.

    """
    def __init__(self, gates: list):
            self.gates = gates

    @classmethod
    def from_string(cls, string_of_gates: str):
        """
        Method that transforms a list of gates into a Circuit.

        Parameters
        ----------
        string_of_gates: str

        Returns
        -------
        Circuit: Circuit

        """
        splitted_gates = re.split(',', string_of_gates)

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
        self: Circuit

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
        
        if temp_gate.angle != 0:
            final_circuit.append(temp_gate)
        
        if final_circuit == []:
            raise UnboundLocalError

        return Circuit(gates = final_circuit)

    def _check_reflections(self):
        """
        Private function to reflect gates when a gate is followed by a reflection
        (either X(theta) followed by Y(180) or Y(theta) followed by X(180)). This
        is a required step for the optimization method.

        Parameters
        ----------
        self: Circuit

        Returns
        --------
        circuit: Circuit


        """
        list_of_gates = self.gates

        if len(list_of_gates) < 3:
            return self

        final_circuit = []
        temp_gate = list_of_gates[0]
        list_of_gates.pop(0)       

        for gate in list_of_gates:
            if temp_gate.axis != gate.axis and gate.angle == 180:
                final_circuit.append(gate)
                temp_gate = Gate(axis = temp_gate.axis, angle = -temp_gate.angle)
            elif temp_gate.axis == gate.axis:
                temp_gate = temp_gate + gate            
            else:
                final_circuit.append(temp_gate)
                temp_gate = gate
        
        if temp_gate.angle != 0:
            final_circuit.append(temp_gate)
        
        if final_circuit == []:
            raise UnboundLocalError

        return Circuit(gates = final_circuit)

    def optimizationXY(self):
        """
        Method to optimize the circuit that will add sequential gates with
        the same axis of rotation and do reflections when Y(180) or X(180)
        are present.

        Parameters
        ----------
        self: Circuit

        Returns
        -------
        circuit: Circuit

        """
        self = self._check_reflections()
        self = self._sum_rotations_same_axis()
        
        return self

    def _swap_Y_for_Z(self):
        """
        Private function to replace all Y(theta) rotation gates for Z(90)X(theta)Z(-90) with the intention of
        simulating a circuit in a quantum computer that does not have Y gates.

        Parameters
        ----------
        self: Circuit

        Returns
        -------
        circuit: Circuit

        """
        list_of_gates = self.gates
        final_circuit = []

        for gate in list_of_gates:
            if gate.axis == 'Y':
                final_circuit.append(Gate(axis = 'Z', angle = 90))
                final_circuit.append(Gate(axis = 'X', angle = gate.angle))
                final_circuit.append(Gate(axis = 'Z', angle = -90))
            else:
                final_circuit.append(gate)
        
        return Circuit(gates = final_circuit)

    def optimizationXZ(self):
        
        self = self._swap_Y_for_Z()