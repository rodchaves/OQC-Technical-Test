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

        return cls(axis=axis,angle=angle)
    


