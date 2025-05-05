import typing
import collections.abc
import typing_extensions
import bge.types.EXP_PyObjectPlus

class SCA_PythonJoystick(bge.types.EXP_PyObjectPlus.EXP_PyObjectPlus):
    """A Python interface to a joystick."""

    name: str
    """ The name assigned to the joystick by the operating system. (read-only)

    :type: str
    """

    activeButtons: list
    """ A list of active button values. (read-only)

    :type: list
    """

    axisValues: list[int]
    """ The state of the joysticks axis as a list of values `numAxis` long. (read-only).Each specifying the value of an axis between -1.0 and 1.0
depending on how far the axis is pushed, 0 for nothing.
The first 2 values are used by most joysticks and gamepads for directional control.
3rd and 4th values are only on some joysticks and can be used for arbitary controls.

    :type: list[int]
    """

    hatValues: list[int]
    """ (Deprecated. Use :data:`activeButtons` instead)The state of the joysticks hats as a list of values `numHats` long. (read-only).Each specifying the direction of the hat from 1 to 12, 0 when inactive.Hat directions are as follows...

    :type: list[int]
    """

    numAxis: int
    """ The number of axes for the joystick at this index. (read-only).

    :type: int
    """

    numButtons: int
    """ The number of buttons for the joystick at this index. (read-only).

    :type: int
    """

    numHats: int
    """ (Deprecated. Use :data:`numButtons` instead)The number of hats for the joystick at this index. (read-only).

    :type: int
    """
