import typing
import collections.abc
import typing_extensions
import bge.types.EXP_PyObjectPlus

class BL_ArmatureConstraint(bge.types.EXP_PyObjectPlus.EXP_PyObjectPlus):
    """Proxy to Armature Constraint. Allows to change constraint on the fly.
    Obtained through `BL_ArmatureObject`.constraints.
    """

    type: int
    """ Type of constraint, (read-only).Use one of `these constants<armatureconstraint-constants-type>`.

    :type: int
    """

    name: str
    """ Name of constraint constructed as <bone_name>:<constraint_name>. constraints list.This name is also the key subscript on `BL_ArmatureObject`.

    :type: str
    """

    enforce: float
    """ fraction of constraint effect that is enforced. Between 0 and 1.

    :type: float
    """

    headtail: typing.Any
    """ Position of target between head and tail of the target bone: 0=head, 1=tail."""

    lin_error: float
    """ runtime linear error (in Blender units) on constraint at the current frame.This is a runtime value updated on each frame by the IK solver. Only available on IK constraint and iTaSC solver.

    :type: float
    """

    rot_error: typing.Any
    """ Runtime rotation error (in radiant) on constraint at the current frame.This is a runtime value updated on each frame by the IK solver. Only available on IK constraint and iTaSC solver.It is only set if the constraint has a rotation part, for example, a CopyPose+Rotation IK constraint."""

    target: typing.Any
    """ Primary target object for the constraint. The position of this object in the GE will be used as target for the constraint."""

    subtarget: typing.Any
    """ Secondary target object for the constraint. The position of this object in the GE will be used as secondary target for the constraint.Currently this is only used for pole target on IK constraint."""

    active: bool
    """ True if the constraint is active.

    :type: bool
    """

    ik_weight: float
    """ Weight of the IK constraint between 0 and 1.Only defined for IK constraint.

    :type: float
    """

    ik_type: int
    """ Type of IK constraint, (read-only).Use one of `these constants<armatureconstraint-constants-ik-type>`.

    :type: int
    """

    ik_flag: int
    """ Combination of IK constraint option flags, read-only.Use one of `these constants<armatureconstraint-constants-ik-flag>`.

    :type: int
    """

    ik_dist: float
    """ Distance the constraint is trying to maintain with target, only used when ik_type=CONSTRAINT_IK_DISTANCE.

    :type: float
    """

    ik_mode: int
    """ Use one of `these constants<armatureconstraint-constants-ik-mode>`.Additional mode for IK constraint. Currently only used for Distance constraint:

    :type: int
    """
