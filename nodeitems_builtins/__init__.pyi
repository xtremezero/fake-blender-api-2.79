import typing
import collections.abc
import typing_extensions
import nodeitems_utils

class SortedNodeCategory(nodeitems_utils.NodeCategory): ...

class CompositorNodeCategory(SortedNodeCategory):
    @classmethod
    def poll(cls, context):
        """

        :param context:
        """

class ShaderNewNodeCategory(SortedNodeCategory):
    @classmethod
    def poll(cls, context):
        """

        :param context:
        """

class ShaderOldNodeCategory(SortedNodeCategory):
    @classmethod
    def poll(cls, context):
        """

        :param context:
        """

class TextureNodeCategory(SortedNodeCategory):
    @classmethod
    def poll(cls, context):
        """

        :param context:
        """

def group_input_output_item_poll(context): ...
def group_tools_draw(self_, layout, context): ...
def line_style_shader_nodes_poll(context): ...
def node_group_items(context): ...
def object_shader_nodes_poll(context): ...
def register(): ...
def unregister(): ...
def world_shader_nodes_poll(context): ...
