import typing
import collections.abc
import typing_extensions
import bge.types.EXP_PyObjectPlus

class SCA_InputEvent(bge.types.EXP_PyObjectPlus.EXP_PyObjectPlus):
    """Events for a keyboard or mouse input."""

    status: list[int]
    """ A list of existing status of the input from the last frame.
Can contain `bge.logic.KX_INPUT_NONE` and `bge.logic.KX_INPUT_ACTIVE`.
The list always contains one value.
The first value of the list is the last value of the list in the last frame. (read-only)

    :type: list[int]
    """

    queue: list[int]
    """ A list of existing events of the input from the last frame.
Can contain `bge.logic.KX_INPUT_JUST_ACTIVATED` and `bge.logic.KX_INPUT_JUST_RELEASED`.
The list can be empty. (read-only)

    :type: list[int]
    """

    values: list[int]
    """ A list of existing value of the input from the last frame.
For keyboard it contains 1 or 0 and for mouse the coordinate of the mouse or the movement of the wheel mouse.
The list contains always one value, the size of the list is the same than `queue` + 1 only for keyboard inputs.
The first value of the list is the last value of the list in the last frame. (read-only)Example to get the non-normalized mouse coordinates:

    :type: list[int]
    """

    inactive: bool
    """ True if the input was inactive from the last frame.

    :type: bool
    """

    active: bool
    """ True if the input was active from the last frame.

    :type: bool
    """

    activated: bool
    """ True if the input was activated from the last frame.

    :type: bool
    """

    released: bool
    """ True if the input was released from the last frame.

    :type: bool
    """

    type: int
    """ The type of the input.
One of `these constants<keyboard-keys>`

    :type: int
    """
