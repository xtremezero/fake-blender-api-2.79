import typing
import collections.abc
import typing_extensions
import bpy.types

def preset_add(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    name: str = "",
    remove_active: bool | None = False,
    use_focal_length: bool | None = False,
):
    """Add or remove a Camera Preset

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param name: Name, Name of the preset, used to make the path name
    :type name: str
    :param remove_active: remove_active
    :type remove_active: bool | None
    :param use_focal_length: Include Focal Length, Include focal length into the preset
    :type use_focal_length: bool | None
    """
