import typing
import collections.abc
import typing_extensions
import bge.types.SCA_IActuator

class KX_SoundActuator(bge.types.SCA_IActuator.SCA_IActuator):
    """Sound Actuator.The `startSound`, `pauseSound` and `stopSound` do not require the actuator to be activated - they act instantly provided that the actuator has been activated once at least."""

    volume: float
    """ The volume (gain) of the sound.

    :type: float
    """

    time: float
    """ The current position in the audio stream (in seconds).

    :type: float
    """

    pitch: float
    """ The pitch of the sound.

    :type: float
    """

    mode: int
    """ The operation mode of the actuator. Can be one of `these constants<logic-sound-actuator>`

    :type: int
    """

    sound: typing.Any
    """ The sound the actuator should play."""

    is3D: bool
    """ Whether or not the actuator should be using 3D sound. (read-only)

    :type: bool
    """

    volume_maximum: float
    """ The maximum gain of the sound, no matter how near it is.

    :type: float
    """

    volume_minimum: float
    """ The minimum gain of the sound, no matter how far it is away.

    :type: float
    """

    distance_reference: float
    """ The distance where the sound has a gain of 1.0.

    :type: float
    """

    distance_maximum: float
    """ The maximum distance at which you can hear the sound.

    :type: float
    """

    attenuation: float
    """ The influence factor on volume depending on distance.

    :type: float
    """

    cone_angle_inner: float
    """ The angle of the inner cone.

    :type: float
    """

    cone_angle_outer: float
    """ The angle of the outer cone.

    :type: float
    """

    cone_volume_outer: float
    """ The gain outside the outer cone (the gain in the outer cone will be interpolated between this value and the normal gain in the inner cone).

    :type: float
    """

    def startSound(self):
        """Starts the sound.

        :return: None
        """

    def pauseSound(self):
        """Pauses the sound.

        :return: None
        """

    def stopSound(self):
        """Stops the sound.

        :return: None
        """
