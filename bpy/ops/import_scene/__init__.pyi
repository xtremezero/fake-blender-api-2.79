import typing
import collections.abc
import typing_extensions
import bpy.types

def autodesk_3ds(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    filepath: str = "",
    axis_forward: typing.Literal["X", "Y", "Z", "-X", "-Y", "-Z"] | None = "Y",
    axis_up: typing.Literal["X", "Y", "Z", "-X", "-Y", "-Z"] | None = "Z",
    filter_glob: str = "*.3ds",
    constrain_size: float | None = 10.0,
    use_image_search: bool | None = True,
    use_apply_transform: bool | None = True,
):
    """Import from 3DS file format (.3ds)

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
    :param constrain_size: Size Constraint, Scale the model by 10 until it reaches the size constraint (0 to disable)
    :type constrain_size: float | None
    :param use_image_search: Image Search, Search subdirectories for any associated images (Warning, may be slow)
    :type use_image_search: bool | None
    :param use_apply_transform: Apply Transform, Workaround for object transformations importing incorrectly
    :type use_apply_transform: bool | None
    """

def fbx(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    filepath: str = "",
    axis_forward: typing.Literal["X", "Y", "Z", "-X", "-Y", "-Z"] | None = "-Z",
    axis_up: typing.Literal["X", "Y", "Z", "-X", "-Y", "-Z"] | None = "Y",
    directory: str = "",
    filter_glob: str = "*.fbx",
    ui_tab: typing.Literal["MAIN", "ARMATURE"] | None = "MAIN",
    use_manual_orientation: bool | None = False,
    global_scale: float | None = 1.0,
    bake_space_transform: bool | None = False,
    use_custom_normals: bool | None = True,
    use_image_search: bool | None = True,
    use_alpha_decals: bool | None = False,
    decal_offset: float | None = 0.0,
    use_anim: bool | None = True,
    anim_offset: float | None = 1.0,
    use_custom_props: bool | None = True,
    use_custom_props_enum_as_string: bool | None = True,
    ignore_leaf_bones: bool | None = False,
    force_connect_children: bool | None = False,
    automatic_bone_orientation: bool | None = False,
    primary_bone_axis: typing.Literal["X", "Y", "Z", "-X", "-Y", "-Z"] | None = "Y",
    secondary_bone_axis: typing.Literal["X", "Y", "Z", "-X", "-Y", "-Z"] | None = "X",
    use_prepost_rot: bool | None = True,
):
    """Load a FBX file

        :type override_context: bpy.types.Context | dict[str, typing.Any]
        :type execution_context: int | str | None
        :type undo: bool | None
        :param filepath: File Path, Filepath used for importing the file
        :type filepath: str
        :param axis_forward: Forward
        :type axis_forward: typing.Literal['X','Y','Z','-X','-Y','-Z'] | None
        :param axis_up: Up
        :type axis_up: typing.Literal['X','Y','Z','-X','-Y','-Z'] | None
        :param directory: directory
        :type directory: str
        :param filter_glob: filter_glob
        :type filter_glob: str
        :param ui_tab: ui_tab, Import options categories

    MAIN Main, Main basic settings.

    ARMATURE Armatures, Armature-related settings.
        :type ui_tab: typing.Literal['MAIN','ARMATURE'] | None
        :param use_manual_orientation: Manual Orientation, Specify orientation and scale, instead of using embedded data in FBX file
        :type use_manual_orientation: bool | None
        :param global_scale: Scale
        :type global_scale: float | None
        :param bake_space_transform: !EXPERIMENTAL! Apply Transform, Bake space transform into object data, avoids getting unwanted rotations to objects when target space is not aligned with Blender's space (WARNING! experimental option, use at own risks, known broken with armatures/animations)
        :type bake_space_transform: bool | None
        :param use_custom_normals: Import Normals, Import custom normals, if available (otherwise Blender will recompute them)
        :type use_custom_normals: bool | None
        :param use_image_search: Image Search, Search subdirs for any associated images (WARNING: may be slow)
        :type use_image_search: bool | None
        :param use_alpha_decals: Alpha Decals, Treat materials with alpha as decals (no shadow casting)
        :type use_alpha_decals: bool | None
        :param decal_offset: Decal Offset, Displace geometry of alpha meshes
        :type decal_offset: float | None
        :param use_anim: Import Animation, Import FBX animation
        :type use_anim: bool | None
        :param anim_offset: Animation Offset, Offset to apply to animation during import, in frames
        :type anim_offset: float | None
        :param use_custom_props: Import User Properties, Import user properties as custom properties
        :type use_custom_props: bool | None
        :param use_custom_props_enum_as_string: Import Enums As Strings, Store enumeration values as strings
        :type use_custom_props_enum_as_string: bool | None
        :param ignore_leaf_bones: Ignore Leaf Bones, Ignore the last bone at the end of each chain (used to mark the length of the previous bone)
        :type ignore_leaf_bones: bool | None
        :param force_connect_children: Force Connect Children, Force connection of children bones to their parent, even if their computed head/tail positions do not match (can be useful with pure-joints-type armatures)
        :type force_connect_children: bool | None
        :param automatic_bone_orientation: Automatic Bone Orientation, Try to align the major bone axis with the bone children
        :type automatic_bone_orientation: bool | None
        :param primary_bone_axis: Primary Bone Axis
        :type primary_bone_axis: typing.Literal['X','Y','Z','-X','-Y','-Z'] | None
        :param secondary_bone_axis: Secondary Bone Axis
        :type secondary_bone_axis: typing.Literal['X','Y','Z','-X','-Y','-Z'] | None
        :param use_prepost_rot: Use Pre/Post Rotation, Use pre/post rotation from FBX transform (you may have to disable that in some cases)
        :type use_prepost_rot: bool | None
    """

def obj(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    filepath: str = "",
    axis_forward: typing.Literal["X", "Y", "Z", "-X", "-Y", "-Z"] | None = "-Z",
    axis_up: typing.Literal["X", "Y", "Z", "-X", "-Y", "-Z"] | None = "Y",
    filter_glob: str = "*.obj;*.mtl",
    use_edges: bool | None = True,
    use_smooth_groups: bool | None = True,
    use_split_objects: bool | None = True,
    use_split_groups: bool | None = True,
    use_groups_as_vgroups: bool | None = False,
    use_image_search: bool | None = True,
    split_mode: typing.Literal["ON", "OFF"] | None = "ON",
    global_clamp_size: float | None = 0.0,
):
    """Load a Wavefront OBJ File

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
        :param use_edges: Lines, Import lines and faces with 2 verts as edge
        :type use_edges: bool | None
        :param use_smooth_groups: Smooth Groups, Surround smooth groups by sharp edges
        :type use_smooth_groups: bool | None
        :param use_split_objects: Object, Import OBJ Objects into Blender Objects
        :type use_split_objects: bool | None
        :param use_split_groups: Group, Import OBJ Groups into Blender Objects
        :type use_split_groups: bool | None
        :param use_groups_as_vgroups: Poly Groups, Import OBJ groups as vertex groups
        :type use_groups_as_vgroups: bool | None
        :param use_image_search: Image Search, Search subdirs for any associated images (Warning, may be slow)
        :type use_image_search: bool | None
        :param split_mode: Split

    ON Split, Split geometry, omits unused verts.

    OFF Keep Vert Order, Keep vertex order from file.
        :type split_mode: typing.Literal['ON','OFF'] | None
        :param global_clamp_size: Clamp Size, Clamp bounds under this value (zero to disable)
        :type global_clamp_size: float | None
    """

def x3d(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    filepath: str = "",
    axis_forward: typing.Literal["X", "Y", "Z", "-X", "-Y", "-Z"] | None = "Z",
    axis_up: typing.Literal["X", "Y", "Z", "-X", "-Y", "-Z"] | None = "Y",
    filter_glob: str = "*.x3d;*.wrl",
):
    """Import an X3D or VRML2 file

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
    """
