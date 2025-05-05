import typing
import collections.abc
import typing_extensions
import bge.types.SCA_IController

class SCA_ORController(bge.types.SCA_IController.SCA_IController):
    """An OR controller activates when any connected sensor activates.There are no special python methods for this controller."""
