import typing
import collections.abc
import typing_extensions
import bpy.types

def active_index_set(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    mode: str = "",
    index: int | None = 0,
):
    """Set active sculpt/paint brush from it's number

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param mode: Mode, Paint mode to set brush for
    :type mode: str
    :param index: Number, Brush number
    :type index: int | None
    """

def add(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Add brush by mode type

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def curve_preset(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    shape: typing.Literal["SHARP", "SMOOTH", "MAX", "LINE", "ROUND", "ROOT"]
    | None = "SMOOTH",
):
    """Set brush shape

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param shape: Mode
    :type shape: typing.Literal['SHARP','SMOOTH','MAX','LINE','ROUND','ROOT'] | None
    """

def reset(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Return brush to defaults based on current tool

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def scale_size(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    scalar: float | None = 1.0,
):
    """Change brush size by a scalar

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param scalar: Scalar, Factor to scale brush size by
    :type scalar: float | None
    """

def stencil_control(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    mode: typing.Literal["TRANSLATION", "SCALE", "ROTATION"] | None = "TRANSLATION",
    texmode: typing.Literal["PRIMARY", "SECONDARY"] | None = "PRIMARY",
):
    """Control the stencil brush

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param mode: Tool
    :type mode: typing.Literal['TRANSLATION','SCALE','ROTATION'] | None
    :param texmode: Tool
    :type texmode: typing.Literal['PRIMARY','SECONDARY'] | None
    """

def stencil_fit_image_aspect(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    use_repeat: bool | None = True,
    use_scale: bool | None = True,
    mask: bool | None = False,
):
    """When using an image texture, adjust the stencil size to fit the image aspect ratio

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param use_repeat: Use Repeat, Use repeat mapping values
    :type use_repeat: bool | None
    :param use_scale: Use Scale, Use texture scale values
    :type use_scale: bool | None
    :param mask: Modify Mask Stencil, Modify either the primary or mask stencil
    :type mask: bool | None
    """

def stencil_reset_transform(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    mask: bool | None = False,
):
    """Reset the stencil transformation to the default

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param mask: Modify Mask Stencil, Modify either the primary or mask stencil
    :type mask: bool | None
    """

def uv_sculpt_tool_set(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    tool: typing.Literal["PINCH", "RELAX", "GRAB"] | None = "PINCH",
):
    """Set the UV sculpt tool

        :type override_context: bpy.types.Context | dict[str, typing.Any]
        :type execution_context: int | str | None
        :type undo: bool | None
        :param tool: Tool

    PINCH Pinch, Pinch UVs.

    RELAX Relax, Relax UVs.

    GRAB Grab, Grab UVs.
        :type tool: typing.Literal['PINCH','RELAX','GRAB'] | None
    """
