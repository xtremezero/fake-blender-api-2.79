import typing
import collections.abc
import typing_extensions
import bge.types.SCA_IActuator

class SCA_2DFilterActuator(bge.types.SCA_IActuator.SCA_IActuator):
    """Create, enable and disable 2D filters.The following properties don't have an immediate effect.
    You must active the actuator to get the result.
    The actuator is not persistent: it automatically stops itself after setting up the filter
    but the filter remains active. To stop a filter you must activate the actuator with 'type'
    set to `~bge.logic.RAS_2DFILTER_DISABLED` or `~bge.logic.RAS_2DFILTER_NOFILTER`.
    """

    shaderText: str
    """ shader source code for custom shader.

    :type: str
    """

    disableMotionBlur: int
    """ action on motion blur: 0=enable, 1=disable.

    :type: int
    """

    mode: int
    """ Type of 2D filter, use one of `these constants <Two-D-FilterActuator-mode>`.

    :type: int
    """

    passNumber: typing.Any
    """ order number of filter in the stack of 2D filters. Filters are executed in increasing order of passNb.Only be one filter can be defined per passNb."""

    value: typing.Any
    """ argument for motion blur filter."""
