import pytest
from source.gates import Gate

class TestGate:
    def test_gate_from_str(self):
        
        gate = Gate.from_string("X(90)")

        assert gate.axis == "X"
        assert gate.angle == 90

    def test_can_sum_if_same_axis(self):

        gate1 = Gate(axis = 'X', angle = 20)
        gate2 = Gate(axis= 'X', angle = 30)

        assert gate1 + gate2 == Gate(axis = 'X', angle = 50)

    def test_cannot_sum_if_different_axis(self):

        gate1 = Gate(axis = 'Y', angle = 20)
        gate2 = Gate(axis= 'X', angle = 30)

        with pytest.raises(ValueError):
            gate1 + gate2

    def test_can_sum_if_same_axis_full_rotation(self):

        gate1 = Gate(axis = 'X', angle = 280)
        gate2 = Gate(axis = 'X', angle = 100)

        assert gate1 + gate2 == Gate(axis = 'X', angle = 20)

    def test_sum_if_same_axis_negative_and_positive(self):

        gate1 = Gate(axis = 'X', angle = 280)
        gate2 = Gate(axis = 'X', angle = -100)

        assert gate1 + gate2 == Gate(axis='X', angle = 180)

    def test_sum_if_same_axis_negative_and_negative(self):

        gate1 = Gate(axis = 'X', angle = -80)
        gate2 = Gate(axis = 'X', angle = -100)

        assert gate1 + gate2 == Gate(axis = 'X', angle = 180)

    def test_sum_if_same_axis_negative_and_negative_full_rotation(self):

        gate1 = Gate(axis = 'X', angle = -280)
        gate2 = Gate(axis = 'X', angle = -100)

        assert gate1 + gate2 == Gate(axis = 'X', angle = 340)