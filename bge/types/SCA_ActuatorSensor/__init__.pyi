import typing
import collections.abc
import typing_extensions
import bge.types.SCA_ISensor

class SCA_ActuatorSensor(bge.types.SCA_ISensor.SCA_ISensor):
    """Actuator sensor detect change in actuator state of the parent object.
    It generates a positive pulse if the corresponding actuator is activated
    and a negative pulse if the actuator is deactivated.
    """

    actuator: str
    """ the name of the actuator that the sensor is monitoring.

    :type: str
    """
