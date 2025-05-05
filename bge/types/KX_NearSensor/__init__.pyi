import typing
import collections.abc
import typing_extensions
import bge.types.KX_CollisionSensor

class KX_NearSensor(bge.types.KX_CollisionSensor.KX_CollisionSensor):
    """A near sensor is a specialised form of touch sensor."""

    distance: float
    """ The near sensor activates when an object is within this distance.

    :type: float
    """

    resetDistance: float
    """ The near sensor deactivates when the object exceeds this distance.

    :type: float
    """
