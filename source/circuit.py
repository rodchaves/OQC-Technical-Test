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
    def from_string(self, list_of_gates: list):
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

        return Circuit(gates = gates)

    