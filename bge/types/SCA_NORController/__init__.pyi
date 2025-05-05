import typing
import collections.abc
import typing_extensions
import bge.types.SCA_IController

class SCA_NORController(bge.types.SCA_IController.SCA_IController):
    """An NOR controller activates only when all linked sensors are de-activated.There are no special python methods for this controller."""
