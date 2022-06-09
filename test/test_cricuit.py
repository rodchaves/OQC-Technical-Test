from source.circuit import Circuit
from source.gates import Gate

class TestCircuit:
    def test_can_read_circuit_from_string(self):
        circuit = Circuit.from_string("X(90),Y(180)")

        assert circuit.gates == [
            Gate(axis = 'X', angle = 90),
            Gate(axis = 'Y', angle = 180)
        ]