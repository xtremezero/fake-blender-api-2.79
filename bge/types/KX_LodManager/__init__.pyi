import typing
import collections.abc
import typing_extensions
import bge.types.EXP_PyObjectPlus
import bge.types.KX_LodLevel

class KX_LodManager(bge.types.EXP_PyObjectPlus.EXP_PyObjectPlus):
    """This class contains a list of all levels of detail used by a game object."""

    levels: list[bge.types.KX_LodLevel.KX_LodLevel]
    """ Return the list of all levels of detail of the lod manager.

    :type: list[bge.types.KX_LodLevel.KX_LodLevel]
    """

    distanceFactor: float
    """ Method to multiply the distance to the camera.

    :type: float
    """
