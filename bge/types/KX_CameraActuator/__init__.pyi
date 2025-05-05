import typing
import collections.abc
import typing_extensions
import bge.types.KX_GameObject
import bge.types.SCA_IActuator

class KX_CameraActuator(bge.types.SCA_IActuator.SCA_IActuator):
    """Applies changes to a camera."""

    damping: float
    """ strength of of the camera following movement.

    :type: float
    """

    axis: int
    """ The camera axis (0, 1, 2) for positive XYZ, (3, 4, 5) for negative XYZ.

    :type: int
    """

    min: float
    """ minimum distance to the target object maintained by the actuator.

    :type: float
    """

    max: float
    """ maximum distance to stay from the target object.

    :type: float
    """

    height: float
    """ height to stay above the target object.

    :type: float
    """

    object: bge.types.KX_GameObject.KX_GameObject | None
    """ the object this actuator tracks.

    :type: bge.types.KX_GameObject.KX_GameObject | None
    """
