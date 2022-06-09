from dataclasses import dataclass
import re


@dataclass
class Gate:
    """
    A class to represent gates. Dataclass was used so we can compare two entries
    of the class for later usage.

    Attributes
    ----------
    axis: axis of rotation
    angle: angle of rotation in angles

    Methods
    -------

    """
    axis: str
    angle: int

    @classmethod
    def from_string(cls, gate:str):
        """
        Construct the gate from a given string.

        Parameters
        ----------
        gate: str

        Returns
        -------
        gate: Gate

        """
        splitted_string = re.split("\(|\)", gate.strip())
        axis = splitted_string[0]
        angle = int(splitted_string[1])

        return cls(axis=axis, angle=angle)

    def __add__(self, gate):
        """
        Add the angle of two gates that have the same axis of rotation.

        Parameters
        ----------
        gate: Gate
        
        Returns
        -------
        gate: Gate
        
        """
        if self.axis == gate.axis:
            new_angle = (self.angle + gate.angle)%360
            return Gate(axis = self.axis, angle = new_angle)
        raise ValueError
    


