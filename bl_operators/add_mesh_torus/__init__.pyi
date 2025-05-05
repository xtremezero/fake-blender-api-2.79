import typing
import collections.abc
import typing_extensions
import bpy.types
import bpy_extras.object_utils

class AddTorus(bpy.types.Operator, bpy_extras.object_utils.AddObjectHelper):
    """Add a torus mesh"""

    abso_major_rad: typing.Any
    abso_minor_rad: typing.Any
    bl_idname: typing.Any
    bl_label: typing.Any
    bl_options: typing.Any
    bl_rna: typing.Any
    generate_uvs: typing.Any
    id_data: typing.Any
    layers: typing.Any
    location: typing.Any
    major_radius: typing.Any
    major_segments: typing.Any
    minor_radius: typing.Any
    minor_segments: typing.Any
    mode: typing.Any
    order: typing.Any
    rotation: typing.Any
    view_align: typing.Any

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

    def draw(self, context):
        """

        :param context:
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

    def mode_update_callback(self, context):
        """

        :param context:
        """

def add_torus(major_rad, minor_rad, major_seg, minor_seg): ...
def add_uvs(mesh, minor_seg, major_seg): ...
