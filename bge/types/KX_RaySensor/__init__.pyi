import typing
import collections.abc
import typing_extensions
import bge.types.KX_GameObject
import bge.types.SCA_ISensor
import mathutils

class KX_RaySensor(bge.types.SCA_ISensor.SCA_ISensor):
    """A ray sensor detects the first object in a given direction."""

    propName: str
    """ The property the ray is looking for.

    :type: str
    """

    range: float
    """ The distance of the ray.

    :type: float
    """

    useMaterial: bool
    """ Whether or not to look for a material (false = property).

    :type: bool
    """

    useXRay: bool
    """ Whether or not to use XRay.

    :type: bool
    """

    mask: typing.Any
    """ The collision mask (16 layers mapped to a 16-bit integer) combined with each object's collision group, to hit only a subset of the
objects in the scene. Only those objects for which collisionGroup & mask is true can be hit."""

    hitObject: bge.types.KX_GameObject.KX_GameObject
    """ The game object that was hit by the ray. (read-only).

    :type: bge.types.KX_GameObject.KX_GameObject
    """

    hitPosition: mathutils.Vector
    """ The position (in worldcoordinates) where the object was hit by the ray. (read-only).

    :type: mathutils.Vector
    """

    hitNormal: mathutils.Vector
    """ The normal (in worldcoordinates) of the object at the location where the object was hit by the ray. (read-only).

    :type: mathutils.Vector
    """

    hitMaterial: str
    """ The material of the object in the face hit by the ray. (read-only).

    :type: str
    """

    rayDirection: mathutils.Vector
    """ The direction from the ray (in worldcoordinates). (read-only).

    :type: mathutils.Vector
    """

    axis: typing.Any
    """ The axis the ray is pointing on."""
