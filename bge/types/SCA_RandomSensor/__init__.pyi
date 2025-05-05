import typing
import collections.abc
import typing_extensions
import bge.types.SCA_ISensor

class SCA_RandomSensor(bge.types.SCA_ISensor.SCA_ISensor):
    """This sensor activates randomly."""

    lastDraw: int
    """ The seed of the random number generator.

    :type: int
    """

    seed: int
    """ The seed of the random number generator.

    :type: int
    """
