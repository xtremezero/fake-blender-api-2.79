import typing
import collections.abc
import typing_extensions
import bpy.types

class LightMapPack(bpy.types.Operator):
    """Pack each faces UV's into the UV bounds"""

    PREF_APPLY_IMAGE: typing.Any
    PREF_BOX_DIV: typing.Any
    PREF_CONTEXT: typing.Any
    PREF_IMG_PX_SIZE: typing.Any
    PREF_MARGIN_DIV: typing.Any
    PREF_NEW_UVLAYER: typing.Any
    PREF_PACK_IN_ONE: typing.Any
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

    def invoke(self, context, event):
        """

        :param context:
        :param event:
        """

class prettyface:
    children: typing.Any
    has_parent: typing.Any
    height: typing.Any
    rot: typing.Any
    uv: typing.Any
    width: typing.Any
    xoff: typing.Any
    yoff: typing.Any

    def place(self, xoff, yoff, xfac, yfac, margin_w, margin_h):
        """

        :param xoff:
        :param yoff:
        :param xfac:
        :param yfac:
        :param margin_w:
        :param margin_h:
        """

    def spin(self): ...

def lightmap_uvpack(
    meshes,
    PREF_SEL_ONLY=True,
    PREF_NEW_UVLAYER=False,
    PREF_PACK_IN_ONE=False,
    PREF_APPLY_IMAGE=False,
    PREF_IMG_PX_SIZE=512,
    PREF_BOX_DIV=8,
    PREF_MARGIN_DIV=512,
):
    """BOX_DIV if the maximum division of the UV map that
    a box may be consolidated into.
    Basically, a lower value will be slower but waist less space
    and a higher value will have more clumpy boxes but more wasted space

    """

def unwrap(operator, context, **kwargs): ...
