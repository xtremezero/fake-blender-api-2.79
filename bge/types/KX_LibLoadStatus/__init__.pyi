import typing
import collections.abc
import typing_extensions
import bge.types.EXP_PyObjectPlus

class KX_LibLoadStatus(bge.types.EXP_PyObjectPlus.EXP_PyObjectPlus):
    """An object providing information about a LibLoad() operation."""

    onFinish: collections.abc.Callable
    """ A callback that gets called when the lib load is done.

    :type: collections.abc.Callable
    """

    finished: bool
    """ The current status of the lib load.

    :type: bool
    """

    progress: float
    """ The current progress of the lib load as a normalized value from 0.0 to 1.0.

    :type: float
    """

    libraryName: str
    """ The name of the library being loaded (the first argument to LibLoad).

    :type: str
    """

    timeTaken: float
    """ The amount of time, in seconds, the lib load took (0 until the operation is complete).

    :type: float
    """
