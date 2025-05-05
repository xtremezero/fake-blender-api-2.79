import typing
import collections.abc
import typing_extensions
import bge.types.SCA_IActuator

class KX_GameActuator(bge.types.SCA_IActuator.SCA_IActuator):
    """The game actuator loads a new .blend file, restarts the current .blend file or quits the game."""

    fileName: str
    """ the new .blend file to load.

    :type: str
    """

    mode: typing.Any
    """ The mode of this actuator. Can be on of `these constants <game-actuator>`"""
