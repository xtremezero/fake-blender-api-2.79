import typing
import collections.abc
import typing_extensions
import bge.types.SCA_IActuator

class KX_SCA_ReplaceMeshActuator(bge.types.SCA_IActuator.SCA_IActuator):
    """Edit Object actuator, in Replace Mesh mode."""

    mesh: typing.Any
    """ `MeshProxy` or the name of the mesh that will replace the current one.Set to None to disable actuator."""

    useDisplayMesh: bool
    """ when true the displayed mesh is replaced.

    :type: bool
    """

    usePhysicsMesh: bool
    """ when true the physics mesh is replaced.

    :type: bool
    """

    def instantReplaceMesh(self):
        """Immediately replace mesh without delay."""
