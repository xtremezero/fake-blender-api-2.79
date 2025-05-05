import typing
import collections.abc
import typing_extensions
import bge.types.SCA_IActuator
import mathutils

class KX_ConstraintActuator(bge.types.SCA_IActuator.SCA_IActuator):
    """A constraint actuator limits the position, rotation, distance or orientation of an object."""

    damp: int
    """ Time constant of the constraint expressed in frame (not use by Force field constraint).

    :type: int
    """

    rotDamp: int
    """ Time constant for the rotation expressed in frame (only for the distance constraint), 0 = use damp for rotation as well.

    :type: int
    """

    direction: mathutils.Vector
    """ The reference direction in world coordinate for the orientation constraint.

    :type: mathutils.Vector
    """

    option: int
    """ Binary combination of `these constants <constraint-actuator-option>`

    :type: int
    """

    time: int
    """ activation time of the actuator. The actuator disables itself after this many frame. If set to 0, the actuator is not limited in time.

    :type: int
    """

    propName: str
    """ the name of the property or material for the ray detection of the distance constraint.

    :type: str
    """

    min: float
    """ The lower bound of the constraint. For the rotation and orientation constraint, it represents radiant.

    :type: float
    """

    distance: float
    """ the target distance of the distance constraint.

    :type: float
    """

    max: float
    """ the upper bound of the constraint. For rotation and orientation constraints, it represents radiant.

    :type: float
    """

    rayLength: float
    """ the length of the ray of the distance constraint.

    :type: float
    """

    limit: int
    """ type of constraint. Use one of the `these constants <constraint-actuator-limit>`

    :type: int
    """
