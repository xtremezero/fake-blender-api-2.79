import typing
import collections.abc
import typing_extensions
import bge.types.SCA_IActuator

class KX_SceneActuator(bge.types.SCA_IActuator.SCA_IActuator):
    """Scene Actuator logic brick."""

    scene: str
    """ the name of the scene to change to/overlay/underlay/remove/suspend/resume.

    :type: str
    """

    camera: str
    """ the camera to change to.

    :type: str
    """

    useRestart: bool
    """ Set flag to True to restart the sene.

    :type: bool
    """

    mode: typing.Any
    """ The mode of the actuator."""
