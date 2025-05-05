import typing
import collections.abc
import typing_extensions
import bge.types.SCA_ILogicBrick

class SCA_IController(bge.types.SCA_ILogicBrick.SCA_ILogicBrick):
    """Base class for all controller logic bricks."""

    state: typing.Any
    """ The controllers state bitmask. This can be used with the GameObject's state to test if the controller is active."""

    sensors: typing.Any
    """ A list of sensors linked to this controller."""

    actuators: typing.Any
    """ A list of actuators linked to this controller."""

    useHighPriority: typing.Any
    """ When set the controller executes always before all other controllers that dont have this set."""
