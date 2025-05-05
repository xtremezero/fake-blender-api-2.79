import typing
import collections.abc
import typing_extensions

class PropertyPanel:
    """The subclass should have its own poll function
    and the variable '_context_path' MUST be set.
    """

    bl_label: typing.Any
    bl_options: typing.Any

    def draw(self, context):
        """

        :param context:
        """

    @classmethod
    def poll(cls, context):
        """

        :param context:
        """

def draw(layout, context, context_member, property_type, use_edit=True): ...
def rna_idprop_context_value(context, context_member, property_type): ...
def rna_idprop_has_properties(rna_item): ...
def rna_idprop_ui_del(item): ...
def rna_idprop_ui_get(item, create=True): ...
def rna_idprop_ui_prop_clear(item, prop, remove=True): ...
def rna_idprop_ui_prop_get(item, prop, create=True): ...
def rna_idprop_ui_prop_update(item, prop): ...
