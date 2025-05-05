import typing
import collections.abc
import typing_extensions
import bge.types.EXP_Value

class KX_2DFilterOffScreen(bge.types.EXP_Value.EXP_Value):
    """2D filter custom off screen."""

    width: int
    """ The off screen width, -1 if the off screen can be resized dynamically (read-only).

    :type: int
    """

    height: int
    """ The off screen height, -1 if the off screen can be resized dynamically (read-only).

    :type: int
    """

    colorBindCodes: typing.Any
    """ The bind code of the color textures attached to the off screen (read-only)."""

    depthBindCode: int
    """ The bind code of the depth texture attached to the off screen (read-only).

    :type: int
    """
