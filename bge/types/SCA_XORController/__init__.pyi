import typing
import collections.abc
import typing_extensions
import bge.types.SCA_IController

class SCA_XORController(bge.types.SCA_IController.SCA_IController):
    """An XOR controller activates when there is the input is mixed, but not when all are on or off.There are no special python methods for this controller."""
