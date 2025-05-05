import typing
import collections.abc
import typing_extensions
import bge.types.SCA_ISensor

class SCA_JoystickSensor(bge.types.SCA_ISensor.SCA_ISensor):
    """This sensor detects player joystick events."""

    axisValues: list[int]
    """ The state of the joysticks axis as a list of values `numAxis` long. (read-only).Each specifying the value of an axis between -32767 and 32767 depending on how far the axis is pushed, 0 for nothing.
The first 2 values are used by most joysticks and gamepads for directional control. 3rd and 4th values are only on some joysticks and can be used for arbitary controls.

    :type: list[int]
    """

    axisSingle: int
    """ like `axisValues` but returns a single axis value that is set by the sensor. (read-only).

    :type: int
    """

    hatValues: list[int]
    """ (Deprecated. Use :data:button instead)The state of the joysticks hats as a list of values `numHats` long. (read-only).Each specifying the direction of the hat from 1 to 12, 0 when inactive.Hat directions are as follows...

    :type: list[int]
    """

    hatSingle: int
    """ (Deprecated. Use :data:button instead)Like `hatValues` but returns a single hat direction value that is set by the sensor. (read-only).

    :type: int
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
    """ (Deprecated. Use :data:numButtons instead)The number of hats for the joystick at this index. (read-only).

    :type: int
    """

    connected: bool
    """ True if a joystick is connected at this joysticks index. (read-only).

    :type: bool
    """

    index: int
    """ The joystick index to use (from 0 to 7). The first joystick is always 0.

    :type: int
    """

    threshold: int
    """ Axis threshold. Joystick axis motion below this threshold wont trigger an event. Use values between (0 and 32767), lower values are more sensitive.

    :type: int
    """

    button: int
    """ The button index the sensor reacts to (first button = 0). When the "All Events" toggle is set, this option has no effect.

    :type: int
    """

    axis: [int, int]
    """ The axis this sensor reacts to, as a list of two values [axisIndex, axisDirection]

    :type: [int, int]
    """

    hat: [int, int]
    """ (Deprecated. Use :data:button instead)The hat the sensor reacts to, as a list of two values: [hatIndex, hatDirection]

    :type: [int, int]
    """

    def getButtonActiveList(self) -> list:
        """

        :return: A list containing the indicies of the currently pressed buttons.
        :rtype: list
        """

    def getButtonStatus(self, buttonIndex: int) -> bool:
        """

        :param buttonIndex: the button index, 0=first button
        :type buttonIndex: int
        :return: The current pressed state of the specified button.
        :rtype: bool
        """
