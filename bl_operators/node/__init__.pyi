import typing
import collections.abc
import typing_extensions
import bpy.types

class NODE_OT_add_and_link_node(NodeAddOperator, bpy.types.Operator):
    """Add a node to the active tree and link to an existing socket"""

    bl_idname: typing.Any
    bl_label: typing.Any
    bl_options: typing.Any
    bl_rna: typing.Any
    id_data: typing.Any
    link_socket_index: typing.Any
    order: typing.Any
    settings: typing.Any
    type: typing.Any
    use_transform: typing.Any

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

class NODE_OT_add_node(NodeAddOperator, bpy.types.Operator):
    """Add a node to the active tree"""

    bl_idname: typing.Any
    bl_label: typing.Any
    bl_options: typing.Any
    bl_rna: typing.Any
    id_data: typing.Any
    order: typing.Any
    settings: typing.Any
    type: typing.Any
    use_transform: typing.Any

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

class NODE_OT_add_search(NodeAddOperator, bpy.types.Operator):
    """Add a node to the active tree"""

    bl_idname: typing.Any
    bl_label: typing.Any
    bl_options: typing.Any
    bl_property: typing.Any
    bl_rna: typing.Any
    id_data: typing.Any
    node_item: typing.Any
    order: typing.Any
    settings: typing.Any
    type: typing.Any
    use_transform: typing.Any

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

    def find_node_item(self, context):
        """

        :param context:
        """

    def invoke(self, context, event):
        """

        :param context:
        :param event:
        """

    def node_enum_items(self, context):
        """

        :param context:
        """

class NODE_OT_collapse_hide_unused_toggle(bpy.types.Operator):
    """Toggle collapsed nodes and hide unused sockets"""

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

class NODE_OT_tree_path_parent(bpy.types.Operator):
    """Go to parent node tree"""

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

class NodeAddOperator:
    settings: typing.Any
    type: typing.Any
    use_transform: typing.Any

    def create_node(self, context, node_type=None):
        """

        :param context:
        :param node_type:
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

    @staticmethod
    def store_mouse_cursor(context, event):
        """

        :param context:
        :param event:
        """

class NodeSetting(bpy.types.PropertyGroup):
    bl_rna: typing.Any
    id_data: typing.Any
    value: typing.Any

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
