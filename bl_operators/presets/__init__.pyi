import typing
import collections.abc
import typing_extensions
import bpy.types

class AddPresetBase:
    bl_options: typing.Any
    name: typing.Any
    order: typing.Any
    remove_active: typing.Any

    @staticmethod
    def as_filename(name):
        """

        :param name:
        """

    def check(self, context):
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

class AddPresetCamera(AddPresetBase, bpy.types.Operator):
    """Add or remove a Camera Preset"""

    bl_idname: typing.Any
    bl_label: typing.Any
    bl_options: typing.Any
    bl_rna: typing.Any
    id_data: typing.Any
    name: typing.Any
    order: typing.Any
    preset_defines: typing.Any
    preset_menu: typing.Any
    preset_subdir: typing.Any
    preset_values: typing.Any
    remove_active: typing.Any
    use_focal_length: typing.Any

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

class AddPresetCloth(AddPresetBase, bpy.types.Operator):
    """Add or remove a Cloth Preset"""

    bl_idname: typing.Any
    bl_label: typing.Any
    bl_options: typing.Any
    bl_rna: typing.Any
    id_data: typing.Any
    name: typing.Any
    order: typing.Any
    preset_defines: typing.Any
    preset_menu: typing.Any
    preset_subdir: typing.Any
    preset_values: typing.Any
    remove_active: typing.Any

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

class AddPresetFluid(AddPresetBase, bpy.types.Operator):
    """Add or remove a Fluid Preset"""

    bl_idname: typing.Any
    bl_label: typing.Any
    bl_options: typing.Any
    bl_rna: typing.Any
    id_data: typing.Any
    name: typing.Any
    order: typing.Any
    preset_defines: typing.Any
    preset_menu: typing.Any
    preset_subdir: typing.Any
    preset_values: typing.Any
    remove_active: typing.Any

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

class AddPresetHairDynamics(AddPresetBase, bpy.types.Operator):
    """Add or remove a Hair Dynamics Preset"""

    bl_idname: typing.Any
    bl_label: typing.Any
    bl_options: typing.Any
    bl_rna: typing.Any
    id_data: typing.Any
    name: typing.Any
    order: typing.Any
    preset_defines: typing.Any
    preset_menu: typing.Any
    preset_subdir: typing.Any
    preset_values: typing.Any
    remove_active: typing.Any

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

class AddPresetInteraction(AddPresetBase, bpy.types.Operator):
    """Add or remove an Application Interaction Preset"""

    bl_idname: typing.Any
    bl_label: typing.Any
    bl_options: typing.Any
    bl_rna: typing.Any
    id_data: typing.Any
    name: typing.Any
    order: typing.Any
    preset_defines: typing.Any
    preset_menu: typing.Any
    preset_subdir: typing.Any
    preset_values: typing.Any
    remove_active: typing.Any

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

class AddPresetInterfaceTheme(AddPresetBase, bpy.types.Operator):
    """Add or remove a theme preset"""

    bl_idname: typing.Any
    bl_label: typing.Any
    bl_options: typing.Any
    bl_rna: typing.Any
    id_data: typing.Any
    name: typing.Any
    order: typing.Any
    preset_menu: typing.Any
    preset_subdir: typing.Any
    remove_active: typing.Any

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

class AddPresetKeyconfig(AddPresetBase, bpy.types.Operator):
    """Add or remove a Key-config Preset"""

    bl_idname: typing.Any
    bl_label: typing.Any
    bl_options: typing.Any
    bl_rna: typing.Any
    id_data: typing.Any
    name: typing.Any
    order: typing.Any
    preset_menu: typing.Any
    preset_subdir: typing.Any
    remove_active: typing.Any

    def add(self, context, filepath):
        """

        :param context:
        :param filepath:
        """

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

    def post_cb(self, context):
        """

        :param context:
        """

    def pre_cb(self, context):
        """

        :param context:
        """

class AddPresetNodeColor(AddPresetBase, bpy.types.Operator):
    """Add or remove a Node Color Preset"""

    bl_idname: typing.Any
    bl_label: typing.Any
    bl_options: typing.Any
    bl_rna: typing.Any
    id_data: typing.Any
    name: typing.Any
    order: typing.Any
    preset_defines: typing.Any
    preset_menu: typing.Any
    preset_subdir: typing.Any
    preset_values: typing.Any
    remove_active: typing.Any

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

class AddPresetOperator(AddPresetBase, bpy.types.Operator):
    """Add or remove an Operator Preset"""

    bl_idname: typing.Any
    bl_label: typing.Any
    bl_options: typing.Any
    bl_rna: typing.Any
    id_data: typing.Any
    name: typing.Any
    operator: typing.Any
    order: typing.Any
    preset_defines: typing.Any
    preset_menu: typing.Any
    preset_subdir: typing.Any
    preset_values: typing.Any
    remove_active: typing.Any

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

    @staticmethod
    def operator_path(operator):
        """

        :param operator:
        """

class AddPresetRender(AddPresetBase, bpy.types.Operator):
    """Add or remove a Render Preset"""

    bl_idname: typing.Any
    bl_label: typing.Any
    bl_options: typing.Any
    bl_rna: typing.Any
    id_data: typing.Any
    name: typing.Any
    order: typing.Any
    preset_defines: typing.Any
    preset_menu: typing.Any
    preset_subdir: typing.Any
    preset_values: typing.Any
    remove_active: typing.Any

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

class AddPresetSSS(AddPresetBase, bpy.types.Operator):
    """Add or remove a Subsurface Scattering Preset"""

    bl_idname: typing.Any
    bl_label: typing.Any
    bl_options: typing.Any
    bl_rna: typing.Any
    id_data: typing.Any
    name: typing.Any
    order: typing.Any
    preset_defines: typing.Any
    preset_menu: typing.Any
    preset_subdir: typing.Any
    preset_values: typing.Any
    remove_active: typing.Any

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

class AddPresetSafeAreas(AddPresetBase, bpy.types.Operator):
    """Add or remove a Safe Areas Preset"""

    bl_idname: typing.Any
    bl_label: typing.Any
    bl_options: typing.Any
    bl_rna: typing.Any
    id_data: typing.Any
    name: typing.Any
    order: typing.Any
    preset_defines: typing.Any
    preset_menu: typing.Any
    preset_subdir: typing.Any
    preset_values: typing.Any
    remove_active: typing.Any

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

class AddPresetSunSky(AddPresetBase, bpy.types.Operator):
    """Add or remove a Sky & Atmosphere Preset"""

    bl_idname: typing.Any
    bl_label: typing.Any
    bl_options: typing.Any
    bl_rna: typing.Any
    id_data: typing.Any
    name: typing.Any
    order: typing.Any
    preset_defines: typing.Any
    preset_menu: typing.Any
    preset_subdir: typing.Any
    preset_values: typing.Any
    remove_active: typing.Any

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

class AddPresetTrackingCamera(AddPresetBase, bpy.types.Operator):
    """Add or remove a Tracking Camera Intrinsics Preset"""

    bl_idname: typing.Any
    bl_label: typing.Any
    bl_options: typing.Any
    bl_rna: typing.Any
    id_data: typing.Any
    name: typing.Any
    order: typing.Any
    preset_defines: typing.Any
    preset_menu: typing.Any
    preset_subdir: typing.Any
    preset_values: typing.Any
    remove_active: typing.Any
    use_focal_length: typing.Any

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

class AddPresetTrackingSettings(AddPresetBase, bpy.types.Operator):
    """Add or remove a motion tracking settings preset"""

    bl_idname: typing.Any
    bl_label: typing.Any
    bl_options: typing.Any
    bl_rna: typing.Any
    id_data: typing.Any
    name: typing.Any
    order: typing.Any
    preset_defines: typing.Any
    preset_menu: typing.Any
    preset_subdir: typing.Any
    preset_values: typing.Any
    remove_active: typing.Any

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

class AddPresetTrackingTrackColor(AddPresetBase, bpy.types.Operator):
    """Add or remove a Clip Track Color Preset"""

    bl_idname: typing.Any
    bl_label: typing.Any
    bl_options: typing.Any
    bl_rna: typing.Any
    id_data: typing.Any
    name: typing.Any
    order: typing.Any
    preset_defines: typing.Any
    preset_menu: typing.Any
    preset_subdir: typing.Any
    preset_values: typing.Any
    remove_active: typing.Any

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

class AddPresetUnitsLength(AddPresetBase, bpy.types.Operator):
    """Add or remove length units preset"""

    bl_idname: typing.Any
    bl_label: typing.Any
    bl_options: typing.Any
    bl_rna: typing.Any
    id_data: typing.Any
    name: typing.Any
    order: typing.Any
    preset_defines: typing.Any
    preset_menu: typing.Any
    preset_subdir: typing.Any
    preset_values: typing.Any
    remove_active: typing.Any

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

class ExecutePreset(bpy.types.Operator):
    """Execute a preset"""

    bl_idname: typing.Any
    bl_label: typing.Any
    bl_rna: typing.Any
    filepath: typing.Any
    id_data: typing.Any
    menu_idname: typing.Any
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

class WM_MT_operator_presets(bpy.types.Menu):
    bl_label: typing.Any
    bl_rna: typing.Any
    id_data: typing.Any
    preset_operator: typing.Any
    preset_subdir: typing.Any

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
