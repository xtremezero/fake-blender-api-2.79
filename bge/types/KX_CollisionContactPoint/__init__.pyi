import typing
import collections.abc
import typing_extensions
import bge.types.EXP_Value
import mathutils

class KX_CollisionContactPoint(bge.types.EXP_Value.EXP_Value):
    """A collision contact point passed to the collision callbacks."""

    localPointA: mathutils.Vector
    """ The contact point in the owner object space.

    :type: mathutils.Vector
    """

    localPointB: mathutils.Vector
    """ The contact point in the collider object space.

    :type: mathutils.Vector
    """

    worldPoint: mathutils.Vector
    """ The contact point in world space.

    :type: mathutils.Vector
    """

    normal: mathutils.Vector
    """ The contact normal in owner object space.

    :type: mathutils.Vector
    """

    combinedFriction: float
    """ The combined friction of the owner and collider object.

    :type: float
    """

    combinedRollingFriction: float
    """ The combined rolling friction of the owner and collider object.

    :type: float
    """

    combinedRestitution: float
    """ The combined restitution of the owner and collider object.

    :type: float
    """

    appliedImpulse: float
    """ The applied impulse to the owner object.

    :type: float
    """
