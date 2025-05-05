import typing
import collections.abc
import typing_extensions
import bge.types.SCA_ISensor

class SCA_PropertySensor(bge.types.SCA_ISensor.SCA_ISensor):
    """Activates when the game object property matches."""

    mode: int
    """ Type of check on the property. Can be one of `these constants <logic-property-sensor>`

    :type: int
    """

    propName: str
    """ the property the sensor operates.

    :type: str
    """

    value: str
    """ the value with which the sensor compares to the value of the property.

    :type: str
    """

    min: str
    """ the minimum value of the range used to evaluate the property when in interval mode.

    :type: str
    """

    max: str
    """ the maximum value of the range used to evaluate the property when in interval mode.

    :type: str
    """
