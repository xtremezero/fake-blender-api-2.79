import typing
import collections.abc
import typing_extensions
import bge.types.KX_GameObject
import mathutils

class KX_FontObject(bge.types.KX_GameObject.KX_GameObject):
    """A Font object."""

    text: str
    """ The text displayed by this Font object.

    :type: str
    """

    resolution: typing.Any
    """ The resolution of the font police."""

    size: typing.Any
    """ The size (scale factor) of the font object, scaled from font object origin (affects text resolution)."""

    dimensions: mathutils.Vector
    """ The size (width and height) of the current text in Blender Units.

    :type: mathutils.Vector
    """
