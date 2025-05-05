import typing
import collections.abc
import typing_extensions
import bge.types.KX_GameObject
import bge.types.SCA_IActuator

class KX_ParentActuator(bge.types.SCA_IActuator.SCA_IActuator):
    """The parent actuator can set or remove an objects parent object."""

    object: bge.types.KX_GameObject.KX_GameObject | None
    """ the object this actuator sets the parent too.

    :type: bge.types.KX_GameObject.KX_GameObject | None
    """

    mode: typing.Any
    """ The mode of this actuator."""

    compound: bool
    """ Whether the object shape should be added to the parent compound shape when parenting.Effective only if the parent is already a compound shape.

    :type: bool
    """

    ghost: bool
    """ Whether the object should be made ghost when parenting
Effective only if the shape is not added to the parent compound shape.

    :type: bool
    """
