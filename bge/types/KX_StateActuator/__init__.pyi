import typing
import collections.abc
import typing_extensions
import bge.types.SCA_IActuator

class KX_StateActuator(bge.types.SCA_IActuator.SCA_IActuator):
    """State actuator changes the state mask of parent object."""

    operation: int
    """ Type of bit operation to be applied on object state mask.You can use one of `these constants <state-actuator-operation>`

    :type: int
    """

    mask: int
    """ Value that defines the bits that will be modified by the operation.The bits that are 1 in the mask will be updated in the object state.The bits that are 0 are will be left unmodified expect for the Copy operation which copies the mask to the object state.

    :type: int
    """
