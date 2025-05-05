import typing
import collections.abc
import typing_extensions
import bge.types.EXP_PyObjectPlus

class SCA_PythonKeyboard(bge.types.EXP_PyObjectPlus.EXP_PyObjectPlus):
    """The current keyboard."""

    inputs: typing.Any
    """ A dictionary containing the input of each keyboard key. (read-only)."""

    events: typing.Any
    """ A dictionary containing the status of each keyboard event or key. (read-only).use :data:`inputs`"""

    activeInputs: typing.Any
    """ A dictionary containing the input of only the active keyboard keys. (read-only)."""

    active_events: typing.Any
    """ A dictionary containing the status of only the active keyboard events or keys. (read-only).use :data:`activeInputs`"""

    text: str
    """ The typed unicode text from the last frame.

    :type: str
    """

    def getClipboard(self) -> str:
        """Gets the clipboard text.

        :return:
        :rtype: str
        """

    def setClipboard(self, text: str):
        """Sets the clipboard text.

        :param text: New clipboard text
        :type text: str
        """
