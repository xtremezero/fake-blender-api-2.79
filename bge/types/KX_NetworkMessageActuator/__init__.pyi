import typing
import collections.abc
import typing_extensions
import bge.types.SCA_IActuator

class KX_NetworkMessageActuator(bge.types.SCA_IActuator.SCA_IActuator):
    """Message Actuator"""

    propName: str
    """ Messages will only be sent to objects with the given property name.

    :type: str
    """

    subject: str
    """ The subject field of the message.

    :type: str
    """

    body: str
    """ The body of the message.

    :type: str
    """

    usePropBody: bool
    """ Send a property instead of a regular body message.

    :type: bool
    """
