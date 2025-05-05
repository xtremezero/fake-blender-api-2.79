import typing
import collections.abc
import typing_extensions
import bpy.types

class ANIM_OT_keying_set_export(bpy.types.Operator):
    """Export Keying Set to a python script"""

    bl_idname: typing.Any
    bl_label: typing.Any
    bl_rna: typing.Any
    filepath: typing.Any
    filter_folder: typing.Any
    filter_python: typing.Any
    filter_text: typing.Any
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

    def invoke(self, context, event):
        """

        :param context:
        :param event:
        """

class BakeAction(bpy.types.Operator):
    """Bake all selected objects loc/scale/rotation animation to an action"""

    bake_types: typing.Any
    bl_idname: typing.Any
    bl_label: typing.Any
    bl_options: typing.Any
    bl_rna: typing.Any
    clear_constraints: typing.Any
    clear_parents: typing.Any
    frame_end: typing.Any
    frame_start: typing.Any
    id_data: typing.Any
    only_selected: typing.Any
    order: typing.Any
    step: typing.Any
    use_current_action: typing.Any
    visual_keying: typing.Any

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

class ClearUselessActions(bpy.types.Operator):
    """Mark actions with no F-Curves for deletion after save & reload of file preserving "action libraries" """

    bl_idname: typing.Any
    bl_label: typing.Any
    bl_options: typing.Any
    bl_rna: typing.Any
    id_data: typing.Any
    only_unused: typing.Any
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

class UpdateAnimatedTransformConstraint(bpy.types.Operator):
    """Update fcurves/drivers affecting Transform constraints (use it with files from 2.70 and earlier)"""

    bl_idname: typing.Any
    bl_label: typing.Any
    bl_options: typing.Any
    bl_rna: typing.Any
    id_data: typing.Any
    order: typing.Any
    use_convert_to_radians: typing.Any

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
