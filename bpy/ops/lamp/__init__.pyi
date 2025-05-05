import typing
import collections.abc
import typing_extensions
import bpy.types

def sunsky_preset_add(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    name: str = "",
    remove_active: bool | None = False,
):
    """Add or remove a Sky & Atmosphere Preset

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param name: Name, Name of the preset, used to make the path name
    :type name: str
    :param remove_active: remove_active
    :type remove_active: bool | None
    """
