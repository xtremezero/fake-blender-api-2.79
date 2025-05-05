import typing
import collections.abc
import typing_extensions
import bge.types.BL_ArmatureBone
import bge.types.EXP_PyObjectPlus

class BL_ArmatureChannel(bge.types.EXP_PyObjectPlus.EXP_PyObjectPlus):
    """Proxy to armature pose channel. Allows to read and set armature pose.
    The attributes are identical to RNA attributes, but mostly in read-only mode.
    """

    name: str
    """ channel name (=bone name), read-only.

    :type: str
    """

    bone: bge.types.BL_ArmatureBone.BL_ArmatureBone
    """ return the bone object corresponding to this pose channel, read-only.

    :type: bge.types.BL_ArmatureBone.BL_ArmatureBone
    """

    parent: typing_extensions.Self
    """ return the parent channel object, None if root channel, read-only.

    :type: typing_extensions.Self
    """

    has_ik: bool
    """ true if the bone is part of an active IK chain, read-only.
This flag is not set when an IK constraint is defined but not enabled (miss target information for example).

    :type: bool
    """

    ik_dof_x: bool
    """ true if the bone is free to rotation in the X axis, read-only.

    :type: bool
    """

    ik_dof_y: bool
    """ true if the bone is free to rotation in the Y axis, read-only.

    :type: bool
    """

    ik_dof_z: bool
    """ true if the bone is free to rotation in the Z axis, read-only.

    :type: bool
    """

    ik_limit_x: bool
    """ true if a limit is imposed on X rotation, read-only.

    :type: bool
    """

    ik_limit_y: bool
    """ true if a limit is imposed on Y rotation, read-only.

    :type: bool
    """

    ik_limit_z: bool
    """ true if a limit is imposed on Z rotation, read-only.

    :type: bool
    """

    ik_rot_control: bool
    """ true if channel rotation should applied as IK constraint, read-only.

    :type: bool
    """

    ik_lin_control: bool
    """ true if channel size should applied as IK constraint, read-only.

    :type: bool
    """

    location: typing.Any
    """ displacement of the bone head in armature local space, read-write."""

    scale: typing.Any
    """ scale of the bone relative to its parent, read-write."""

    rotation_quaternion: typing.Any
    """ rotation of the bone relative to its parent expressed as a quaternion, read-write."""

    rotation_euler: typing.Any
    """ rotation of the bone relative to its parent expressed as a set of euler angles, read-write."""

    rotation_mode: typing.Any
    """ Method of updating the bone rotation, read-write."""

    channel_matrix: typing.Any
    """ pose matrix in bone space (deformation of the bone due to action, constraint, etc), Read-only.
This field is updated after the graphic render, it represents the current pose."""

    pose_matrix: typing.Any
    """ pose matrix in armature space, read-only,
This field is updated after the graphic render, it represents the current pose."""

    pose_head: typing.Any
    """ position of bone head in armature space, read-only."""

    pose_tail: typing.Any
    """ position of bone tail in armature space, read-only."""

    ik_min_x: float
    """ minimum value of X rotation in degree (<= 0) when X rotation is limited (see ik_limit_x), read-only.

    :type: float
    """

    ik_max_x: float
    """ maximum value of X rotation in degree (>= 0) when X rotation is limited (see ik_limit_x), read-only.

    :type: float
    """

    ik_min_y: float
    """ minimum value of Y rotation in degree (<= 0) when Y rotation is limited (see ik_limit_y), read-only.

    :type: float
    """

    ik_max_y: float
    """ maximum value of Y rotation in degree (>= 0) when Y rotation is limited (see ik_limit_y), read-only.

    :type: float
    """

    ik_min_z: float
    """ minimum value of Z rotation in degree (<= 0) when Z rotation is limited (see ik_limit_z), read-only.

    :type: float
    """

    ik_max_z: float
    """ maximum value of Z rotation in degree (>= 0) when Z rotation is limited (see ik_limit_z), read-only.

    :type: float
    """

    ik_stiffness_x: typing.Any
    """ bone rotation stiffness in X axis, read-only."""

    ik_stiffness_y: typing.Any
    """ bone rotation stiffness in Y axis, read-only."""

    ik_stiffness_z: typing.Any
    """ bone rotation stiffness in Z axis, read-only."""

    ik_stretch: float
    """ ratio of scale change that is allowed, 0=bone can't change size, read-only.

    :type: float
    """

    ik_rot_weight: typing.Any
    """ weight of rotation constraint when ik_rot_control is set, read-write."""

    ik_lin_weight: typing.Any
    """ weight of size constraint when ik_lin_control is set, read-write."""

    joint_rotation: typing.Any
    """ Control bone rotation in term of joint angle (for robotic applications), read-write.When writing to this attribute, you pass a [x, y, z] vector and an appropriate set of euler angles or quaternion is calculated according to the rotation_mode.When you read this attribute, the current pose matrix is converted into a [x, y, z] vector representing the joint angles.The value and the meaning of the x, y, z depends on the ik_dof_x/ik_dof_y/ik_dof_z attributes:"""
