import typing
import collections.abc
import typing_extensions

class MotionPathButtonsPanel:
    bl_label: typing.Any
    bl_options: typing.Any
    bl_region_type: typing.Any
    bl_space_type: typing.Any

    def draw_settings(self, context, avs, mpath, bones=False):
        """

        :param context:
        :param avs:
        :param mpath:
        :param bones:
        """

class OnionSkinButtonsPanel:
    bl_label: typing.Any
    bl_options: typing.Any
    bl_region_type: typing.Any
    bl_space_type: typing.Any

    def draw(self, context):
        """

        :param context:
        """
