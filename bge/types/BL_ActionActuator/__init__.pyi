import typing
import collections.abc
import typing_extensions
import bge.types.SCA_IActuator

class BL_ActionActuator(bge.types.SCA_IActuator.SCA_IActuator):
    """Action Actuators apply an action to an actor."""

    action: str
    """ The name of the action to set as the current action.

    :type: str
    """

    frameStart: float
    """ Specifies the starting frame of the animation.

    :type: float
    """

    frameEnd: float
    """ Specifies the ending frame of the animation.

    :type: float
    """

    blendIn: float
    """ Specifies the number of frames of animation to generate when making transitions between actions.

    :type: float
    """

    priority: int
    """ Sets the priority of this actuator. Actuators will lower priority numbers will override actuators with higher numbers.

    :type: int
    """

    frame: float
    """ Sets the current frame for the animation.

    :type: float
    """

    propName: str
    """ Sets the property to be used in FromProp playback mode.

    :type: str
    """

    mode: int
    """ The operation mode of the actuator. Can be one of `these constants<action-actuator>`.

    :type: int
    """

    useContinue: bool
    """ The actions continue option, True or False. When True, the action will always play from where last left off,
otherwise negative events to this actuator will reset it to its start frame.

    :type: bool
    """

    framePropName: str
    """ The name of the property that is set to the current frame number.

    :type: str
    """
