import typing
import collections.abc
import typing_extensions
import bpy.types

class VertexPaintDirt(bpy.types.Operator):
    bl_idname: typing.Any
    bl_label: typing.Any
    bl_options: typing.Any
    bl_rna: typing.Any
    blur_iterations: typing.Any
    blur_strength: typing.Any
    clean_angle: typing.Any
    dirt_angle: typing.Any
    dirt_only: typing.Any
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

def applyVertexDirt(
    me, blur_iterations, blur_strength, clamp_dirt, clamp_clean, dirt_only
): ...
def get_vcolor_layer_data(me): ...
