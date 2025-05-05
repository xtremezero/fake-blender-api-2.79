import typing
import collections.abc
import typing_extensions
import bge.types.BL_ArmatureChannel
import bge.types.BL_ArmatureConstraint
import bge.types.KX_GameObject

class BL_ArmatureObject(bge.types.KX_GameObject.KX_GameObject):
    """An armature object."""

    constraints: list[bge.types.BL_ArmatureConstraint.BL_ArmatureConstraint]
    """ The list of armature constraint defined on this armature.
Elements of the list can be accessed by index or string.
The key format for string access is '<bone_name>:<constraint_name>'.

    :type: list[bge.types.BL_ArmatureConstraint.BL_ArmatureConstraint]
    """

    channels: list[bge.types.BL_ArmatureChannel.BL_ArmatureChannel]
    """ The list of armature channels.
Elements of the list can be accessed by index or name the bone.

    :type: list[bge.types.BL_ArmatureChannel.BL_ArmatureChannel]
    """

    def update(self):
        """Ensures that the armature will be updated on next graphic frame.This action is unecessary if a KX_ArmatureActuator with mode run is active
        or if an action is playing. Use this function in other cases. It must be called
        on each frame to ensure that the armature is updated continously.

        """

    def draw(self):
        """Draw lines that represent armature to view it in real time."""
