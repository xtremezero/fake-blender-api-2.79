import typing
import collections.abc
import typing_extensions
import bge.types.BL_ArmatureConstraint
import bge.types.KX_GameObject
import bge.types.SCA_IActuator

class BL_ArmatureActuator(bge.types.SCA_IActuator.SCA_IActuator):
    """Armature Actuators change constraint condition on armatures."""

    type: int
    """ The type of action that the actuator executes when it is active.Can be one of `these constants <armatureactuator-constants-type>`

    :type: int
    """

    constraint: bge.types.BL_ArmatureConstraint.BL_ArmatureConstraint
    """ The constraint object this actuator is controlling.

    :type: bge.types.BL_ArmatureConstraint.BL_ArmatureConstraint
    """

    target: bge.types.KX_GameObject.KX_GameObject
    """ The object that this actuator will set as primary target to the constraint it controls.

    :type: bge.types.KX_GameObject.KX_GameObject
    """

    subtarget: typing.Any
    """ The object that this actuator will set as secondary target to the constraint it controls."""

    weight: typing.Any
    """ The weight this actuator will set on the constraint it controls."""

    influence: typing.Any
    """ The influence this actuator will set on the constraint it controls."""
