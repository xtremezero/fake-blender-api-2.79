import typing
import collections.abc
import typing_extensions
import bge.types.EXP_PyObjectPlus

class KX_LodLevel(bge.types.EXP_PyObjectPlus.EXP_PyObjectPlus):
    """A single lod level for a game object lod manager."""

    mesh: typing.Any
    """ The mesh used for this lod level. (read only)"""

    level: int
    """ The number of the lod level. (read only)

    :type: int
    """

    distance: typing.Any
    """ Distance to begin using this level of detail. (read only)"""

    hysteresis: typing.Any
    """ Minimum distance factor change required to transition to the previous level of detail in percent. (read only)"""

    useMesh: bool
    """ Return True if the lod level uses a different mesh than the original object mesh. (read only)

    :type: bool
    """

    useMaterial: bool
    """ Return True if the lod level uses a different material than the original object mesh material. (read only)

    :type: bool
    """

    useHysteresis: bool
    """ Return true if the lod level uses hysteresis override. (read only)

    :type: bool
    """
