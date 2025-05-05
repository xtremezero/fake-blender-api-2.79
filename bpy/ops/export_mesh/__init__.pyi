import typing
import collections.abc
import typing_extensions
import bpy.types

def ply(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    filepath: str = "",
    check_existing: bool | None = True,
    axis_forward: typing.Literal["X", "Y", "Z", "-X", "-Y", "-Z"] | None = "Y",
    axis_up: typing.Literal["X", "Y", "Z", "-X", "-Y", "-Z"] | None = "Z",
    filter_glob: str = "*.ply",
    use_mesh_modifiers: bool | None = True,
    use_normals: bool | None = True,
    use_uv_coords: bool | None = True,
    use_colors: bool | None = True,
    global_scale: float | None = 1.0,
):
    """Export a single object as a Stanford PLY with normals, colors and texture coordinates

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param filepath: File Path, Filepath used for exporting the file
    :type filepath: str
    :param check_existing: Check Existing, Check and warn on overwriting existing files
    :type check_existing: bool | None
    :param axis_forward: Forward
    :type axis_forward: typing.Literal['X','Y','Z','-X','-Y','-Z'] | None
    :param axis_up: Up
    :type axis_up: typing.Literal['X','Y','Z','-X','-Y','-Z'] | None
    :param filter_glob: filter_glob
    :type filter_glob: str
    :param use_mesh_modifiers: Apply Modifiers, Apply Modifiers to the exported mesh
    :type use_mesh_modifiers: bool | None
    :param use_normals: Normals, Export Normals for smooth and hard shaded faces (hard shaded faces will be exported as individual faces)
    :type use_normals: bool | None
    :param use_uv_coords: UVs, Export the active UV layer
    :type use_uv_coords: bool | None
    :param use_colors: Vertex Colors, Export the active vertex color layer
    :type use_colors: bool | None
    :param global_scale: Scale
    :type global_scale: float | None
    """

def stl(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    filepath: str = "",
    check_existing: bool | None = True,
    axis_forward: typing.Literal["X", "Y", "Z", "-X", "-Y", "-Z"] | None = "Y",
    axis_up: typing.Literal["X", "Y", "Z", "-X", "-Y", "-Z"] | None = "Z",
    filter_glob: str = "*.stl",
    use_selection: bool | None = False,
    global_scale: float | None = 1.0,
    use_scene_unit: bool | None = False,
    ascii: bool | None = False,
    use_mesh_modifiers: bool | None = True,
    batch_mode: typing.Literal["OFF", "OBJECT"] | None = "OFF",
):
    """Save STL triangle mesh data from the active object

        :type override_context: bpy.types.Context | dict[str, typing.Any]
        :type execution_context: int | str | None
        :type undo: bool | None
        :param filepath: File Path, Filepath used for exporting the file
        :type filepath: str
        :param check_existing: Check Existing, Check and warn on overwriting existing files
        :type check_existing: bool | None
        :param axis_forward: Forward
        :type axis_forward: typing.Literal['X','Y','Z','-X','-Y','-Z'] | None
        :param axis_up: Up
        :type axis_up: typing.Literal['X','Y','Z','-X','-Y','-Z'] | None
        :param filter_glob: filter_glob
        :type filter_glob: str
        :param use_selection: Selection Only, Export selected objects only
        :type use_selection: bool | None
        :param global_scale: Scale
        :type global_scale: float | None
        :param use_scene_unit: Scene Unit, Apply current scene's unit (as defined by unit scale) to exported data
        :type use_scene_unit: bool | None
        :param ascii: Ascii, Save the file in ASCII file format
        :type ascii: bool | None
        :param use_mesh_modifiers: Apply Modifiers, Apply the modifiers before saving
        :type use_mesh_modifiers: bool | None
        :param batch_mode: Batch Mode

    OFF Off, All data in one file.

    OBJECT Object, Each object as a file.
        :type batch_mode: typing.Literal['OFF','OBJECT'] | None
    """
