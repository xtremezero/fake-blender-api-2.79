import typing
import collections.abc
import typing_extensions
import bge.types.KX_GameObject
import bge.types.SCA_IActuator
import mathutils

class KX_SteeringActuator(bge.types.SCA_IActuator.SCA_IActuator):
    """Steering Actuator for navigation."""

    behavior: typing.Any
    """ The steering behavior to use."""

    velocity: float
    """ Velocity magnitude

    :type: float
    """

    acceleration: float
    """ Max acceleration

    :type: float
    """

    turnspeed: float
    """ Max turn speed

    :type: float
    """

    distance: float
    """ Relax distance

    :type: float
    """

    target: bge.types.KX_GameObject.KX_GameObject
    """ Target object

    :type: bge.types.KX_GameObject.KX_GameObject
    """

    navmesh: bge.types.KX_GameObject.KX_GameObject
    """ Navigation mesh

    :type: bge.types.KX_GameObject.KX_GameObject
    """

    selfterminated: bool
    """ Terminate when target is reached

    :type: bool
    """

    enableVisualization: bool
    """ Enable debug visualization

    :type: bool
    """

    pathUpdatePeriod: int
    """ Path update period

    :type: int
    """

    path: list[mathutils.Vector]
    """ Path point list.

    :type: list[mathutils.Vector]
    """
