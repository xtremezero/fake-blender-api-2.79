import typing
import collections.abc
import typing_extensions
import bge.types.SCA_IActuator
import mathutils

class KX_MouseActuator(bge.types.SCA_IActuator.SCA_IActuator):
    """The mouse actuator gives control over the visibility of the mouse cursor and rotates the parent object according to mouse movement."""

    visible: bool
    """ The visibility of the mouse cursor.

    :type: bool
    """

    use_axis_x: bool
    """ Mouse movement along the x axis effects object rotation.

    :type: bool
    """

    use_axis_y: bool
    """ Mouse movement along the y axis effects object rotation.

    :type: bool
    """

    threshold: mathutils.Vector
    """ Amount of movement from the mouse required before rotation is triggered.The values in the list should be between 0.0 and 0.5.

    :type: mathutils.Vector
    """

    reset_x: bool
    """ Mouse is locked to the center of the screen on the x axis.

    :type: bool
    """

    reset_y: bool
    """ Mouse is locked to the center of the screen on the y axis.

    :type: bool
    """

    object_axis: typing.Any
    """ The object's 3D axis to rotate with the mouse movement. ([x, y])"""

    local_x: bool
    """ Rotation caused by mouse movement along the x axis is local.

    :type: bool
    """

    local_y: bool
    """ Rotation caused by mouse movement along the y axis is local.

    :type: bool
    """

    sensitivity: mathutils.Vector
    """ The amount of rotation caused by mouse movement along the x and y axis.Negative values invert the rotation.

    :type: mathutils.Vector
    """

    limit_x: mathutils.Vector
    """ The minimum and maximum angle of rotation caused by mouse movement along the x axis in degrees.
limit_x[0] is minimum, limit_x[1] is maximum.

    :type: mathutils.Vector
    """

    limit_y: mathutils.Vector
    """ The minimum and maximum angle of rotation caused by mouse movement along the y axis in degrees.
limit_y[0] is minimum, limit_y[1] is maximum.

    :type: mathutils.Vector
    """

    angle: mathutils.Vector
    """ The current rotational offset caused by the mouse actuator in degrees.

    :type: mathutils.Vector
    """

    def reset(self):
        """Undoes the rotation caused by the mouse actuator."""
