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
    files: bpy.types.bpy_prop_collection[bpy.types.OperatorFileListElement]
    | None = None,
    directory: str = "",
    filter_glob: str = "*.ply",
):
    """Load a PLY geometry file

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param filepath: File Path, Filepath used for importing the file
    :type filepath: str
    :param files: File Path, File path used for importing the PLY file
    :type files: bpy.types.bpy_prop_collection[bpy.types.OperatorFileListElement] | None
    :param directory: directory
    :type directory: str
    :param filter_glob: filter_glob
    :type filter_glob: str
    """

def stl(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    filepath: str = "",
    axis_forward: typing.Literal["X", "Y", "Z", "-X", "-Y", "-Z"] | None = "Y",
    axis_up: typing.Literal["X", "Y", "Z", "-X", "-Y", "-Z"] | None = "Z",
    filter_glob: str = "*.stl",
    files: bpy.types.bpy_prop_collection[bpy.types.OperatorFileListElement]
    | None = None,
    directory: str = "",
    global_scale: float | None = 1.0,
    use_scene_unit: bool | None = False,
    use_facet_normal: bool | None = False,
):
    """Load STL triangle mesh data

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param filepath: File Path, Filepath used for importing the file
    :type filepath: str
    :param axis_forward: Forward
    :type axis_forward: typing.Literal['X','Y','Z','-X','-Y','-Z'] | None
    :param axis_up: Up
    :type axis_up: typing.Literal['X','Y','Z','-X','-Y','-Z'] | None
    :param filter_glob: filter_glob
    :type filter_glob: str
    :param files: File Path
    :type files: bpy.types.bpy_prop_collection[bpy.types.OperatorFileListElement] | None
    :param directory: directory
    :type directory: str
    :param global_scale: Scale
    :type global_scale: float | None
    :param use_scene_unit: Scene Unit, Apply current scene's unit (as defined by unit scale) to imported data
    :type use_scene_unit: bool | None
    :param use_facet_normal: Facet Normals, Use (import) facet normals (note that this will still give flat shading)
    :type use_facet_normal: bool | None
    """
