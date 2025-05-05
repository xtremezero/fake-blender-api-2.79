import typing
import collections.abc
import typing_extensions
import bge.types.SCA_IController

class SCA_XNORController(bge.types.SCA_IController.SCA_IController):
    """An XNOR controller activates when all linked sensors are the same (activated or inative).There are no special python methods for this controller."""
