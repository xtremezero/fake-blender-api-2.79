import typing
import collections.abc
import typing_extensions
import bge.types.SCA_IActuator

class SCA_PropertyActuator(bge.types.SCA_IActuator.SCA_IActuator):
    """Property Actuator"""

    propName: str
    """ the property on which to operate.

    :type: str
    """

    value: str
    """ the value with which the actuator operates.

    :type: str
    """

    mode: int
    """ TODO - add constants to game logic dict!.

    :type: int
    """
