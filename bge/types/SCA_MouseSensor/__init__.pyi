import typing
import collections.abc
import typing_extensions
import bge.types.SCA_ISensor

class SCA_MouseSensor(bge.types.SCA_ISensor.SCA_ISensor):
    """Mouse Sensor logic brick."""

    position: [int]
    """ current [x, y] coordinates of the mouse, in frame coordinates (pixels).

    :type: [int]
    """

    mode: int
    """ sensor mode.

    :type: int
    """

    def getButtonStatus(self, button: int) -> int:
        """Get the mouse button status.

        :param button: The code that represents the key you want to get the state of, use one of `these constants<mouse-keys>`
        :type button: int
        :return: The state of the given key, can be one of `these constants<input-status>`
        :rtype: int
        """
