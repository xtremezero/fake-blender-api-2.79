import typing
import collections.abc
import typing_extensions
import bge.types.KX_GameObject
import bge.types.SCA_IActuator

class KX_SCA_AddObjectActuator(bge.types.SCA_IActuator.SCA_IActuator):
    """Edit Object Actuator (in Add Object Mode)"""

    object: bge.types.KX_GameObject.KX_GameObject | None
    """ the object this actuator adds.

    :type: bge.types.KX_GameObject.KX_GameObject | None
    """

    objectLastCreated: bge.types.KX_GameObject.KX_GameObject | None
    """ the last added object from this actuator (read-only).

    :type: bge.types.KX_GameObject.KX_GameObject | None
    """

    time: float
    """ the lifetime of added objects, in frames. Set to 0 to disable automatic deletion.

    :type: float
    """

    linearVelocity: typing.Any
    """ the initial linear velocity of added objects."""

    angularVelocity: typing.Any
    """ the initial angular velocity of added objects."""

    def instantAddObject(self):
        """adds the object without needing to calling SCA_PythonController.activate()"""
