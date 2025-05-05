import typing
import collections.abc
import typing_extensions
import bge.types.EXP_PyObjectPlus

class KX_ConstraintWrapper(bge.types.EXP_PyObjectPlus.EXP_PyObjectPlus):
    """KX_ConstraintWrapper"""

    constraint_id: int
    """ Returns the contraint ID  (read only)

    :type: int
    """

    constraint_type: int
    """ Returns the contraint type (read only)

    :type: int
    """

    breakingThreshold: typing.Any
    """ The impulse threshold breaking the constraint, if the constraint is broken `enabled` is set to False."""

    enabled: bool
    """ The status of the constraint. Set to True to restore a constraint after breaking.

    :type: bool
    """

    def getConstraintId(self, val) -> int:
        """Returns the contraint ID

        :param val:
        :return: the constraint ID
        :rtype: int
        """

    def setParam(self, axis: int, value0: float, value1: float):
        """Set the contraint limitsFor PHY_LINEHINGE_CONSTRAINT = 2 or PHY_ANGULAR_CONSTRAINT = 3:For PHY_CONE_TWIST_CONSTRAINT = 4:For PHY_GENERIC_6DOF_CONSTRAINT = 12:

        :param axis:
        :type axis: int
        :param value0: Set the minimum limit of the axisSet the minimum limit of the axisSet the minimum limit of the axisSet the linear velocity of the axisSet the stiffness of the spring
        :type value0: float
        :param value1: Set the maximum limit of the axisSet the maximum limit of the axisSet the maximum limit of the axisSet the maximum force limit of the axisTendency of the spring to return to it's original position
        :type value1: float
        """

    def getParam(self, axis: int) -> float:
        """Get the contraint position or euler angle of a generic 6DOF constraint

        :param axis:
        :type axis: int
        :return: position
        :rtype: float
        """
