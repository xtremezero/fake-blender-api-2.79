import typing
import collections.abc
import typing_extensions
import bge.types.EXP_Value
import bge.types.KX_GameObject

class SCA_ILogicBrick(bge.types.EXP_Value.EXP_Value):
    """Base class for all logic bricks."""

    executePriority: typing.Any
    """ This determines the order controllers are evaluated, and actuators are activated (lower priority is executed first)."""

    owner: bge.types.KX_GameObject.KX_GameObject
    """ The game object this logic brick is attached to (read-only).

    :type: bge.types.KX_GameObject.KX_GameObject
    """

    name: str
    """ The name of this logic brick (read-only).

    :type: str
    """
