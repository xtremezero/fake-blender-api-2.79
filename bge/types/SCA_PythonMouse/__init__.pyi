import typing
import collections.abc
import typing_extensions
import bge.types.EXP_PyObjectPlus

class SCA_PythonMouse(bge.types.EXP_PyObjectPlus.EXP_PyObjectPlus):
    """The current mouse."""

    inputs: typing.Any
    """ A dictionary containing the input of each mouse event. (read-only)."""

    events: typing.Any
    """ a dictionary containing the status of each mouse event. (read-only).use :data:`inputs`"""

    activeInputs: typing.Any
    """ A dictionary containing the input of only the active mouse events. (read-only)."""

    active_events: typing.Any
    """ a dictionary containing the status of only the active mouse events. (read-only).use :data:`activeInputs`"""

    position: typing.Any
    """ The normalized x and y position of the mouse cursor."""

    visible: bool
    """ The visibility of the mouse cursor.

    :type: bool
    """
