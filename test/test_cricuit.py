from source.circuit import Circuit
from source.gates import Gate

class TestCircuit:
    def test_can_read_circuit_from_string(self):
        circuit = Circuit.from_string("X(90),Y(180)")

        assert circuit.gates == [
            Gate(axis = 'X', angle = 90),
            Gate(axis = 'Y', angle = 180)
        ]
    
    def test_sum_of_gates(self):
        circuit1 = Circuit.from_string("X(90),X(90),X(90)")
        circuit2 = Circuit.from_string("X(90),Y(90),X(90)")
        circuit3 = Circuit.from_string("X(90),X(-90),X(90)")
        circuit4 = Circuit.from_string("X(90),X(90),Y(90)")
        circuit5 = Circuit.from_string("X(30),X(90)")
        circuit6 = Circuit.from_string("X(90)")
        
        circuit1 = circuit1.optimizationXY()
        circuit2 = circuit2.optimizationXY()
        circuit3 = circuit3.optimizationXY()
        circuit4 = circuit4.optimizationXY()
        circuit5 = circuit5.optimizationXY()
        circuit6 = circuit6.optimizationXY()

        
        assert circuit1.gates == [
            Gate(axis = 'X', angle = 270)
        ]
        assert circuit2.gates == [
            Gate(axis = 'X', angle = 90),
            Gate(axis = 'Y', angle = 90),
            Gate(axis = 'X', angle = 90)
        ]
        assert circuit3.gates == [
            Gate(axis = 'X', angle = 90)
        ]
        assert circuit4.gates == [
            Gate(axis = 'X', angle = 180),
            Gate(axis = 'Y', angle = 90)
        ]
        assert circuit5.gates == [
            Gate(axis = 'X', angle = 120)
        ]
        assert circuit6.gates == [
            Gate(axis = 'X', angle = 90)
        ]