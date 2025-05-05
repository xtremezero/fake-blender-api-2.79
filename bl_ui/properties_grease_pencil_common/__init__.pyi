import typing
import collections.abc
import typing_extensions
import bpy.types

class GPENCIL_MT_brush_specials(bpy.types.Menu):
    bl_label: typing.Any
    bl_rna: typing.Any
    id_data: typing.Any

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

class GPENCIL_MT_gpencil_edit_specials(bpy.types.Menu):
    bl_label: typing.Any
    bl_rna: typing.Any
    id_data: typing.Any

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

class GPENCIL_MT_layer_specials(bpy.types.Menu):
    bl_label: typing.Any
    bl_rna: typing.Any
    id_data: typing.Any

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

class GPENCIL_MT_palettecolor_specials(bpy.types.Menu):
    bl_label: typing.Any
    bl_rna: typing.Any
    id_data: typing.Any

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

class GPENCIL_MT_pie_sculpt(bpy.types.Menu):
    """A pie menu for accessing Grease Pencil stroke sculpting settings"""

    bl_label: typing.Any
    bl_rna: typing.Any
    id_data: typing.Any

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

    @classmethod
    def poll(cls, context):
        """

        :param context:
        """

class GPENCIL_MT_pie_settings_palette(bpy.types.Menu):
    """A pie menu for quick access to Grease Pencil settings"""

    bl_label: typing.Any
    bl_rna: typing.Any
    id_data: typing.Any

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

    @classmethod
    def poll(cls, context):
        """

        :param context:
        """

class GPENCIL_MT_pie_tool_palette(bpy.types.Menu):
    """A pie menu for quick access to Grease Pencil tools"""

    bl_label: typing.Any
    bl_rna: typing.Any
    id_data: typing.Any

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

class GPENCIL_MT_pie_tools_more(bpy.types.Menu):
    """A pie menu for accessing more Grease Pencil tools"""

    bl_label: typing.Any
    bl_rna: typing.Any
    id_data: typing.Any

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

    @classmethod
    def poll(cls, context):
        """

        :param context:
        """

class GPENCIL_MT_snap(bpy.types.Menu):
    bl_label: typing.Any
    bl_rna: typing.Any
    id_data: typing.Any

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

class GPENCIL_UL_brush(bpy.types.UIList):
    bl_rna: typing.Any
    id_data: typing.Any

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

    def draw_item(
        self, context, layout, data, item, icon, active_data, active_propname, index
    ):
        """

        :param context:
        :param layout:
        :param data:
        :param item:
        :param icon:
        :param active_data:
        :param active_propname:
        :param index:
        """

class GPENCIL_UL_layer(bpy.types.UIList):
    bl_rna: typing.Any
    id_data: typing.Any

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

    def draw_item(
        self, context, layout, data, item, icon, active_data, active_propname, index
    ):
        """

        :param context:
        :param layout:
        :param data:
        :param item:
        :param icon:
        :param active_data:
        :param active_propname:
        :param index:
        """

class GPENCIL_UL_palettecolor(bpy.types.UIList):
    bl_rna: typing.Any
    id_data: typing.Any

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

    def draw_item(
        self, context, layout, data, item, icon, active_data, active_propname, index
    ):
        """

        :param context:
        :param layout:
        :param data:
        :param item:
        :param icon:
        :param active_data:
        :param active_propname:
        :param index:
        """

class GreasePencilBrushCurvesPanel:
    bl_category: typing.Any
    bl_label: typing.Any
    bl_options: typing.Any
    bl_region_type: typing.Any

    @staticmethod
    def draw(self_, context):
        """

        :param self_:
        :param context:
        """

    @classmethod
    def poll(cls, context):
        """

        :param context:
        """

class GreasePencilBrushPanel:
    bl_category: typing.Any
    bl_label: typing.Any
    bl_region_type: typing.Any

    @staticmethod
    def draw(self_, context):
        """

        :param self_:
        :param context:
        """

class GreasePencilDataPanel:
    bl_label: typing.Any
    bl_region_type: typing.Any

    @staticmethod
    def draw(self_, context):
        """

        :param self_:
        :param context:
        """

    @staticmethod
    def draw_header(self_, context):
        """

        :param self_:
        :param context:
        """

    def draw_layer(self, context, layout, gpl):
        """

        :param context:
        :param layout:
        :param gpl:
        """

    def draw_layers(self, context, layout, gpd):
        """

        :param context:
        :param layout:
        :param gpd:
        """

class GreasePencilDrawingToolsPanel:
    bl_category: typing.Any
    bl_label: typing.Any
    bl_region_type: typing.Any

    @staticmethod
    def draw(self_, context):
        """

        :param self_:
        :param context:
        """

class GreasePencilInterpolatePanel:
    bl_category: typing.Any
    bl_label: typing.Any
    bl_options: typing.Any
    bl_region_type: typing.Any
    bl_space_type: typing.Any

    @staticmethod
    def draw(self_, context):
        """

        :param self_:
        :param context:
        """

    @classmethod
    def poll(cls, context):
        """

        :param context:
        """

class GreasePencilPaletteColorPanel:
    bl_label: typing.Any
    bl_region_type: typing.Any

    @staticmethod
    def draw(self_, context):
        """

        :param self_:
        :param context:
        """

    def draw_palettecolors(self, layout, pcolor):
        """

        :param layout:
        :param pcolor:
        """

    @classmethod
    def poll(cls, context):
        """

        :param context:
        """

class GreasePencilStrokeEditPanel:
    bl_category: typing.Any
    bl_label: typing.Any
    bl_options: typing.Any
    bl_region_type: typing.Any

    @staticmethod
    def draw(self_, context):
        """

        :param self_:
        :param context:
        """

    @classmethod
    def poll(cls, context):
        """

        :param context:
        """

class GreasePencilStrokeSculptPanel:
    bl_category: typing.Any
    bl_label: typing.Any
    bl_region_type: typing.Any

    @staticmethod
    def draw(self_, context):
        """

        :param self_:
        :param context:
        """

    @classmethod
    def poll(cls, context):
        """

        :param context:
        """

class GreasePencilToolsPanel:
    bl_label: typing.Any
    bl_region_type: typing.Any

    @staticmethod
    def draw(self_, context):
        """

        :param self_:
        :param context:
        """

    @classmethod
    def poll(cls, context):
        """

        :param context:
        """

def gpencil_active_brush_settings_simple(context, layout): ...
def gpencil_stroke_placement_settings(context, layout): ...
