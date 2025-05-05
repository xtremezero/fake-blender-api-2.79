import typing
import collections.abc
import typing_extensions
import bge.types.KX_GameObject
import bge.types.SCA_IActuator

class KX_TrackToActuator(bge.types.SCA_IActuator.SCA_IActuator):
    """Edit Object actuator in Track To mode."""

    object: bge.types.KX_GameObject.KX_GameObject | None
    """ the object this actuator tracks.

    :type: bge.types.KX_GameObject.KX_GameObject | None
    """

    time: int
    """ the time in frames with which to delay the tracking motion.

    :type: int
    """

    use3D: bool
    """ the tracking motion to use 3D.

    :type: bool
    """

    upAxis: typing.Any
    """ The axis that points upward."""

    trackAxis: typing.Any
    """ The axis that points to the target object."""
