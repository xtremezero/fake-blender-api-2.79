import typing
import collections.abc
import typing_extensions
import bge.types.BL_ArmatureConstraint
import bge.types.SCA_ISensor

class KX_ArmatureSensor(bge.types.SCA_ISensor.SCA_ISensor):
    """Armature sensor detect conditions on armatures."""

    type: int
    """ The type of measurement that the sensor make when it is active.Can be one of `these constants <armaturesensor-type>`

    :type: int
    """

    constraint: bge.types.BL_ArmatureConstraint.BL_ArmatureConstraint
    """ The constraint object this sensor is watching.

    :type: bge.types.BL_ArmatureConstraint.BL_ArmatureConstraint
    """

    value: float
    """ The threshold used in the comparison with the constraint error
The linear error is only updated on CopyPose/Distance IK constraint with iTaSC solver
The rotation error is only updated on CopyPose+rotation IK constraint with iTaSC solver
The linear error on CopyPose is always >= 0: it is the norm of the distance between the target and the bone
The rotation error on CopyPose is always >= 0: it is the norm of the equivalent rotation vector between the bone and the target orientations
The linear error on Distance can be positive if the distance between the bone and the target is greater than the desired distance, and negative if the distance is smaller.

    :type: float
    """
