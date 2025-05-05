import typing
import collections.abc
import typing_extensions
import bge.types.SCA_IActuator

class KX_VisibilityActuator(bge.types.SCA_IActuator.SCA_IActuator):
    """Visibility Actuator."""

    visibility: bool
    """ whether the actuator makes its parent object visible or invisible.

    :type: bool
    """

    useOcclusion: bool
    """ whether the actuator makes its parent object an occluder or not.

    :type: bool
    """

    useRecursion: bool
    """ whether the visibility/occlusion should be propagated to all children of the object.

    :type: bool
    """
