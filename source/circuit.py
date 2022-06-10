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
    
    def _send_reflection_to_left(self, reflection_position):
        """
        Private method to exchange position of a gate with the reflection gate and
        set the angle of the gate to minus its angle.

        Parameters
        ----------
        self: Circuit
        reflection_position: int

        Returns
        -------
        circuit: Circuit
        
        """
        temporary_gate = self.gates[reflection_position]
        self.gates[reflection_position] = self.gates[reflection_position-1].reflect()
        self.gates[reflection_position-1] = temporary_gate

        return self

    def _perform_reflection(self):
        """
        Private method to perform a reflection using '_send_reflection_to_left' and return a bool
        if the reflection was perfomed.

        Parameters
        ----------
        self: Circuit

        Returns
        -------
        performed_reflection: bool
        
        """
        if len(self.gates) < 3:
            return False

        performed_reflection, i = False, 1

        while i < len(self.gates):
            if self.gates[i-1].axis != self.gates[i].axis and self.gates[i].angle%360 == 180:
                self = self._send_reflection_to_left(i)
                performed_reflection = True
            i += 1

        return performed_reflection

    def _sum_to_previous(self, sum_position):
        """
        Private method to add to gates and remove one of them from the circuit.

        Parameters
        ----------
        self: Circuit
        sum_position: int

        Returns
        -------
        circuit: Circuit
        
        """
        self.gates[sum_position-1] = self.gates[sum_position] + self.gates[sum_position - 1]
        self.gates.pop(sum_position)

        return self




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
        self = self._sum_rotations_same_axis()
        list_of_gates = self.gates
        final_circuit = []

        for gate in list_of_gates:
            if gate.axis == 'Y':
                final_circuit.append(Gate(axis = 'Z', angle = 90))
                final_circuit.append(Gate(axis = 'X', angle = gate.angle))
                final_circuit.append(Gate(axis = 'Z', angle = -90))
            else:
                final_circuit.append(gate)
        
        return Circuit(gates = final_circuit)._sum_rotations_same_axis()

    def optimizationXZ(self):
        """
        Method responsible for replacing all Y rotations for ZX rotations and applying all the necessary
        optimizations like reflections and sum of gates.

        Parameters
        ----------
        self: Circuit

        Returns
        -------
        circuit: Circuit

        """

        self = self._swap_Y_for_Z()
        self = self._check_reflections()
        self = self._sum_rotations_same_axis()

        return self

    def hardware_running_time(self, lengthZ, lengthX):
        """
        Method to check the expected running time of a circuit in the harware.
        The method loops through all gates and add the expected time of each one
        of them.

        Parameters
        ----------
        self: Circuit
        lengthZ: int
        lengthX: int

        Returns
        --------
        time_taken: int
        
        """

        self = self.optimizationXZ()
        list_of_gates = self.gates
        time_taken = 0

        for gate in list_of_gates:
            if gate.axis == 'Z':
                time_taken += lengthZ
            else:
                time_taken += lengthX
        
        return time_taken