import typing
import collections.abc
import typing_extensions
import bge.types.EXP_Value

class KX_BatchGroup(bge.types.EXP_Value.EXP_Value):
    """The batch group is class containing a mesh resulting of the merging of meshes used by objects.
    The meshes are merged with the transformation of the objects using it.
    An instance of this class is not owned by one object but shared between objects.
    In consideration an instance of `KX_BatchGroup` have to instanced with as argument a list of at least one object containing the meshes to merge.
    This can be done in a way similar to:
    """

    objects: typing.Any
    """ The list of the objects merged. (read only)"""

    referenceObject: typing.Any
    """ The object used for object rendering settings (layer, color...)."""

    def merge(self, objects):
        """Merge meshes using the transformation of the objects using them.

        :param objects: The objects to merge.
        """

    def split(self, objects):
        """Split the meshes of the objects using them and restore their original meshes.

        :param objects: The objects to unmerge.
        """

    def destruct(self):
        """Destruct the batch group and restore all the objects to their original meshes."""
