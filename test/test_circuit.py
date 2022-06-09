from source.circuit import Circuit
from source.gates import Gate
import pytest

class TestCircuit:
    def test_can_read_circuit_from_string(self):

        circuit = Circuit.from_string("X(90),Y(180)")

        assert circuit.gates == [
            Gate(axis = 'X', angle = 90),
            Gate(axis = 'Y', angle = 180)
        ]
    
    @pytest.mark.parametrize(
        "gate_string, final_circuit",
        [
            (
                "X(90),X(90),X(90)", 
                [Gate(axis = 'X', angle = 270)]
            ),
            (
                "X(90),Y(90),X(90)", 
                [Gate(axis = 'X', angle = 90), Gate(axis = 'Y', angle = 90), Gate(axis = 'X', angle = 90)]
            ),
            (
                "X(90),X(-90),X(90)", 
                [Gate(axis = 'X', angle = 90)]
            ),
            (
                "X(90),X(90),Y(90)", 
                [Gate(axis = 'X', angle = 180), Gate(axis = 'Y', angle = 90)]
            ),
            (
                "X(30),X(90)", 
                [Gate(axis = 'X', angle = 120)]
            ),
            (
                "X(90)", 
                [Gate(axis = 'X', angle = 90)]
            ),
            (
                "X(0)", 
                [None]
            ),
        ],
    )

    def test_sum_of_gates(self, gate_string, final_circuit):
        
        if gate_string == "X(0)":
            with pytest.raises(UnboundLocalError):
                circuit = Circuit.from_string(gate_string).optimizationXY()
        else:
            circuit = Circuit.from_string(gate_string).optimizationXY()
            assert circuit.gates == final_circuit

    @pytest.mark.parametrize(
        "gate_string, final_circuit",
        [
            (
                "X(90),Y(180),X(90)", 
                [Gate(axis = 'Y', angle = 180)]
            ),
            (
                "Y(90),X(180),Y(90)", 
                [Gate(axis = 'X', angle = 180)]
            ),
            (
                "Y(90),Y(90),X(180),Y(90),Y(90)", 
                [Gate(axis = 'X', angle = 180)]
            ),
            (
                "X(90),Y(180),X(90),X(90),Y(180),X(90),Y(20)", 
                [ Gate(axis = 'Y', angle = 20)]
            ),
            (
                "Y(90),X(180)", 
                [Gate(axis = 'Y', angle = 90), Gate(axis = 'X', angle = 180)]
            ),
            (
                "X(90),X(180)", 
                [Gate(axis = 'X', angle = 270)]
            ),
            (
                "X(90),Y(90),X(90),Y(180),X(90),Y(90),X(90)", 
                [Gate(axis = 'X', angle = 180)]
            ),
            (
                "X(90),Y(90),X(90),X(90),X(90),Y(180),X(90)", 
                [Gate(axis = 'X', angle = 90), Gate(axis = 'Y', angle = 270), Gate(axis = 'X', angle = 180)]
            ),
        ],
    )


    def test_reflections_and_sum_of_gates(self, gate_string, final_circuit):

        circuit = Circuit.from_string(gate_string).optimizationXY()

        assert circuit.gates == final_circuit

    @pytest.mark.parametrize(
        "gate_string, final_circuit",
        [
            (
                "Y(90)", 
                [Gate(axis = 'Z', angle = 90), Gate(axis = 'X', angle = 90), Gate(axis = 'Z', angle = -90)]
            ),
            (
                "X(90),Y(90)", 
                [Gate(axis = 'X', angle = 90), Gate(axis = 'Z', angle = 90), Gate(axis = 'X', angle = 90), Gate(axis = 'Z', angle = -90)]
            ),
        ],
    )
    def test_swap_between_Y_and_Z(self, gate_string, final_circuit):

        circuit = Circuit.from_string(gate_string).optimizationXZ()

        assert circuit.gates == final_circuit

    @pytest.mark.parametrize(
        "gate_string, final_circuit",
        [
            (
                "X(90),Y(180)", 
                [Gate(axis = 'X', angle = 270), Gate(axis = 'Z', angle = 180)]
            ),
            (
                "X(-180),Y(180)", 
                [Gate(axis = 'Z', angle = 180)]
            ),
            (
                "X(90),Y(180),X(90),X(90),Y(180),X(90),Y(20)", 
                [Gate(axis = 'Z', angle = 90), Gate(axis = 'X', angle = 20), Gate(axis = 'Z', angle = -90)]
            ),
            (
                "Y(90),Y(90),X(180),Y(90),Y(90)", 
                [Gate(axis = 'X', angle = 180)]
            ),
        ],
    )
    def test_optimization_of_circuit_with_X_and_Z(self, gate_string, final_circuit):

        circuit = Circuit.from_string(gate_string).optimizationXZ()

        assert circuit.gates == final_circuit
