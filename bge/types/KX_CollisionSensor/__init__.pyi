import typing
import collections.abc
import typing_extensions
import bge.types.KX_GameObject
import bge.types.SCA_ISensor

class KX_CollisionSensor(bge.types.SCA_ISensor.SCA_ISensor):
    """Collision sensor detects collisions between objects."""

    propName: str
    """ The property or material to collide with.

    :type: str
    """

    useMaterial: bool
    """ Determines if the sensor is looking for a property or material. KX_True = Find material; KX_False = Find property.

    :type: bool
    """

    usePulseCollision: bool
    """ When enabled, changes to the set of colliding objects generate a pulse.

    :type: bool
    """

    hitObject: bge.types.KX_GameObject.KX_GameObject | None
    """ The last collided object. (read-only).

    :type: bge.types.KX_GameObject.KX_GameObject | None
    """

    hitObjectList: typing.Any
    """ A list of colliding objects. (read-only)."""

    hitMaterial: str
    """ The material of the object in the face hit by the ray. (read-only).

    :type: str
    """
