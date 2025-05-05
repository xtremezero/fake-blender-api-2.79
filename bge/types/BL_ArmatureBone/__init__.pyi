import typing
import collections.abc
import typing_extensions
import bge.types.EXP_PyObjectPlus

class BL_ArmatureBone(bge.types.EXP_PyObjectPlus.EXP_PyObjectPlus):
    """Proxy to Blender bone structure. All fields are read-only and comply to RNA names.
    All space attribute correspond to the rest pose.
    """

    name: str
    """ bone name.

    :type: str
    """

    connected: bool
    """ true when the bone head is struck to the parent's tail.

    :type: bool
    """

    hinge: bool
    """ true when bone doesn't inherit rotation or scale from parent bone.

    :type: bool
    """

    inherit_scale: bool
    """ true when bone inherits scaling from parent bone.

    :type: bool
    """

    bbone_segments: int
    """ number of B-bone segments.

    :type: int
    """

    roll: float
    """ bone rotation around head-tail axis.

    :type: float
    """

    head: typing.Any
    """ location of head end of the bone in parent bone space."""

    tail: typing.Any
    """ location of head end of the bone in parent bone space."""

    length: float
    """ bone length.

    :type: float
    """

    arm_head: typing.Any
    """ location of head end of the bone in armature space."""

    arm_tail: typing.Any
    """ location of tail end of the bone in armature space."""

    arm_mat: typing.Any
    """ matrix of the bone head in armature space."""

    bone_mat: typing.Any
    """ rotation matrix of the bone in parent bone space."""

    parent: typing_extensions.Self
    """ parent bone, or None for root bone.

    :type: typing_extensions.Self
    """

    children: list[BL_ArmatureBone]
    """ list of bone's children.

    :type: list[BL_ArmatureBone]
    """
