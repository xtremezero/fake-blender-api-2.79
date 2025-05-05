import typing
import collections.abc
import typing_extensions
import bge.types.SCA_IController

class SCA_ANDController(bge.types.SCA_IController.SCA_IController):
    """An AND controller activates only when all linked sensors are activated.There are no special python methods for this controller."""
