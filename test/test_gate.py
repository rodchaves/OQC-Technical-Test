import pytest
from source.gates import Gate

class TestGate:
    def test_gate_from_str(self):
        
        gate = Gate.from_string("X(90)")

        assert gate.axis == "X"
        assert gate.angle == 90