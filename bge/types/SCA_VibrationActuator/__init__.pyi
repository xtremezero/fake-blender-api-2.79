import typing
import collections.abc
import typing_extensions
import bge.types.SCA_IActuator

class SCA_VibrationActuator(bge.types.SCA_IActuator.SCA_IActuator):
    """Vibration Actuator."""

    joyindex: typing.Any
    """ Joystick index."""

    strengthLeft: typing.Any
    """ Strength of the Low frequency joystick's motor (placed at left position usually)."""

    strengthRight: typing.Any
    """ Strength of the High frequency joystick's motor (placed at right position usually)."""

    duration: typing.Any
    """ Duration of the vibration in milliseconds."""

    isVibrating: typing.Any
    """ Check status of joystick vibration"""

    hasVibration: typing.Any
    """ Check if the joystick supports vibration"""

    def startVibration(self):
        """Starts the vibration.

        :return: None
        """

    def stopVibration(self):
        """Stops the vibration.

        :return: None
        """
