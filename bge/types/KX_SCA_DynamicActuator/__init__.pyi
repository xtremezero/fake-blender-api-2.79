import typing
import collections.abc
import typing_extensions
import bge.types.SCA_IActuator

class KX_SCA_DynamicActuator(bge.types.SCA_IActuator.SCA_IActuator):
    """Dynamic Actuator."""

    mode: int
    """ the type of operation of the actuator, 0-4

    :type: int
    """

    mass: float
    """ the mass value for the KX_DYN_SET_MASS operation.

    :type: float
    """
