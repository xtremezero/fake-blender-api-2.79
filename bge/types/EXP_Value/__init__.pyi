import typing
import collections.abc
import typing_extensions
import bge.types.EXP_PyObjectPlus

class EXP_Value(bge.types.EXP_PyObjectPlus.EXP_PyObjectPlus):
    """This class is a basis for other classes."""

    name: str
    """ The name of this EXP_Value derived object (read-only).

    :type: str
    """
