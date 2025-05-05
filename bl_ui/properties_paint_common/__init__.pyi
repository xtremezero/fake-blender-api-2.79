import typing
import collections.abc
import typing_extensions
import bpy.types

class UnifiedPaintPanel:
    @staticmethod
    def paint_settings(context):
        """

        :param context:
        """

    @staticmethod
    def prop_unified_color(parent, context, brush, prop_name, text=""):
        """

        :param parent:
        :param context:
        :param brush:
        :param prop_name:
        :param text:
        """

    @staticmethod
    def prop_unified_color_picker(parent, context, brush, prop_name, value_slider=True):
        """

        :param parent:
        :param context:
        :param brush:
        :param prop_name:
        :param value_slider:
        """

    @staticmethod
    def prop_unified_size(
        parent, context, brush, prop_name, icon="NONE", text="", slider=False
    ):
        """

        :param parent:
        :param context:
        :param brush:
        :param prop_name:
        :param icon:
        :param text:
        :param slider:
        """

    @staticmethod
    def prop_unified_strength(
        parent, context, brush, prop_name, icon="NONE", text="", slider=False
    ):
        """

        :param parent:
        :param context:
        :param brush:
        :param prop_name:
        :param icon:
        :param text:
        :param slider:
        """

    @staticmethod
    def prop_unified_weight(
        parent, context, brush, prop_name, icon="NONE", text="", slider=False
    ):
        """

        :param parent:
        :param context:
        :param brush:
        :param prop_name:
        :param icon:
        :param text:
        :param slider:
        """

    @staticmethod
    def unified_paint_settings(parent, context):
        """

        :param parent:
        :param context:
        """

class VIEW3D_MT_tools_projectpaint_clone(bpy.types.Menu):
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

def brush_mask_texture_settings(layout, brush): ...
def brush_texpaint_common(panel, context, layout, brush, settings, projpaint=False): ...
def brush_texture_settings(layout, brush, sculpt): ...
