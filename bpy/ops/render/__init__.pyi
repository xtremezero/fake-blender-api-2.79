import typing
import collections.abc
import typing_extensions
import bpy.types

def cycles_integrator_preset_add(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    name: str = "",
    remove_active: bool | None = False,
):
    """Add an Integrator Preset

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param name: Name, Name of the preset, used to make the path name
    :type name: str
    :param remove_active: remove_active
    :type remove_active: bool | None
    """

def cycles_sampling_preset_add(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    name: str = "",
    remove_active: bool | None = False,
):
    """Add a Sampling Preset

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param name: Name, Name of the preset, used to make the path name
    :type name: str
    :param remove_active: remove_active
    :type remove_active: bool | None
    """

def opengl(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    animation: bool | None = False,
    sequencer: bool | None = False,
    write_still: bool | None = False,
    view_context: bool | None = True,
):
    """OpenGL render active viewport

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param animation: Animation, Render files from the animation range of this scene
    :type animation: bool | None
    :param sequencer: Sequencer, Render using the sequencer's OpenGL display
    :type sequencer: bool | None
    :param write_still: Write Image, Save rendered the image to the output path (used only when animation is disabled)
    :type write_still: bool | None
    :param view_context: View Context, Use the current 3D view for rendering, else use scene settings
    :type view_context: bool | None
    """

def play_rendered_anim(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Play back rendered frames/movies using an external player

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def preset_add(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    name: str = "",
    remove_active: bool | None = False,
):
    """Add or remove a Render Preset

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param name: Name, Name of the preset, used to make the path name
    :type name: str
    :param remove_active: remove_active
    :type remove_active: bool | None
    """

def render(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    animation: bool | None = False,
    write_still: bool | None = False,
    use_viewport: bool | None = False,
    layer: str = "",
    scene: str = "",
):
    """Render active scene

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param animation: Animation, Render files from the animation range of this scene
    :type animation: bool | None
    :param write_still: Write Image, Save rendered the image to the output path (used only when animation is disabled)
    :type write_still: bool | None
    :param use_viewport: Use 3D Viewport, When inside a 3D viewport, use layers and camera of the viewport
    :type use_viewport: bool | None
    :param layer: Render Layer, Single render layer to re-render (used only when animation is disabled)
    :type layer: str
    :param scene: Scene, Scene to render, current scene if not specified
    :type scene: str
    """

def shutter_curve_preset(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    shape: typing.Literal["SHARP", "SMOOTH", "MAX", "LINE", "ROUND", "ROOT"]
    | None = "SMOOTH",
):
    """Set shutter curve

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param shape: Mode
    :type shape: typing.Literal['SHARP','SMOOTH','MAX','LINE','ROUND','ROOT'] | None
    """

def view_cancel(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Cancel show render view

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def view_show(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Toggle show render view

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    """
