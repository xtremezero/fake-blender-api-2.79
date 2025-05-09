import typing
import collections.abc
import typing_extensions
import bpy.types

class BakeToKeyframes(bpy.types.Operator):
    """Bake rigid body transformations of selected objects to keyframes"""

    bl_idname: typing.Any
    bl_label: typing.Any
    bl_options: typing.Any
    bl_rna: typing.Any
    frame_end: typing.Any
    frame_start: typing.Any
    id_data: typing.Any
    order: typing.Any
    step: typing.Any

    def bl_rna_get_subclass(self) -> bpy.types.Struct:
        """

        :return: The RNA type or default when not found.
        :rtype: bpy.types.Struct
        """

    def bl_rna_get_subclass_py(self) -> typing.Any:
        """

        :return: The class or default when not found.
        :rtype: typing.Any
        """

    def execute(self, context):
        """

        :param context:
        """

    def invoke(self, context, event):
        """

        :param context:
        :param event:
        """

    @classmethod
    def poll(cls, context):
        """

        :param context:
        """

class ConnectRigidBodies(bpy.types.Operator):
    """Create rigid body constraints between selected rigid bodies"""

    bl_idname: typing.Any
    bl_label: typing.Any
    bl_options: typing.Any
    bl_rna: typing.Any
    con_type: typing.Any
    connection_pattern: typing.Any
    id_data: typing.Any
    order: typing.Any
    pivot_type: typing.Any

    def bl_rna_get_subclass(self) -> bpy.types.Struct:
        """

        :return: The RNA type or default when not found.
        :rtype: bpy.types.Struct
        """

    def bl_rna_get_subclass_py(self) -> typing.Any:
        """

        :return: The class or default when not found.
        :rtype: typing.Any
        """

    def execute(self, context):
        """

        :param context:
        """

    @classmethod
    def poll(cls, context):
        """

        :param context:
        """

class CopyRigidbodySettings(bpy.types.Operator):
    """Copy Rigid Body settings from active object to selected"""

    bl_idname: typing.Any
    bl_label: typing.Any
    bl_options: typing.Any
    bl_rna: typing.Any
    id_data: typing.Any
    order: typing.Any

    def bl_rna_get_subclass(self) -> bpy.types.Struct:
        """

        :return: The RNA type or default when not found.
        :rtype: bpy.types.Struct
        """

    def bl_rna_get_subclass_py(self) -> typing.Any:
        """

        :return: The class or default when not found.
        :rtype: typing.Any
        """

    def execute(self, context):
        """

        :param context:
        """

    @classmethod
    def poll(cls, context):
        """

        :param context:
        """
