import typing
import collections.abc
import typing_extensions
import bge.types.SCA_ISensor

class KX_NetworkMessageSensor(bge.types.SCA_ISensor.SCA_ISensor):
    """The Message Sensor logic brick.Currently only loopback (local) networks are supported."""

    subject: str
    """ The subject the sensor is looking for.

    :type: str
    """

    frameMessageCount: int
    """ The number of messages received since the last frame. (read-only).

    :type: int
    """

    subjects: list[str]
    """ The list of message subjects received. (read-only).

    :type: list[str]
    """

    bodies: list[str]
    """ The list of message bodies received. (read-only).

    :type: list[str]
    """
