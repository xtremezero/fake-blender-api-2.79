import typing
import collections.abc
import typing_extensions
import bge.types.KX_GameObject
import bge.types.SCA_MouseSensor

class KX_MouseFocusSensor(bge.types.SCA_MouseSensor.SCA_MouseSensor):
    """The mouse focus sensor detects when the mouse is over the current game object.The mouse focus sensor works by transforming the mouse coordinates from 2d device
    space to 3d space then raycasting away from the camera.
    """

    raySource: typing.Any
    """ The worldspace source of the ray (the view position)."""

    rayTarget: typing.Any
    """ The worldspace target of the ray."""

    rayDirection: typing.Any
    """ The `rayTarget` - `raySource` normalized."""

    hitObject: bge.types.KX_GameObject.KX_GameObject | None
    """ the last object the mouse was over.

    :type: bge.types.KX_GameObject.KX_GameObject | None
    """

    hitPosition: typing.Any
    """ The worldspace position of the ray intersecton."""

    hitNormal: typing.Any
    """ the worldspace normal from the face at point of intersection."""

    hitUV: typing.Any
    """ the UV coordinates at the point of intersection.If the object has no UV mapping, it returns [0, 0].The UV coordinates are not normalized, they can be < 0 or > 1 depending on the UV mapping."""

    usePulseFocus: bool
    """ When enabled, moving the mouse over a different object generates a pulse. (only used when the 'Mouse Over Any' sensor option is set).

    :type: bool
    """

    useXRay: bool
    """ 

    :type: bool
    """

    mask: typing.Any
    """ The collision mask (16 layers mapped to a 16-bit integer) combined with each object's collision group, to hit only a subset of the
objects in the scene. Only those objects for which collisionGroup & mask is true can be hit."""

    propName: str
    """ 

    :type: str
    """

    useMaterial: bool
    """ 

    :type: bool
    """
