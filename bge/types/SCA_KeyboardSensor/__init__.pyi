import typing
import collections.abc
import typing_extensions
import bge.types.SCA_ISensor

class SCA_KeyboardSensor(bge.types.SCA_ISensor.SCA_ISensor):
    """A keyboard sensor detects player key presses.See module `bge.events` for keycode values."""

    key: typing.Any
    """ The key code this sensor is looking for."""

    hold1: typing.Any
    """ The key code for the first modifier this sensor is looking for."""

    hold2: typing.Any
    """ The key code for the second modifier this sensor is looking for."""

    toggleProperty: str
    """ The name of the property that indicates whether or not to log keystrokes as a string.

    :type: str
    """

    targetProperty: str
    """ The name of the property that receives keystrokes in case in case a string is logged.

    :type: str
    """

    useAllKeys: bool
    """ Flag to determine whether or not to accept all keys.

    :type: bool
    """

    inputs: typing.Any
    """ A list of pressed input keys that have either been pressed, or just released, or are active this frame. (read-only)."""

    events: typing.Any
    """ a list of pressed keys that have either been pressed, or just released, or are active this frame. (read-only).use :data:`inputs`"""

    def getKeyStatus(self, keycode: int) -> int:
        """Get the status of a key.

        :param keycode: The code that represents the key you want to get the state of, use one of `these constants<keyboard-keys>`
        :type keycode: int
        :return: The state of the given key, can be one of `these constants<input-status>`
        :rtype: int
        """
