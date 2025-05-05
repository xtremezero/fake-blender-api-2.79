import typing
import collections.abc
import typing_extensions
import bge.types.KX_GameObject
import bge.types.SCA_IController

class SCA_PythonController(bge.types.SCA_IController.SCA_IController):
    """A Python controller uses a Python script to activate it's actuators,
    based on it's sensors.
    """

    owner: bge.types.KX_GameObject.KX_GameObject
    """ The object the controller is attached to.

    :type: bge.types.KX_GameObject.KX_GameObject
    """

    script: str
    """ The value of this variable depends on the execution methid.

    :type: str
    """

    mode: int
    """ the execution mode for this controller (read-only).

    :type: int
    """

    def activate(self, actuator):
        """Activates an actuator attached to this controller.

        :param actuator: The actuator to operate on.
        """

    def deactivate(self, actuator):
        """Deactivates an actuator attached to this controller.

        :param actuator: The actuator to operate on.
        """
