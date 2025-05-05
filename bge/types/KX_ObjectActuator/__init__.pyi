import typing
import collections.abc
import typing_extensions
import bge.types.KX_GameObject
import bge.types.SCA_IActuator

class KX_ObjectActuator(bge.types.SCA_IActuator.SCA_IActuator):
    """The object actuator ("Motion Actuator") applies force, torque, displacement, angular displacement,
    velocity, or angular velocity to an object.
    Servo control allows to regulate force to achieve a certain speed target.
    """

    force: typing.Any
    """ The force applied by the actuator."""

    useLocalForce: bool
    """ A flag specifying if the force is local.

    :type: bool
    """

    torque: typing.Any
    """ The torque applied by the actuator."""

    useLocalTorque: bool
    """ A flag specifying if the torque is local.

    :type: bool
    """

    dLoc: typing.Any
    """ The displacement vector applied by the actuator."""

    useLocalDLoc: bool
    """ A flag specifying if the dLoc is local.

    :type: bool
    """

    dRot: typing.Any
    """ The angular displacement vector applied by the actuator"""

    useLocalDRot: bool
    """ A flag specifying if the dRot is local.

    :type: bool
    """

    linV: typing.Any
    """ The linear velocity applied by the actuator."""

    useLocalLinV: bool
    """ A flag specifying if the linear velocity is local.

    :type: bool
    """

    angV: typing.Any
    """ The angular velocity applied by the actuator."""

    useLocalAngV: bool
    """ A flag specifying if the angular velocity is local.

    :type: bool
    """

    damping: typing.Any
    """ The damping parameter of the servo controller."""

    forceLimitX: typing.Any
    """ The min/max force limit along the X axis and activates or deactivates the limits in the servo controller."""

    forceLimitY: typing.Any
    """ The min/max force limit along the Y axis and activates or deactivates the limits in the servo controller."""

    forceLimitZ: typing.Any
    """ The min/max force limit along the Z axis and activates or deactivates the limits in the servo controller."""

    pid: list[float]
    """ The PID coefficients of the servo controller.

    :type: list[float]
    """

    reference: bge.types.KX_GameObject.KX_GameObject | None
    """ The object that is used as reference to compute the velocity for the servo controller.

    :type: bge.types.KX_GameObject.KX_GameObject | None
    """
