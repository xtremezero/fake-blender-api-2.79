import typing
import collections.abc
import typing_extensions
import bge.types.EXP_PyObjectPlus
import mathutils

class KX_BoundingBox(bge.types.EXP_PyObjectPlus.EXP_PyObjectPlus):
    """A bounding volume box of a game object. Used to get and alterate the volume box or AABB."""

    min: mathutils.Vector
    """ The minimal point in x, y and z axis of the bounding box.

    :type: mathutils.Vector
    """

    max: mathutils.Vector
    """ The maximal point in x, y and z axis of the bounding box.

    :type: mathutils.Vector
    """

    center: mathutils.Vector
    """ The center of the bounding box. (read only)

    :type: mathutils.Vector
    """

    radius: float
    """ The radius of the bounding box. (read only)

    :type: float
    """

    autoUpdate: bool
    """ Allow to update the bounding box if the mesh is modified.

    :type: bool
    """
