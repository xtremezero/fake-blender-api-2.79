import typing
import collections.abc
import typing_extensions
import bge.types.SCA_IController

class SCA_NANDController(bge.types.SCA_IController.SCA_IController):
    """An NAND controller activates when all linked sensors are not active.There are no special python methods for this controller."""
